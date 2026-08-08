#!/usr/bin/env python3
"""
Template conformance linter for Neuro Scutbook pages.

Checks the STRUCTURAL invariants of the canonical "Headache" format — the things
that are mechanically true or false — and stays silent about anything that needs
clinical judgement. That division is the whole point: this script burns none of a
reviewer's attention on whether the Verified footer is present, so the reviewers
can spend all of it on medicine.

Deliberately NOT checked: exact H2 heading wording. Real pages legitimately vary
("Acute (abortive) treatment — the ladder" vs "Maintenance therapy"), and a linter
that demanded the ROADMAP's literal 12 headings would fail every page in the repo.

Usage:
    python3 tools/lint_page.py docs/nmj/index.md
    python3 tools/lint_page.py --all
    python3 tools/lint_page.py --all --strict     # warnings fail too

Exit code: 1 if any ERROR (or, with --strict, any WARN). Stdlib only, py3.9+.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

MONTHS = (
    "January February March April May June July August September October "
    "November December"
).split()

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

RE_STAMP = re.compile(
    r'<span class="reviewed-stamp">Last reviewed: ([A-Z][a-z]+) (\d{4})</span>'
)
RE_VERIFIED = re.compile(r"^\*Verified ([A-Z][a-z]+) (\d{4})", re.M)
RE_ONELINER = re.compile(r"^\*\*One-liner:\*\*", re.M)
RE_ADMON_OPEN = re.compile(r'^!!! (\w+)(?:\s+"(.*)")?\s*$')
# Content tabs (`=== "Refractory / steroid-dependent"`) hold prescribing content too.
# The MG page hid eight undosed biologics in these and the linter passed it clean —
# tabs are dose-checked exactly like order sets.
RE_TAB_OPEN = re.compile(r'^===\+?\s+"(.*)"\s*$')
RE_MD_LINK = re.compile(r"\[[^\]]+\]\((?!#)[^)]+\)")

# A dose is a number followed by a unit, or a frequency/rate expression.
# Kept broad on purpose — a false NEGATIVE here (missing a real dose) is far worse
# than a false positive, which a human dismisses in one second.
RE_DOSE = re.compile(
    r"""(
        \d[\d.,]*\s*(?:–|-|to|/)?\s*[\d.,]*\s*
            (?:mg|mcg|µg|ug|g|kg|units?|IU|U|mL|ml|L|%|mmol|mEq|Gy)\b
      | \d+\s*(?:mg|mcg|g|units?)\s*/\s*kg
      | \bq\s?\d+\s?(?:h|hr|hrs|hours|min|d|days|wk|weeks|mo|months)\b
      | \b(?:BID|TID|QID|QHS|QAM|PRN|daily|once daily|twice daily)\b
      | \bmg/kg\b | \bmcg/kg\b | \bg/kg\b
    )""",
    re.X | re.I,
)

# Bullets inside an orderset that name a bolded agent. Step labels and non-drug
# options are filtered out downstream.
RE_ORDERSET_BULLET = re.compile(r"^\s*[-*]\s+\*\*([^*]+?)\*\*")

# The dose check is deliberately HIGH PRECISION, not high recall. A linter that
# cries wolf gets ignored, and the reviewer agents catch what this misses. So a
# bullet is only held to "must have a dose" when it is positively identifiable as
# a drug — either the name carries a pharmacological suffix, or the bullet names a
# route of administration. Everything else (prisms, PT, CBT-I, thymectomy, nerve
# blocks) is left alone.
DRUG_SUFFIX = re.compile(
    r"(mab|nib|zumab|ximab|umab|cept|tinib|pine|pam|zolam|olol|pril|sartan|"
    r"statin|cillin|mycin|micin|floxacin|azole|prazole|triptan|gabalin|gabapentin|"
    r"toin|barbital|caine|morphone|codone|fentanil|oxetine|sertraline|pramine|"
    r"tyline|azine|peridol|dopa|stigmine|onium|curium|sulfate|chloride|"
    r"prednisone|prednisolone|methasone|cortisone|globulin|immunoglobulin)$",
    re.I,
)
ROUTE = re.compile(
    r"\b(PO|IV|IM|SC|SubQ|subcutaneous|intravenous|oral(?:ly)?|intranasal|IN|PR|"
    r"sublingual|SL|transdermal|infusion|bolus|drip|nebuli[sz]ed|inhaled)\b"
)
# Structural / non-pharmacological bullets — never dose-checked.
NON_DRUG_BULLET = re.compile(
    r"^(step|tier|option|if\b|then\b|escalat|refer|admit|discharge|consult|monitor|"
    r"goal|target|note|caveat|first|second|third|next|stop|start|who|when|"
    r"why|what|but\b|avoid|do not|never|always|surg|thymectomy|plex|plasma|"
    r"physical therapy|\bPT\b|\bOT\b|counsel|educat|document|profile|imaging|"
    r"mri|ct\b|eeg|emg|\blp\b|lumbar|lab|serolog|screen|disposition|follow|"
    r"tools|prism|lens|exercise|rehab|vestibular|reposition|epley|block|"
    r"stimulation|neuromodulation|rtms|tms|cbt|therapy|device|provider|"
    r"evidence|home|office|trial|full|driving|mild|moderate|severe|adrenal|"
    r"diabetes insipidus|siadh|topical|nsaid|pap\b|schedule|"
    r"infusion-related|reaction|counsel|combination|non-pharmacolog)",
    re.I,
)


def looks_like_drug(label, chunk_text):
    """True only when we are confident the bullet prescribes a drug."""
    if NON_DRUG_BULLET.match(label):
        return False
    # Sentences and phrases are labels, not drug names.
    if len(label.split()) > 4:
        return False
    if label.rstrip()[-1:] in ".:?,;":
        return False
    if "," in label or "'" in label or "’" in label:
        return False
    head = label.split()[0].strip("()/-") if label.split() else ""
    return bool(DRUG_SUFFIX.search(head) or ROUTE.search(chunk_text))

MILITARY_FIELDS = {
    "Deployability": re.compile(r"deployab", re.I),
    "Profile": re.compile(r"\bprofile\b", re.I),
    "EPTS/LOD": re.compile(r"\bEPTS\b|\bLOD\b|line of duty|line-of-duty", re.I),
    "Retention": re.compile(r"retention|40-501|6130\.03", re.I),
    "MEB/IDES": re.compile(r"\bMEB\b|\bIDES\b|\bDES\b|\bMAR2\b|1332\.18", re.I),
}

# Pages that are intentionally not clinical topic pages.
NONCLINICAL = {"docs/index.md", "docs/contributing.md"}


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------


class Finding(object):
    def __init__(self, level, code, line, message):
        self.level = level  # ERROR | WARN | INFO
        self.code = code
        self.line = line  # 1-indexed, or 0 for whole-file
        self.message = message


class Block(object):
    """One `!!! type "title"` admonition and its indented body."""

    def __init__(self, kind, title, start, lines):
        self.kind = kind
        self.title = title or ""
        self.start = start  # 1-indexed line of the `!!!` opener
        self.lines = lines  # body lines, original text, indentation intact

    @property
    def body(self):
        return "\n".join(self.lines)


def parse_blocks(lines):
    """Collect top-level admonitions. Nested ones stay inside their parent's body,
    which is what we want — a `!!! warning` inside a `!!! military` is part of it."""
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        m = RE_ADMON_OPEN.match(lines[i])
        tab = None if m else RE_TAB_OPEN.match(lines[i])
        if not m and not tab:
            i += 1
            continue
        kind = m.group(1) if m else "tab"
        title = (m.group(2) if m else tab.group(1))
        start = i
        body = []
        j = i + 1
        while j < n:
            ln = lines[j]
            if ln.strip() == "":
                body.append(ln)
                j += 1
                continue
            if ln.startswith("    ") or ln.startswith("\t"):
                body.append(ln)
                j += 1
                continue
            break
        # trim trailing blanks
        while body and body[-1].strip() == "":
            body.pop()
        blocks.append(Block(kind, title, start + 1, body))
        i = j
    return blocks


def classify(path, text, blocks):
    """clinical | satellite | nonclinical.

    A 'satellite' is a real page that deliberately defers its detail to a dedicated
    page (the TBI comorbidity sub-pages do this) — it carries no military/TRICARE
    box of its own because the hub owns that. Holding those to the full clinical
    requirements would be crying wolf.

    A page can declare its own class with `<!-- lint: satellite -->`; that always
    wins over the heuristic.
    """
    declared = re.search(r"<!--\s*lint:\s*(clinical|satellite|nonclinical)\s*-->", text)
    if declared:
        return declared.group(1)
    rel = path.replace(os.sep, "/")
    for nc in NONCLINICAL:
        if rel.endswith(nc):
            return "nonclinical"
    has_orderset = any(b.kind == "orderset" for b in blocks)
    defers = re.search(
        r"(full detail|doses[^.]{0,60}are on the|see the dedicated|"
        r"covered (?:in full )?on the)[^.]{0,80}\[[^\]]+\]\([^)]+\.md\)",
        text,
        re.I,
    )
    if not has_orderset and defers:
        return "satellite"
    return "clinical"


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


def lint(path):
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    lines = text.split("\n")
    blocks = parse_blocks(lines)
    kind = classify(path, text, blocks)
    out = []

    def add(level, code, line, msg):
        out.append(Finding(level, code, line, msg))

    if kind == "nonclinical":
        return kind, out

    # --- stamp + Verified footer, and that they agree -----------------------
    stamp = RE_STAMP.search(text)
    verified = RE_VERIFIED.search(text)

    if not stamp:
        add("ERROR", "STAMP-MISSING", 0,
            'no `<span class="reviewed-stamp">Last reviewed: MON YYYY</span>`')
    elif stamp.group(1) not in MONTHS:
        add("ERROR", "STAMP-MONTH", 0,
            "stamp month %r is not a full month name" % stamp.group(1))

    if not verified:
        add("ERROR", "VERIFIED-MISSING", 0,
            "no `*Verified MON YYYY: ...*` footer — the page claims a review date "
            "with no audit trail behind it")
    elif stamp:
        if (verified.group(1), verified.group(2)) != (stamp.group(1), stamp.group(2)):
            add("ERROR", "VERIFIED-MISMATCH", 0,
                "stamp says %s %s but footer says %s %s"
                % (stamp.group(1), stamp.group(2),
                   verified.group(1), verified.group(2)))

    # --- opening structure --------------------------------------------------
    if not RE_ONELINER.search(text):
        add("ERROR", "ONELINER-MISSING", 0, "no `**One-liner:**`")

    if not any(b.kind == "danger" for b in blocks):
        add("WARN", "REDFLAG-MISSING", 0,
            "no `!!! danger` red-flag box")

    # --- references ---------------------------------------------------------
    if not re.search(r"^## References", text, re.M):
        add("ERROR", "REFS-MISSING", 0, "no `## References` section")
    else:
        tail = text.split("## References", 1)[1]
        if not RE_MD_LINK.search(tail):
            add("ERROR" if kind == "clinical" else "WARN", "REFS-UNLINKED", 0,
                "References section contains no external links")

    if kind == "clinical" and not re.search(r"^## (?:📚 )?Discover", text, re.M):
        add("WARN", "DISCOVER-MISSING", 0, "no `## 📚 Discover` evidence brief")

    # --- military box -------------------------------------------------------
    mil = [b for b in blocks if b.kind == "military"]
    if not mil:
        if kind == "clinical":
            add("ERROR", "MIL-MISSING", 0, "no `!!! military` box")
    else:
        mb = mil[0]
        if mb.title.startswith("<") or "<topic>" in mb.title:
            add("ERROR", "MIL-PLACEHOLDER", mb.start,
                "military box title is still the template placeholder")
        # A "delta box" explicitly defers the five-field framing to a hub page and
        # carries only what differs for this disease. Holding it to the full field
        # list would force six near-identical boxes across a section, which is the
        # duplication the section-review design exists to remove.
        is_delta = re.search(
            r"(section-wide framing|framing .{0,40}is on the|Only the deltas)",
            mb.body, re.I) and RE_MD_LINK.search(mb.body)
        if not is_delta:
            missing = [name for name, rx in MILITARY_FIELDS.items()
                       if not rx.search(mb.body)]
            if missing:
                add("WARN", "MIL-FIELDS", mb.start,
                    "military box does not mention: %s" % ", ".join(missing))

    # --- order sets + doses -------------------------------------------------
    ordersets = [b for b in blocks if b.kind == "orderset"]
    if kind == "clinical" and not ordersets:
        add("WARN", "ORDERSET-MISSING", 0,
            "no `!!! orderset` box — a clinical page should say what to order")

    drug_bullets = 0
    for b in ordersets + [x for x in blocks if x.kind == "tab"]:
        for k, raw in enumerate(b.lines):
            m = RE_ORDERSET_BULLET.match(raw)
            if not m:
                continue
            name = m.group(1).strip()
            # A bullet runs until the next bullet at the same-or-shallower indent.
            indent = len(raw) - len(raw.lstrip())
            chunk = [raw]
            for nxt in b.lines[k + 1:]:
                if not nxt.strip():
                    chunk.append(nxt)
                    continue
                nindent = len(nxt) - len(nxt.lstrip())
                if nindent <= indent and re.match(r"^\s*[-*]\s", nxt):
                    break
                if nindent <= indent and nxt.strip().startswith("!!!"):
                    break
                chunk.append(nxt)
            chunk_text = "\n".join(chunk)
            if not looks_like_drug(name, chunk_text):
                continue
            drug_bullets += 1
            if not RE_DOSE.search(chunk_text):
                add("WARN", "DOSE-MISSING", b.start + 1 + k,
                    'order-set item "%s" has no dose/frequency — the format '
                    "requires a dose on every drug" % name[:60])

    # --- TRICARE ------------------------------------------------------------
    has_tricare = any(
        b.kind == "tip" and b.title.strip().upper().startswith("TRICARE")
        for b in blocks
    )
    if drug_bullets and not has_tricare and kind == "clinical":
        add("ERROR", "TRICARE-MISSING", 0,
            "page prescribes %d drug(s) but has no `!!! tip \"TRICARE — ...\"` box"
            % drug_bullets)
    if has_tricare:
        tb = [b for b in blocks
              if b.kind == "tip" and b.title.strip().upper().startswith("TRICARE")][0]
        if not re.search(r"formulary search", tb.body, re.I):
            add("WARN", "TRICARE-NOHEDGE", tb.start,
                "TRICARE box does not tell the reader to verify at the Formulary "
                "Search — tiers change without notice")

    # --- leftover template scaffolding --------------------------------------
    for idx, ln in enumerate(lines, 1):
        if re.search(r"<(?:topic|drug|dose|finding|Drug|Topic)[^>]*>", ln):
            add("ERROR", "PLACEHOLDER", idx,
                "unfilled template placeholder: %s" % ln.strip()[:70])
        if "MON YYYY" in ln:
            add("ERROR", "PLACEHOLDER", idx, "literal `MON YYYY` left in page")
        if re.search(r"\bTK\b|\bTODO\b|\bFIXME\b|\bXXX\b", ln):
            add("WARN", "TODO", idx, "unresolved marker: %s" % ln.strip()[:70])

    return kind, out


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

COLOR = sys.stdout.isatty()


def paint(s, c):
    if not COLOR:
        return s
    return {"red": "\033[31m", "yellow": "\033[33m", "dim": "\033[2m",
            "green": "\033[32m", "bold": "\033[1m"}[c] + s + "\033[0m"


DEFAULT_BASELINE = "tools/lint-baseline.txt"


def key_of(rel, f):
    """Baseline key. Line numbers are excluded on purpose so that editing a page
    elsewhere doesn't resurrect an accepted finding."""
    return "%s\t%s\t%s" % (rel, f.code, f.message)


