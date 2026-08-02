#!/usr/bin/env python3
"""
Deterministic evidence pulls for the Neuro Scutbook review pipeline.

This is the half of the review that must NOT be a language model. Trial lists and
FDA label text are facts with addresses; looking them up in code makes them
reproducible, re-runnable, and citable by PMID/NCT number rather than by vibe.

All four endpoints are public and need no key (PubMed allows ~3 req/s unkeyed,
which is why the polite sleep is here).

    python3 tools/evidence.py pubmed  --query "myasthenia gravis treatment" --since 2024
    python3 tools/evidence.py trials  --cond "myasthenia gravis" --phase 3 --since 2024
    python3 tools/evidence.py label   --drug efgartigimod
    python3 tools/evidence.py label   --drug pyridostigmine --section dosage

Add --json for machine-readable output. Stdlib only, py3.9+.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "neuro-scutbook-review/1.0 (+https://github.com/matthewdholtkamp/Neurology)"
TIMEOUT = 30


def get(url, params=None):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        sys.stderr.write("HTTP %s for %s\n" % (e.code, url[:120]))
        return None
    except Exception as e:  # network, JSON, timeout
        sys.stderr.write("error: %s (%s)\n" % (e, url[:120]))
        return None


# ---------------------------------------------------------------------------
# PubMed
# ---------------------------------------------------------------------------

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def pubmed(query, since, maxn, pubtypes):
    term = query
    if pubtypes:
        clauses = " OR ".join('"%s"[Publication Type]' % p for p in pubtypes)
        term = "(%s) AND (%s)" % (term, clauses)
    res = get(EUTILS + "esearch.fcgi", {
        "db": "pubmed", "term": term, "retmax": maxn, "retmode": "json",
        "sort": "date", "datetype": "pdat",
        "mindate": "%s/01/01" % since, "maxdate": "3000",
    })
    if not res:
        return []
    ids = res.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    time.sleep(0.4)
    summ = get(EUTILS + "esummary.fcgi",
               {"db": "pubmed", "id": ",".join(ids), "retmode": "json"})
    if not summ:
        return []
    out = []
    result = summ.get("result", {})
    for pmid in result.get("uids", []):
        d = result.get(pmid, {})
        doi = ""
        for aid in d.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = aid.get("value", "")
        out.append({
            "pmid": pmid,
            "title": d.get("title", "").rstrip("."),
            "journal": d.get("source", ""),
            "date": d.get("pubdate", ""),
            "type": ", ".join(d.get("pubtype", [])),
            "doi": doi,
            "url": "https://pubmed.ncbi.nlm.nih.gov/%s/" % pmid,
        })
    return out


# ---------------------------------------------------------------------------
# ClinicalTrials.gov v2
# ---------------------------------------------------------------------------

CTG = "https://clinicaltrials.gov/api/v2/studies"


def trials(cond, phase, since, maxn):
    params = {"query.cond": cond, "pageSize": min(maxn, 100),
              "sort": "LastUpdatePostDate:desc"}
    filt = []
    if phase:
        filt.append("AREA[Phase]PHASE%s" % phase)
    if since:
        filt.append("AREA[LastUpdatePostDate]RANGE[%s-01-01,MAX]" % since)
    if filt:
        params["filter.advanced"] = " AND ".join(filt)
    res = get(CTG, params)
    if not res:
        return []
    out = []
    for s in res.get("studies", [])[:maxn]:
        ps = s.get("protocolSection", {})
        ident = ps.get("identificationModule", {})
        status = ps.get("statusModule", {})
        design = ps.get("designModule", {})
        nct = ident.get("nctId", "")
        out.append({
            "nct": nct,
            "title": ident.get("briefTitle", ""),
            "acronym": ident.get("acronym", ""),
            "status": status.get("overallStatus", ""),
            "phase": "/".join(design.get("phases", []) or []),
            "completion": (status.get("primaryCompletionDateStruct", {}) or {})
                          .get("date", ""),
            "updated": (status.get("lastUpdatePostDateStruct", {}) or {})
                       .get("date", ""),
            "url": "https://clinicaltrials.gov/study/%s" % nct,
        })
    return out


# ---------------------------------------------------------------------------
# openFDA drug labels
# ---------------------------------------------------------------------------

OPENFDA = "https://api.fda.gov/drug/label.json"

LABEL_SECTIONS = {
    "dosage": "dosage_and_administration",
    "boxed": "boxed_warning",
    "contraindications": "contraindications",
    "warnings": "warnings_and_cautions",
    "indications": "indications_and_usage",
    "pregnancy": "pregnancy",
    "pediatric": "pediatric_use",
}


def label(drug, sections):
    res = None
    for field in ("openfda.generic_name", "openfda.brand_name",
                  "openfda.substance_name"):
        res = get(OPENFDA, {"search": '%s:"%s"' % (field, drug), "limit": 1})
        if res and res.get("results"):
            break
    if not res or not res.get("results"):
        return None
    r = res["results"][0]
    ofda = r.get("openfda", {})
    out = {
        "query": drug,
        "generic": ", ".join(ofda.get("generic_name", []) or []),
        "brand": ", ".join(ofda.get("brand_name", []) or []),
        "manufacturer": ", ".join(ofda.get("manufacturer_name", []) or []),
        "label_effective": r.get("effective_time", ""),
        "sections": {},
    }
    wanted = sections or list(LABEL_SECTIONS.keys())
    for key in wanted:
        fld = LABEL_SECTIONS.get(key)
        if not fld:
            continue
        val = r.get(fld)
        if val:
            out["sections"][key] = "\n".join(val) if isinstance(val, list) else str(val)
    return out


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def render_pubmed(rows, since):
    if not rows:
        return "_No PubMed hits since %s._" % since
    out = ["| Date | Journal | Title | PMID |", "|---|---|---|---|"]
    for r in rows:
        t = r["title"].replace("|", "\\|")
        out.append("| %s | %s | %s | [%s](%s) |"
                   % (r["date"], r["journal"], t[:150], r["pmid"], r["url"]))
    return "\n".join(out)


def render_trials(rows):
    if not rows:
        return "_No matching trials._"
    out = ["| NCT | Acronym | Phase | Status | Primary completion | Title |",
           "|---|---|---|---|---|---|"]
    for r in rows:
        t = r["title"].replace("|", "\\|")
        out.append("| [%s](%s) | %s | %s | %s | %s | %s |"
                   % (r["nct"], r["url"], r["acronym"] or "—", r["phase"] or "—",
                      r["status"], r["completion"] or "—", t[:110]))
    return "\n".join(out)


def render_label(d, truncate):
    if not d:
        return "_No FDA label found. This is meaningful: it may be off-label, "\
               "non-US, or not yet approved — do not assume a dose._"
    out = ["**%s** (%s) — label effective %s"
           % (d["generic"] or d["query"], d["brand"] or "—",
              d["label_effective"] or "unknown")]
    for k, v in d["sections"].items():
        body = " ".join(v.split())
        if truncate and len(body) > truncate:
            body = body[:truncate] + " …[truncated]"
        out.append("\n### %s\n%s" % (k, body))
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--json", action="store_true", help="raw JSON output")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("pubmed", help="recent literature")
    p.add_argument("--query", required=True)
    p.add_argument("--since", default="2024", help="earliest publication year")
    p.add_argument("--max", type=int, default=25)
    p.add_argument("--types", nargs="*", default=None,
                   help='e.g. "Randomized Controlled Trial" "Practice Guideline"')

    t = sub.add_parser("trials", help="ClinicalTrials.gov")
    t.add_argument("--cond", required=True)
    t.add_argument("--phase", default=None, help="2, 3, ...")
    t.add_argument("--since", default="2024")
    t.add_argument("--max", type=int, default=25)

    l = sub.add_parser("label", help="FDA label text (authoritative dosing)")
    l.add_argument("--drug", required=True)
    l.add_argument("--section", nargs="*", default=None,
                   choices=sorted(LABEL_SECTIONS.keys()))
    l.add_argument("--truncate", type=int, default=1200,
                   help="chars per section; 0 = full")

    a = ap.parse_args(argv)

    if a.cmd == "pubmed":
        rows = pubmed(a.query, a.since, a.max, a.types)
        print(json.dumps(rows, indent=2) if a.json
              else render_pubmed(rows, a.since))
    elif a.cmd == "trials":
        rows = trials(a.cond, a.phase, a.since, a.max)
        print(json.dumps(rows, indent=2) if a.json else render_trials(rows))
    elif a.cmd == "label":
        d = label(a.drug, a.section)
        print(json.dumps(d, indent=2) if a.json
              else render_label(d, a.truncate or 0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
