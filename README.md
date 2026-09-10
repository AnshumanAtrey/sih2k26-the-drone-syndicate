# Smart India Hackathon 2026 (SIH 2026)

> **Status:** all **229** problem statements scraped, verified against the live page, and saved.
> **Nothing submitted yet — the PS pick is still open.**
> **Idea-submission deadline: 20 September 2026 → 23 days from today (Aug 28, 2026).**

India's national hackathon, run by the **Innovation Cell, Ministry of Education + AICTE**. Ministries and
PSUs post real problem statements; student teams submit an idea against one, and shortlisted teams build a
working prototype at an offline Grand Finale (**proposed December 2026**, nodal centres pan-India).

- **Official PS page:** https://www.sih.gov.in/sih2026PS
- **Guidelines:** [`given/SIH-2026-Guidelines.pdf`](given/SIH-2026-Guidelines.pdf) ·
  SPOC version: [`given/SIH-2026-Guidelines-College-SPOC.pdf`](given/SIH-2026-Guidelines-College-SPOC.pdf)
- **All 229 statements:** [`given/problem-statements/00-INDEX.md`](given/problem-statements/00-INDEX.md)
- **Provenance + proof:** [`VERIFICATION.md`](VERIFICATION.md)

---

## The dataset

| Path | What it is |
|---|---|
| [`given/problem-statements/`](given/problem-statements/) | **229 markdown files** — `SIH26001.md` … `SIH26229.md`, every field, full description |
| [`given/problem-statements/00-INDEX.md`](given/problem-statements/00-INDEX.md) | One-table index of all 229 (PS number · title · org · category · theme · ideas · deadline) |
| `data/ps.json` | Full structured export, 17 fields per statement |
| `data/ps-detailed.csv` | Everything incl. the full description |
| `data/ps-overview.csv` | Everything **except** the description + a `description_chars` column — the scannable sheet |
| `data/stats.json` | Counts by theme / org / category / deadline |
| `data/_provenance.json` | Machine-readable audit record (what was fetched, when, diff vs public copies) |
| `given/sih2026PS-raw-2026-08-28.html` | Raw page snapshot the data was parsed from (2.6 MB) |
| `scripts/build.py` | Fetch + parse + emit every artifact above |
| `scripts/verify.py` | Re-check our data against the snapshot and against 5 public copies |
| `scripts/vendor/` | Upstream parser we reuse (MIT, © Vedant Chalke) — see `vendor/README.md` |

### Every field the site exposes (all 17 captured)

| Field | Where it comes from |
|---|---|
| `sno` | list table, col 1 |
| `ps_id` | detail modal → **Problem Statement ID** (e.g. `26001`) |
| `ps_number` | list table, col 5 (e.g. `SIH26001`) |
| `title` | list table, col 3 (the clickable link) |
| `modal_title` | detail modal → Problem Statement Title |
| `org` | list table, col 2 |
| `department` | detail modal → Department |
| `category` | list table, col 4 — `Software` / `Hardware` |
| `theme` | list table, col 7 (**and** modal → Theme; we check both agree) |
| `ideas` | list table, col 6 — submitted / cap, e.g. `0/500` |
| `deadline` | list table, col 8 |
| `deadline_date` | derived ISO form of `deadline` |
| `dataset_link` | detail modal → Dataset Link (populated for 44 of 229) |
| `contact` | detail modal → Contact info (**empty for all 229** on the site right now) |
| `youtube` | detail modal → Youtube Link (populated for 5 of 229) |
| `description` | detail modal → Description — Background / Description / Expected Solution, 59–11,955 chars |
| `scraped_at` | our fetch date |

### Refresh it

```bash
cd scripts
./.venv/bin/python build.py      # re-fetch the live page, rebuild every artifact
./.venv/bin/python verify.py     # re-prove it against the page + public copies
```

Worth re-running weekly until Sep 20 — SIH edits this page live (see below).

---

## Why we scraped instead of taking the GitHub copy

