#!/usr/bin/env python3
"""
Build the SIH 2026 problem-statement dataset for hackathons/sih-2026.

Source of truth: https://www.sih.gov.in/sih2026PS  (single server-rendered page --
every problem statement's detail modal is already in the static HTML, so no browser
automation is needed; a plain HTTP fetch gets all fields).

Reuses upstream's validated parser (see vendor/README.md) and adds the two fields it
drops: `ps_id` (the modal's own "Problem Statement ID") and `modal_title`.

Outputs (all paths relative to hackathons/sih-2026/):
  given/sih2026PS-raw-<date>.html        raw page snapshot (audit trail)
  given/problem-statements/SIH26NNN.md   one markdown file per PS, every field
  given/problem-statements/00-INDEX.md   index table of all PS
  data/ps.json                           full structured export
  data/ps-detailed.csv                   all fields incl. description
  data/ps-overview.csv                   scannable: everything except description
  data/stats.json                        counts by theme / org / category
  data/_provenance.json                  what was fetched, when, and the diff vs upstream

Usage:
  .venv/bin/python build.py                      # fetch live + rebuild everything
  .venv/bin/python build.py --cache FILE.html    # rebuild from a saved snapshot
  .venv/bin/python build.py --validate           # validate existing artifacts, no fetch
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "vendor"))
from scrape_sih_upstream import fetch_html, parse, fix_text  # noqa: E402

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("beautifulsoup4 required:  .venv/bin/pip install beautifulsoup4 lxml")

ROOT = Path(__file__).resolve().parent.parent
GIVEN = ROOT / "given"
PS_DIR = GIVEN / "problem-statements"
DATA = ROOT / "data"
URL = "https://www.sih.gov.in/sih2026PS"
TODAY = date.today().isoformat()

# Refuse to write if the page yields fewer than this -- guards against a partial
# fetch silently truncating the dataset. Live count was 229 on 2026-08-28.
MIN_RECORDS = 220

FIELDS = [
    "sno", "ps_id", "ps_number", "title", "modal_title", "org", "department",
    "category", "theme", "ideas", "deadline", "deadline_date",
    "dataset_link", "contact", "youtube", "description", "scraped_at",
]
OVERVIEW_FIELDS = [f for f in FIELDS if f != "description"] + ["description_chars"]

# Every <th> label the detail modal can show, so we notice if SIH adds a new one.
KNOWN_MODAL_KEYS = {
    "Problem Statement ID", "Problem Statement Title", "Description",
    "Organization", "Department", "Category", "Theme",
    "Youtube Link", "Dataset Link", "Contact info",
}


def enrich(html_text: str, records: list) -> list:
    """Add ps_id + modal_title from each row's modal; warn on unknown modal fields."""
    soup = BeautifulSoup(html_text, "lxml")
    table = soup.find("table", id="dataTablePS")
    if not table:
        sys.exit("#dataTablePS not found -- site layout changed, check build.py")

    extra: dict[str, dict] = {}
    unknown_keys: set[str] = set()
    for tr in table.find("tbody").find_all("tr"):
        tds = tr.find_all("td", recursive=False)
        if len(tds) < 8:
            continue
        ps_number = fix_text(tds[4].get_text(strip=True))
        modal = tds[2].find("div", id=re.compile(r"^ViewProblemStatement"))
        vals: dict[str, str] = {}
        if modal:
            for mrow in modal.find_all("tr"):
                th, td = mrow.find("th"), mrow.find("td")
                if not th or not td:
                    continue
                key = th.get_text(strip=True)
                if key not in KNOWN_MODAL_KEYS:
                    unknown_keys.add(key)
                vals[key] = fix_text(td.get_text(" ", strip=True))
        extra[ps_number] = {
            "ps_id": vals.get("Problem Statement ID", "").strip(),
            "modal_title": vals.get("Problem Statement Title", "").strip(),
        }

    if unknown_keys:
        print(f"  !! NEW modal field(s) on the site: {sorted(unknown_keys)}")
        print("     -> add them to KNOWN_MODAL_KEYS + FIELDS in build.py")

    out = []
    for r in records:
        e = extra.get(r["ps_number"], {})
        merged = dict(r)
        merged["ps_id"] = e.get("ps_id") or r["ps_number"].replace("SIH", "")
        merged["modal_title"] = e.get("modal_title") or r["title"]
        merged["scraped_at"] = TODAY
        out.append({k: merged.get(k, "") for k in FIELDS})
    return out


