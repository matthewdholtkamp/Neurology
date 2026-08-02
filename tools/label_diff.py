#!/usr/bin/env python3
"""
Diff a Neuro Scutbook page's drug claims against the current FDA labels.

This replaces most of what the retired `dose-pharmacist` and `recency-scout` agents
did, at roughly zero cost. Their highest-value findings on the MG page were not
research — they were *comparisons*:

  - "page says nipocalimab is IV or SC" vs label route == INTRAVENOUS only
  - "page says efgartigimod is AChR+" vs label indication has no serostatus qualifier
  - "page names a drug with no dose" vs label has a dosage section
  - "label carries a boxed warning" vs page never mentions one

A script does comparisons better than a language model does: deterministically,
reproducibly, and for free. The model's job shrinks to adjudicating the flags.

Usage:
    python3 tools/label_diff.py docs/nmj/index.md
    python3 tools/label_diff.py docs/nmj/index.md --out review/nmj/15-machine.md
    python3 tools/label_diff.py docs/nmj/index.md --json

Exit code: 1 if any HIGH flag fired. Stdlib only, py3.9+.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lint_page import (  # noqa: E402  — deliberate reuse, not duplication
    DRUG_SUFFIX,
    MONTHS,
    RE_DOSE,
    RE_ORDERSET_BULLET,
    RE_STAMP,
    parse_blocks,
)

UA = "neuro-scutbook-review/1.0 (+https://github.com/matthewdholtkamp/Neurology)"
OPENFDA = "https://api.fda.gov/drug/label.json"
TIMEOUT = 30

# Things that parse as drug bullets but have no FDA label to diff against.
NOT_A_DRUG = re.compile(
    r"^(ivig|plex|plasma exchange|plasmapheresis|immunoadsorption|thymectomy|"
    r"steroid-sparing|corticosteroids?|others?|all\b|both\b|the\b|"
    r"live |vaccin|high-dose|low-dose|pulse |induction|maintenance|regimen|"
    r"dose|dosing|titration|taper)", re.I
)

# openFDA's search is fuzzy enough to return a "match" for phrases like "find and".
# So a candidate must first look like a drug name. Any of these words anywhere in
# the normalized candidate means we're looking at a sentence, not a drug.
STOP_TOKENS = set("""
a an and or the if then to for with without less more most both either neither
all every any some each this that these those it its is are was were be been being
can may might should must will would do does not no give given use used using
avoid check monitor treat consider start stop hold find admit serial intubate
first second third next before after during while when where what who why how
in on at by from up down out off over under again further once here there
only just also very such same than too now then still yet but so
expect expects occur occurs occurred divided mandatory watch reserve raise
lower lowering target note tell warn counsel screen prefer choose pick keep
""".split())


def plausible_drug_name(drug):
    """Cheap gate before we spend a network call — and before openFDA's fuzzy
    matcher hands us a label for something that isn't a drug."""
    words = drug.split()
    if not words:
        return False
    # Split hyphenated compounds too: "start-low-go-slow" is a regimen name, not a
    # drug, and it is only visible as one if you look inside the hyphens.
    parts = [p for w in words for p in w.replace("-", " ").split()]
    if any(p.strip(".,;:") in STOP_TOKENS for p in parts):
        return False
    return len(words[0]) >= 4 and re.match(r"^[a-z][a-z\-]+$", words[0]) is not None

# Serostatus / population qualifiers we compare between page and label.
SEROSTATUS = re.compile(
    r"\b(AChR|MuSK|LRP4|seronegative|serostatus|antibody[- ]positive|"
    r"anti-acetylcholine|anti-muscle)\b", re.I
)
ROUTE_WORDS = {
    # "infusion" is deliberately absent: subcutaneous infusions exist, and mapping
    # it to IV turns "SC infusion once weekly" into a route conflict.
    "IV": "INTRAVENOUS", "intravenous": "INTRAVENOUS",
    "SC": "SUBCUTANEOUS", "subcutaneous": "SUBCUTANEOUS", "subq": "SUBCUTANEOUS",
    "PO": "ORAL", "oral": "ORAL", "orally": "ORAL",
    "IM": "INTRAMUSCULAR", "intramuscular": "INTRAMUSCULAR",
}


def get(url, params=None):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        sys.stderr.write("HTTP %s for %s\n" % (e.code, url[:110]))
        return None
    except Exception as e:
        sys.stderr.write("error: %s\n" % e)
        return None


# ---------------------------------------------------------------------------
# Extract what the page claims
# ---------------------------------------------------------------------------


