# given/ — official SIH 2026 source material

Everything here came from **sih.gov.in**, unmodified. Our own derived exports live in `../data/`.

| Path | What it is |
|---|---|
| [`problem-statements/`](problem-statements/) | **229 problem statements**, one markdown file each (`SIH26001.md` … `SIH26229.md`) — every field the site exposes, full description |
| [`problem-statements/00-INDEX.md`](problem-statements/00-INDEX.md) | Single-table index of all 229 |
| [`SIH-2026-Guidelines.pdf`](SIH-2026-Guidelines.pdf) | Official participant guidelines, 26 pp — SPOC registration, internal hackathon, team formation, idea submission, finale |
| [`SIH-2026-Guidelines-College-SPOC.pdf`](SIH-2026-Guidelines-College-SPOC.pdf) | SPOC-facing version of the same guidelines |
| `sih2026PS-raw-2026-08-28.html` | Raw snapshot of https://www.sih.gov.in/sih2026PS as fetched on 2026-08-28 (2.6 MB) — the audit trail the dataset was parsed from |

## Reading a problem-statement file

Each `SIH26NNN.md` is a field table followed by the full description:

```
| Field | Value |
| S.No. · Problem Statement ID · PS Number · Problem Statement Title |
| Organization · Department · Category · Theme |
| Submitted Idea(s) Count · Deadline for Idea Submission · Deadline (ISO) |
| Dataset Link · Contact info · Youtube Link |

## Description
Background: … Description: … Expected Solution: …
```

`N/A` means the field is genuinely blank on the source page — not a scrape miss. `contact` is blank for
all 229 and `youtube` for 224; `dataset_link` is populated for 44.

## Key numbers

- **229** problem statements · **175** Software / **54** Hardware · **17** themes · **32** organisations
- Every statement: deadline **20 September 2026**, idea counter **0/500** (freezes at 500)
- Descriptions run **59 – 11,955 characters**

Full breakdown in [`../data/stats.json`](../data/stats.json); provenance and the diff against public
copies in [`../VERIFICATION.md`](../VERIFICATION.md).