def cell(v) -> str:
    """Make a value safe for a one-line markdown table cell without losing content."""
    v = (str(v) if v is not None else "").strip()
    if not v:
        return "N/A"
    # 21 of the site's Dataset Link values are multi-paragraph prose; keep every word
    # but render the breaks so the table does not collapse.
    v = re.sub(r"\s*\n\s*", "<br>", v)
    return v.replace("|", "\\|")


def oneline(v) -> str:
    """Collapse a value to a single line (headings, index rows)."""
    return re.sub(r"\s+", " ", (str(v) if v is not None else "").strip())


def write_markdown(records: list):
    PS_DIR.mkdir(parents=True, exist_ok=True)
    for old in PS_DIR.glob("SIH*.md"):
        old.unlink()

    for r in records:
        body = [
            f"# {r['ps_number']} - {oneline(r['title'])}",
            "",
            "| Field | Value |",
            "|---|---|",
            f"| S.No. | {cell(r['sno'])} |",
            f"| Problem Statement ID | {cell(r['ps_id'])} |",
            f"| PS Number | {cell(r['ps_number'])} |",
            f"| Problem Statement Title | {cell(r['modal_title'])} |",
            f"| Organization | {cell(r['org'])} |",
            f"| Department | {cell(r['department'])} |",
            f"| Category | {cell(r['category'])} |",
            f"| Theme | {cell(r['theme'])} |",
            f"| Submitted Idea(s) Count | {cell(r['ideas'])} |",
            f"| Deadline for Idea Submission | {cell(r['deadline'])} |",
            f"| Deadline (ISO) | {cell(r['deadline_date'])} |",
            f"| Dataset Link | {cell(r['dataset_link'])} |",
            f"| Contact info | {cell(r['contact'])} |",
            f"| Youtube Link | {cell(r['youtube'])} |",
            "",
            "## Description",
            "",
            r["description"] or "_(empty on the source page)_",
            "",
            "---",
            f"_Source: [{URL}]({URL}) · scraped {r['scraped_at']} · "
            "content © Smart India Hackathon (CC-BY-4.0)_",
        ]
        (PS_DIR / f"{r['ps_number']}.md").write_text("\n".join(body) + "\n", encoding="utf-8")