def normalize_drug(label_text):
    """'Efgartigimod (Vyvgart IV; Vyvgart Hytrulo SC' -> 'efgartigimod'.

    Note we do NOT split on '-': that turns 'Steroid-sparing oral agents' into
    'steroid' and invents a drug that isn't there.
    """
    s = re.split(r"[(—–;,:/]| - ", label_text, 1)[0]
    s = re.sub(r"[*_`]", "", s).strip().lower()
    words = s.split()
    if len(words) > 2:
        words = words[:2]
    return " ".join(words).strip(" .")


def page_claims(path):
    """Every drug bullet on the page, with its full text and location."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    lines = text.split("\n")
    blocks = parse_blocks(lines)
    stamp = RE_STAMP.search(text)
    stamp_ym = None
    if stamp and stamp.group(1) in MONTHS:
        stamp_ym = "%s%02d" % (stamp.group(2), MONTHS.index(stamp.group(1)) + 1)

    claims = []
    seen = set()
    for b in blocks:
        if b.kind not in ("orderset", "tab"):
            continue
        for k, raw in enumerate(b.lines):
            m = RE_ORDERSET_BULLET.match(raw)
            if not m:
                continue
            name = m.group(1).strip()
            indent = len(raw) - len(raw.lstrip())
            chunk = [raw]
            for nxt in b.lines[k + 1:]:
                if not nxt.strip():
                    chunk.append(nxt)
                    continue
                ni = len(nxt) - len(nxt.lstrip())
                if ni <= indent and (re.match(r"^\s*[-*]\s", nxt)
                                     or nxt.strip().startswith("!!!")):
                    break
                chunk.append(nxt)
            body = "\n".join(chunk)
            # Deliberately NOT filtered by lint's looks_like_drug(): that filter is
            # tuned for precision in the linter and drops real drugs whose bullet
            # label is wordy — it dropped efgartigimod, the single most important
            # finding of the first run. Here openFDA itself is the drug detector:
            # anything with a label is a drug, anything without is reported only if
            # the bullet carries independent drug signals (see main()).
            drug = normalize_drug(name)
            if (not drug or NOT_A_DRUG.match(drug) or drug in seen
                    or not plausible_drug_name(drug)):
                continue
            seen.add(drug)
            claims.append({
                "drug": drug, "bullet_label": name,
                "line": b.start + 1 + k, "text": body,
            })
    return claims, stamp_ym, text


# ---------------------------------------------------------------------------
# Fetch the label
# ---------------------------------------------------------------------------

FIELDS = ("indications_and_usage", "dosage_and_administration", "boxed_warning",
          "contraindications", "warnings_and_cautions")


def fetch_label(drug):
    """Try the normalized name, then its first word ('mycophenolate mofetil' ->
    'mycophenolate'). openFDA finding a label is our proof that this is a drug."""
    candidates = [drug]
    first = drug.split()[0] if drug.split() else ""
    if first and first != drug:
        candidates.append(first)
    for cand in candidates:
        for field in ("openfda.generic_name", "openfda.substance_name",
                      "openfda.brand_name"):
            res = get(OPENFDA, {"search": '%s:"%s"' % (field, cand), "limit": 1})
            if res and res.get("results"):
                break
        else:
            continue
        break
    else:
        return None

    # Routes must come from EVERY label for this drug, not the one arbitrary label
    # `limit=1` handed us. Rituximab's first hit is the SC hyaluronidase product;
    # judging "page says IV" against that alone produces a confident wrong answer.
    all_routes = set()
    cnt = get(OPENFDA, {"search": '%s:"%s"' % (field, cand),
                        "count": "openfda.route.exact"})
    if cnt and cnt.get("results"):
        all_routes = set(x["term"] for x in cnt["results"])

    r = res["results"][0]
    o = r.get("openfda", {})
    out = {
        "all_routes": sorted(all_routes),
        "matched_on": "%s (%s)" % (field, cand),
        "brand": ", ".join(o.get("brand_name", []) or []),
        "generic": ", ".join(o.get("generic_name", []) or []),
        "route": sorted(set(o.get("route", []) or [])),
        "effective": r.get("effective_time", ""),
    }
    for f in FIELDS:
        v = r.get(f)
        out[f] = " ".join(" ".join(v).split()) if v else ""
    return out


# ---------------------------------------------------------------------------
# The comparisons — this is the whole point
# ---------------------------------------------------------------------------


def drug_signal(claim):
    """openFDA found nothing — is this still probably a drug? Only then is a
    missing label worth reporting (unapproved, non-US, or off-label)."""
    first = claim["drug"].split()[0] if claim["drug"].split() else ""
    return bool(
        DRUG_SUFFIX.search(first)
        or RE_DOSE.search(claim["text"])
        or re.search(r"\b(IV|SC|PO|IM|subcutaneous|intravenous|oral)\b", claim["text"])
    )


def compare(claim, label, stamp_ym):
    """Return a list of (severity, code, message) flags."""
    flags = []
    page = claim["text"]

    if label is None:
        flags.append(("HIGH", "NO-LABEL",
                      "no FDA label found — may be off-label, non-US, or unapproved. "
                      "Do not assume a dose; say which on the page."))
        return flags

    # 1. Route, judged against the union of every label for this drug.
    #    This is the nipocalimab catch, automated.
    # Look only at the drug's own dosing line, and ignore negated routes. Nested
    # sub-bullets name OTHER drugs' routes ("premedicate with PO diphenhydramine"),
    # and a page that has already been corrected says things like "IV only — no SC
    # formulation is approved". Both produce confident nonsense if read naively.
    own_lines = [page.split("\n")[0]]
    for ln in page.split("\n")[1:]:
        if re.match(r"^\s*[-*]\s", ln):  # a nested bullet — a different drug's text
            break
        own_lines.append(ln)
    route_text = " ".join(own_lines)[:500]
    route_text = re.sub(
        r"\b(no|not|never|without)\b[^.;]{0,40}?\b"
        r"(IV|SC|PO|IM|subcutaneous|intravenous|oral|intramuscular)\b",
        " ", route_text, flags=re.I)
    page_routes = set()
    for word, canon in ROUTE_WORDS.items():
        if re.search(r"\b%s\b" % re.escape(word), route_text):
            page_routes.add(canon)
    label_routes = set(label["all_routes"]) or set(label["route"])
    if page_routes and label_routes:
        extra = page_routes - label_routes
        if extra:
            flags.append(("HIGH", "ROUTE-MISMATCH",
                          "page implies %s; no FDA label for this drug has that "
                          "route (labels cover %s)"
                          % ("/".join(sorted(extra)), "/".join(sorted(label_routes)))))

    # 2. Serostatus / population qualifier. This is the efgartigimod catch — but it
    #    must fire on the page ASSERTING a restriction, not merely discussing
    #    serostatus. A page that correctly explains a restriction was lifted talks
    #    about serostatus more, not less.
    ind = label["indications_and_usage"]
    ind_sero = set(x.lower() for x in SEROSTATUS.findall(ind))
    expansion = re.search(
        r"no serostatus|all (adult )?serotypes|any serotype|regardless of "
        r"(antibody|serostatus)|restriction (was |has been )?(removed|lifted|broadened)",
        page, re.I)
    restriction = re.search(
        r"(AChR|MuSK|LRP4)\+?\s*(only|positive only)\b"
        r"|—\s*\**(AChR|MuSK|LRP4)\+"
        r"|\*\*(AChR|MuSK|LRP4)\+\**\s*[;,.]"
        r"|restricted to|limited to|indicated only", page, re.I)
    if restriction and not expansion and not ind_sero and ind:
        flags.append(("HIGH", "POPULATION-DRIFT",
                      "page asserts a serostatus restriction (%r) but the label's "
                      "indication carries no such qualifier — check whether it was "
                      "removed" % restriction.group(0).strip()))
    elif ind_sero and not SEROSTATUS.search(page):
        flags.append(("MED", "POPULATION-MISSING",
                      "label restricts the indication (%s); the page states no "
                      "restriction" % ", ".join(sorted(ind_sero))))

    # 3. Dose present on the page at all.
    if not RE_DOSE.search(page) and label["dosage_and_administration"]:
        flags.append(("HIGH", "NO-DOSE",
                      "page names this drug with no dose; the label has a dosage "
                      "section"))

    # 4. Boxed warning acknowledged.
    if label["boxed_warning"]:
        if not re.search(r"boxed|black.?box", page, re.I):
            flags.append(("MED", "BOXED-UNMENTIONED",
                          "label carries a BOXED WARNING the page does not mention"))

    # 5. Label revised since the page was reviewed — the cheap staleness signal.
    eff = label["effective"]
    if stamp_ym and eff and len(eff) >= 6 and eff[:6] > stamp_ym:
        flags.append(("MED", "LABEL-NEWER",
                      "label was revised %s-%s, after the page's review stamp — "
                      "re-read it" % (eff[:4], eff[4:6])))

    # 6. Loading/induction language in the label, absent from the page.
    if re.search(r"\b(loading dose|induction|then \d|week 5|initial dose)\b",
                 label["dosage_and_administration"], re.I):
        if not re.search(r"\b(load|loading|induction|then\b|week 5|×\s?4|x\s?4)\b",
                         page, re.I):
            flags.append(("HIGH", "INDUCTION-MISSING",
                          "label describes a loading/induction phase the page's "
                          "dosing does not reflect"))
    return flags


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

SEV_ORDER = {"HIGH": 0, "MED": 1, "LOW": 2}


def render(path, rows, stamp_ym):
    n_high = sum(1 for r in rows for f in r["flags"] if f[0] == "HIGH")
    n_med = sum(1 for r in rows for f in r["flags"] if f[0] == "MED")
    out = []
    out.append("# Label diff — `%s`" % path)
    out.append("")
    out.append("Generated by `tools/label_diff.py` against current FDA labels "
               "(openFDA). Page review stamp: **%s**."
               % (("%s-%s" % (stamp_ym[:4], stamp_ym[4:])) if stamp_ym else "none"))
    out.append("")
    out.append("**%d drug(s) checked — %d HIGH, %d MED flag(s).** Every flag below is a "
               "mechanical comparison, not a judgement: adjudicate each one, do not "
               "apply blindly." % (len(rows), n_high, n_med))
    out.append("")

    flagged = [r for r in rows if r["flags"]]
    clean = [r for r in rows if not r["flags"]]

    if flagged:
        out.append("## Flags")
        for r in sorted(flagged,
                        key=lambda x: min(SEV_ORDER[f[0]] for f in x["flags"])):
            lab = r["label"]
            out.append("")
            out.append("### `%s` — page line %d" % (r["drug"], r["line"]))
            if lab:
                out.append("*Label: %s (%s), route %s, effective %s*"
                           % (lab["generic"] or "—", lab["brand"] or "—",
                              "/".join(lab["route"]) or "—", lab["effective"] or "—"))
            for sev, code, msg in sorted(r["flags"], key=lambda f: SEV_ORDER[f[0]]):
                out.append("- **%s · %s** — %s" % (sev, code, msg))
            out.append("")
            out.append("<details><summary>page text</summary>")
            out.append("")
            out.append("```")
            out.append(r["text"][:900])
            out.append("```")
            out.append("</details>")
            if lab and lab["dosage_and_administration"]:
                out.append("")
                out.append("<details><summary>label dosage</summary>")
                out.append("")
                out.append("```")
                out.append(lab["dosage_and_administration"][:1400])
                out.append("```")
                out.append("</details>")
            if lab and lab["boxed_warning"]:
                out.append("")
                out.append("<details><summary>BOXED WARNING</summary>")
                out.append("")
                out.append("```")
                out.append(lab["boxed_warning"][:900])
                out.append("```")
                out.append("</details>")

    if clean:
        out.append("")
        out.append("## Checked clean")
        out.append("")
        out.append("| Drug | Label | Route | Effective |")
        out.append("|---|---|---|---|")
        for r in clean:
            lab = r["label"]
            out.append("| `%s` | %s | %s | %s |"
                       % (r["drug"], (lab["brand"] or lab["generic"] or "—"),
                          "/".join(lab["route"]) or "—", lab["effective"] or "—"))
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Diff page drug claims vs FDA labels.")
    ap.add_argument("page")
    ap.add_argument("--out", help="write markdown here instead of stdout")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    claims, stamp_ym, _ = page_claims(a.page)
    rows = []
    skipped = []
    for c in claims:
        lab = fetch_label(c["drug"])
        if lab is None and not drug_signal(c):
            # openFDA doesn't know it and the bullet carries no drug signal —
            # it's a heading or a non-pharmacological intervention. Say nothing.
            skipped.append(c["drug"])
            continue
        c["label"] = lab
        c["flags"] = compare(c, lab, stamp_ym)
        rows.append(c)
        time.sleep(0.2)
    if skipped and not a.json:
        sys.stderr.write("not drugs, skipped: %s\n" % ", ".join(skipped))

    if a.json:
        print(json.dumps(rows, indent=2))
    else:
        md = render(a.page, rows, stamp_ym)
        if a.out:
            with open(a.out, "w", encoding="utf-8") as fh:
                fh.write(md + "\n")
            n_high = sum(1 for r in rows for f in r["flags"] if f[0] == "HIGH")
            n_med = sum(1 for r in rows for f in r["flags"] if f[0] == "MED")
            print("%s — %d drug(s), %d HIGH, %d MED"
                  % (a.out, len(rows), n_high, n_med))
        else:
            print(md)

    return 1 if any(f[0] == "HIGH" for r in rows for f in r["flags"]) else 0


if __name__ == "__main__":
    sys.exit(main())