The linked repo ([`vedantchalke36/sih-2026-problem-statements`](https://github.com/vedantchalke36/sih-2026-problem-statements))
is the best public copy and its parser is good — we **reuse** it rather than rewrite it. But its *data* is
stale, and so is every other public copy. Checked all five on Aug 28:

| Dataset | Records | Missing | Themes wrong vs live page |
|---|---|---|---|
| `vedantchalke36/sih-2026-problem-statements` | 226 | 3 | 149 / 226 (66%) |
| `NoBugNinja/Smart-India-Hackathon-SIH-2026-…` | 226 | 3 | 149 / 226 (66%) |
| `Sourav112-droid/sih-2026-problem-statements` | 226 | 3 | 149 / 226 (66%) |
| `sea-deep/sih2026-problem-statements` | 226 | 3 | 149 / 226 (66%) |
| `Rugved-dev18/SIH-2026-official-Software-…` | 172 | 57 | 109 / 172 (63%) |
| **this folder** | **229** | **0** | **0 — every field matches the page** |

Two things every copy gets wrong:

1. **Three statements exist that no public dataset has** — all copies stop at `SIH26226`:
   - **`SIH26227`** · Software · Space Technology · **Ministry of Defence** — Semantic Retrieval and
     Multi-Temporal Change Analysis of Satellite Imagery
   - **`SIH26228`** · Software · Blockchain & Cybersecurity · **Ministry of Defence** — Trustworthy Computer
     Vision Integrity Assurance for Data, Models and Inference Outputs in Multi-Contributor Pipelines
   - **`SIH26229`** · Software · Clean & Green Technology · Ministry of Mines — Kabadiwala Connect: Bringing
     the Informal Collector into the Formal Recycling Chain
2. **SIH re-bucketed the themes** after those copies were taken. `Miscellaneous` went 38 → 15,
   `Smart Automation` 31 → 55, `Blockchain & Cybersecurity` 22 → 31, and `Smart Resource Conservation` was
   retired to zero. Filter by theme on a stale copy and two thirds of the answers are wrong.

No browser automation was needed: `sih2026PS` is one server-rendered page and every statement's detail
modal is already inside the static HTML, so a plain HTTP GET returns all 17 fields. Playwright/Puppeteer
would have added a browser for nothing. There is also **no official 2026 spreadsheet** — sih.gov.in only
hosts `SIH_PS_2024.xlsx`.

### Source-side quirks (kept as-is, do not "fix" silently)

- `Ministry of Defence (MoD)` (1 PS) and `Ministry of defence (MoD)` (2 PS) — **two spellings, same
  ministry.** Filter case-insensitively or you lose records.
- `Governmcnt of Jharkhand` (5 PS) — the site's own typo for *Government of Jharkhand*.
- `contact` is empty on all 229; `youtube` on 224. Not a scrape failure — the site's fields are blank.

---

## The landscape

**229 statements · 175 Software / 54 Hardware · 17 themes · 32 organisations · all due 20 Sep 2026 · all at 0/500 ideas.**

| Theme | PS | | Organisation | PS |
|---|---:|---|---|---:|
| Smart Automation | 55 | | AICTE | 34 |
| **Blockchain & Cybersecurity** | **31** | | Ministry of Earth Sciences (MoES) | 30 |
| Disaster Management | 25 | | National Technical Research Organisation (NTRO) | 23 |
| Agriculture, FoodTech & Rural Dev | 22 | | ISRO | 11 |
| MedTech / BioTech / HealthTech | 18 | | Ministry of Home Affairs | 11 |
| Miscellaneous | 15 | | Ministry of Rural Development | 10 |
| **Robotics and Drones** | **12** | | Ministry of Consumer Affairs | 10 |
| Smart Education | 11 | | Government of Maharashtra | 9 |
| Space Technology | 9 | | Ministry of Social Justice (MoSJE) | 8 |
| Transportation & Logistics | 7 | | **DRDO** | **7** |
| Clean & Green Technology | 7 | | MDoNER | 5 |
| Smart Vehicles | 6 | | `Governmcnt of Jharkhand` | 5 |
| Heritage & Culture | 3 | | *…20 more* | |
| Fitness & Sports · Renewable Energy · Travel & Tourism · Toys & Games | 2 each | | **Ministry of Defence** | **3** |

Two themes line up with what we already build — **Blockchain & Cybersecurity (31)** for the Walrus
Securitas lane, **Robotics and Drones (12)** for the Drone Syndicate lane — and the defence-adjacent
orgs (DRDO 7 · NTRO 23 · MoD 3 · MHA 11 · ISRO 11) are where the iDEX-shaped work lives. Nothing picked
yet; that's the next conversation.

---

## Rules that actually constrain us (from the official guidelines)

| Rule | Consequence |
|---|---|
| **Students cannot register directly.** A college **SPOC** (faculty member) registers the college, runs an internal hackathon, and nominates teams. | No SPOC → no entry. This is the first thing to check, before picking a PS. |
| Only students **selected in the college's internal hackathon** can be nominated. | The internal hackathon is the real qualifier. |
| Team = **exactly 6 members, all from the same college.** No inter-college teams. | Gayatri can't be on the team unless she's at the same college. Need 6 from ours. |
| **At least one female member is mandatory.** | Team composition constraint, not optional. |
| Max **50 teams per college** (45 + 5 waitlisted); 100 per university. | Competing internally for a slot. |
| One team may submit against **max 2 problem statements**. | We get two shots, not twenty. |
| **500-idea cap per PS — the PS freezes at 500.** Counter is public, live, and all 229 sit at `0/500`. | Submitting early is a real edge on any popular PS. |
| **Last date for nomination + idea submission: 20 Sep 2026.** "No request will be entertained after the deadline." | 23 days. |
| **4–5 teams per PS** reach the Grand Finale; the PS-owning org is not obliged to declare a winner. | Selection is per-PS, so PS choice ≈ competition level. |
| Submission = team details + college authorisation letter (letterhead, principal-signed, sealed) + PS choice + idea title + description + **idea presentation PDF**. | The PDF is the deliverable. |
| Grand Finale offline at an assigned nodal centre, **anywhere in India**, ~Dec 2026. Travel reimbursed to **₹3,000/person**; accommodation arranged. | Travel is largely covered but capped. |
| **IP of a winning idea is split 50/50 with the organisation that posted the problem statement** (or by mutual agreement). | Flagging once: a win on a MoD/DRDO statement means shared IP on that work. Fine for a hackathon artefact, worth knowing before pointing a *company* build at it. |
| The idea **must be new** — not presented in any previous event/programme. | The Samsung Solve for Tomorrow Walrus Securitas submission can't be re-filed as-is here. |

---

## Status log

- **2026-08-28** — Folder created. Audited five public datasets + the official site: no 2026 spreadsheet
  exists, and every public copy is stale (226 records, 66% wrong themes). Scraped the live page instead,
  reusing upstream's parser and adding the `ps_id` / `modal_title` fields it drops. **229 statements saved**
  as markdown + JSON + detailed CSV + overview CSV; `verify.py` confirms **0 field mismatches** against the
  page snapshot. Official guidelines pulled into `given/`. **Next: pick the problem statement(s)** — and
  confirm whether our college has a registered SPOC, since that gates everything.