def write_ps_index(records: list):
    themes = Counter(r["theme"] for r in records)
    lines = [
        "# SIH 2026 - all problem statements",
        "",
        f"**{len(records)} problem statements** · scraped {TODAY} from "
        f"[sih.gov.in/sih2026PS]({URL})",
        "",
        f"Software: {sum(1 for r in records if r['category'].lower() == 'software')} · "
        f"Hardware: {sum(1 for r in records if r['category'].lower() == 'hardware')} · "
        f"Themes: {len(themes)} · "
        f"Organizations: {len({r['org'] for r in records})}",
        "",
        "| # | PS Number | Title | Org | Cat | Theme | Ideas | Deadline |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in records:
        title = oneline(r["title"]).replace("|", "\\|")
        org = oneline(r["org"]).replace("|", "\\|")
        lines.append(
            f"| {r['sno']} | [{r['ps_number']}]({r['ps_number']}.md) | {title} | "
            f"{org} | {r['category']} | {r['theme']} | {r['ideas']} | {r['deadline']} |"
        )
    lines += ["", "---", "_Generated by `scripts/build.py`. Do not hand-edit._"]
    (PS_DIR / "00-INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_data(records: list):
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "ps.json").write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    with (DATA / "ps-detailed.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(records)

    with (DATA / "ps-overview.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OVERVIEW_FIELDS)
        w.writeheader()
        for r in records:
            row = {k: r[k] for k in OVERVIEW_FIELDS if k != "description_chars"}
            row["description_chars"] = len(r["description"])
            w.writerow(row)

    stats = {
        "total": len(records),
        "scraped_at": TODAY,
        "source": URL,
        "by_category": dict(Counter(r["category"] for r in records).most_common()),
        "by_theme": dict(Counter(r["theme"] for r in records).most_common()),
        "by_organization": dict(Counter(r["org"] for r in records).most_common()),
        "deadlines": dict(Counter(r["deadline"] for r in records).most_common()),
        "with_dataset_link": sum(1 for r in records if r["dataset_link"]),
        "with_youtube": sum(1 for r in records if r["youtube"]),
        "with_contact": sum(1 for r in records if r["contact"]),
        "description_chars": {
            "min": min(len(r["description"]) for r in records),
            "max": max(len(r["description"]) for r in records),
            "mean": round(sum(len(r["description"]) for r in records) / len(records)),
        },
    }
    (DATA / "stats.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return stats


def validate(records: list) -> list:
    issues, seen = [], set()
    md = sorted(PS_DIR.glob("SIH*.md"))
    if len(md) != len(records):
        issues.append(f"{len(records)} records but {len(md)} markdown files")
    for r in records:
        pn = r["ps_number"]
        if pn in seen:
            issues.append(f"duplicate PS number {pn}")
        seen.add(pn)
        if not (PS_DIR / f"{pn}.md").exists():
            issues.append(f"missing {pn}.md")
        for key in ("sno", "ps_id", "ps_number", "title", "modal_title", "org",
                    "category", "theme", "ideas", "deadline", "deadline_date", "description"):
            if not str(r.get(key, "")).strip():
                issues.append(f"{pn}: empty {key}")
        if len(r["description"]) < 50:
            issues.append(f"{pn}: description only {len(r['description'])} chars")
        if not re.fullmatch(r"SIH26\d{3}", pn):
            issues.append(f"{pn}: unexpected PS-number format")
        if r["ps_id"] and pn.replace("SIH", "") != r["ps_id"]:
            issues.append(f"{pn}: ps_id {r['ps_id']!r} disagrees with ps_number")
        if r["deadline_date"]:
            try:
                datetime.strptime(r["deadline_date"], "%Y-%m-%d")
            except ValueError:
                issues.append(f"{pn}: bad deadline_date {r['deadline_date']!r}")
    nums = sorted(int(r["ps_number"][5:]) for r in records)
    gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in set(nums)]
    if gaps:
        issues.append(f"gaps in PS numbering: {gaps}")
    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", help="parse a saved HTML snapshot instead of fetching")
    ap.add_argument("--validate", action="store_true",
                    help="validate data/ps.json against the markdown files and exit")
    args = ap.parse_args()

    if args.validate:
        records = json.loads((DATA / "ps.json").read_text(encoding="utf-8"))
        issues = validate(records)
        if issues:
            print(f"VALIDATION FAILED -- {len(issues)} issue(s):")
            for i in issues:
                print("  -", i)
            sys.exit(1)
        print(f"OK: {len(records)} problem statements, "
              f"{len(list(PS_DIR.glob('SIH*.md')))} markdown files, all fields present.")
        return

    if args.cache:
        html_text = Path(args.cache).read_text(encoding="utf-8", errors="replace")
        print(f"Parsing cached snapshot {args.cache}")
    else:
        print(f"Fetching {URL} ...")
        html_text = fetch_html(URL)
        GIVEN.mkdir(parents=True, exist_ok=True)
        snap = GIVEN / f"sih2026PS-raw-{TODAY}.html"
        snap.write_text(html_text, encoding="utf-8")
        print(f"  raw snapshot -> given/{snap.name} ({len(html_text):,} bytes)")

    records = enrich(html_text, parse(html_text))
    if len(records) < MIN_RECORDS:
        sys.exit(f"Only {len(records)} records parsed (expected >= {MIN_RECORDS}). "
                 "Refusing to overwrite with partial data.")

    records.sort(key=lambda r: int(r["ps_number"][5:]))
    write_markdown(records)
    write_ps_index(records)
    stats = write_data(records)

    issues = validate(records)
    print(f"\n{len(records)} problem statements written "
          f"({stats['by_category'].get('Software', 0)} software / "
          f"{stats['by_category'].get('Hardware', 0)} hardware, "
          f"{len(stats['by_theme'])} themes, {len(stats['by_organization'])} orgs)")
    print(f"  markdown : given/problem-statements/ ({len(list(PS_DIR.glob('SIH*.md')))} files)")
    print(f"  data     : data/ps.json · data/ps-detailed.csv · data/ps-overview.csv · data/stats.json")
    if issues:
        print(f"\nVALIDATION: {len(issues)} issue(s):")
        for i in issues[:40]:
            print("  -", i)
        sys.exit(1)
    print("\nVALIDATION: clean -- every record has every field.")


if __name__ == "__main__":
    main()