def load_baseline(path):
    if not path or not os.path.exists(path):
        return set()
    keys = set()
    with open(path, "r", encoding="utf-8") as fh:
        for ln in fh:
            ln = ln.rstrip("\n")
            if ln and not ln.startswith("#"):
                keys.add(ln)
    return keys


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Lint Neuro Scutbook pages against the canonical format.")
    ap.add_argument("paths", nargs="*", help="page paths")
    ap.add_argument("--all", action="store_true", help="lint every page under docs/")
    ap.add_argument("--strict", action="store_true", help="warnings are failures")
    ap.add_argument("--quiet", action="store_true",
                    help="only show pages with findings")
    ap.add_argument("--baseline", default=None,
                    help="file of accepted pre-existing findings "
                         "(default: %s if present)" % DEFAULT_BASELINE)
    ap.add_argument("--no-baseline", action="store_true",
                    help="ignore the baseline and show all existing debt")
    ap.add_argument("--update-baseline", action="store_true",
                    help="rewrite the baseline from the current findings")
    args = ap.parse_args(argv)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bl_path = args.baseline or os.path.join(root, DEFAULT_BASELINE)
    baseline = set() if args.no_baseline else load_baseline(bl_path)

    paths = list(args.paths)
    if args.all or not paths:
        docs = os.path.join(root, "docs")
        for dirpath, _dirs, files in os.walk(docs):
            for f in sorted(files):
                if f.endswith(".md"):
                    paths.append(os.path.join(dirpath, f))
        paths.sort()

    n_err = n_warn = n_suppressed = 0
    clean = 0
    all_keys = []

    for p in paths:
        if not os.path.exists(p):
            print(paint("MISSING", "red") + "  %s" % p)
            n_err += 1
            continue
        kind, findings = lint(p)
        rel = os.path.relpath(p, root).replace(os.sep, "/")
        for f in findings:
            all_keys.append(key_of(rel, f))
        live = [f for f in findings if key_of(rel, f) not in baseline]
        n_suppressed += len(findings) - len(live)
        errs = [f for f in live if f.level == "ERROR"]
        warns = [f for f in live if f.level == "WARN"]
        n_err += len(errs)
        n_warn += len(warns)
        if not live:
            clean += 1
            if not args.quiet:
                print("%s  %s %s" % (paint("  ok  ", "green"), rel,
                                     paint("(%s)" % kind, "dim")))
            continue
        print("%s  %s %s" % (paint(" FAIL ", "red") if errs
                             else paint(" warn ", "yellow"),
                             rel, paint("(%s)" % kind, "dim")))
        for f in sorted(live, key=lambda x: (x.level != "ERROR", x.line)):
            loc = ":%d" % f.line if f.line else ""
            tag = paint(f.level, "red" if f.level == "ERROR" else "yellow")
            print("        %s %s%s  %s — %s"
                  % (tag, paint(rel, "dim"), loc, f.code, f.message))

    if args.update_baseline:
        with open(bl_path, "w", encoding="utf-8") as fh:
            fh.write("# Accepted pre-existing lint findings — the site's known debt.\n"
                     "# Regenerate: python3 tools/lint_page.py --all "
                     "--no-baseline --update-baseline\n"
                     "# See what is in here: python3 tools/lint_page.py --all "
                     "--no-baseline\n")
            for k in sorted(set(all_keys)):
                fh.write(k + "\n")
        print()
        print("baseline written: %s (%d finding(s))"
              % (os.path.relpath(bl_path, root), len(set(all_keys))))
        return 0

    print()
    summary = ("%d page(s): %s clean, %s error(s), %s warning(s)"
               % (len(paths), clean,
                  paint(str(n_err), "red") if n_err else "0",
                  paint(str(n_warn), "yellow") if n_warn else "0"))
    if n_suppressed:
        summary += paint(", %d baselined" % n_suppressed, "dim")
    print(summary)

    if n_err or (args.strict and n_warn):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
