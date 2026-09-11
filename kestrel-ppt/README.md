# Kestrel — SIH26177 idea presentation kit

> **PS:** SIH26177 · **Qualcomm Inc** · Hardware · Robotics and Drones
> **Idea:** Kestrel — a truck-launched drone swarm that sweeps a disaster zone in hours, not days
> **Deadline:** 20 Sep 2026 · deliverable = **one PDF, six pages**
> **Rewritten:** 9 Sep 2026 — 11 days out

---

## What this kit is

Four files and six slide briefs. Each slide brief carries its prompts, its native-text content, its
layout map and a 30-second script. `DATA.md` holds every number with a source and a confidence tag;
`STYLE.md` holds the palette, the prompt grammar and the rules about what not to draw.

```
kestrel-ppt/
├── README.md   ← you are here: deck map, workflow, what changed
├── DATA.md     ← every number, sourced and tagged. Single source of truth
├── STYLE.md    ← two tiers, both palettes, prompt grammar
├── PROMPTS-TO-RUN.md  ← round 1: the 9 slide-committed prompts, copy-paste ready
├── PROMPTS-ROUND-2.md ← round 2: 9 exploratory prompts, nothing slide-committed yet
├── scripts/whiten.py  ← snaps a render's near-white to pure #FFFFFF and trims the margin
├── images/     ← 12 renders + the official SIH 2026 logo
└── slides/
    ├── slide-1-title.md                  0 prompts (view slide)
    ├── slide-2-proposed-solution.md      3 prompts
    ├── slide-3-technical-approach.md     3 prompts
    ├── slide-4-feasibility-viability.md  3 prompts
    ├── slide-5-impact-benefits.md        3 prompts
    └── slide-6-research-references.md    0 prompts (view slide)
```

**12 prompts total.** No slide has more than three. The two view slides have none, by design.

---

## The format, confirmed

**The actual 2026 template is now in the repo** — `given/SIH2026-IDEA-Presentation-Format.pptx`,
downloaded 9 Sep 2026 from `sih.gov.in/letters/2026/`, publicly linked as "Idea PPT". Full extract:
`given/SIH2026-TEMPLATE-EXTRACT.md`. **Every heading and sub-bullet this kit assumed is confirmed
verbatim — no structural rework.** It also added three constraints, below.

| Rule | Value |
|---|---|
| Slides | **Maximum 6, including the title slide** |
| Upload | **PDF only.** No PPT, no DOC, no other format |
| Content rule | *"Try to avoid paragraphs and post your idea in points, diagrams, infographics, or pictures"* |
| Section headings | Fixed: Title · Proposed Solution · Technical Approach · Feasibility and Viability · Impact and Benefits · Research and References |
| Evaluation | Nine criteria, **no published weightages**: novelty · complexity · clarity and details in the prescribed format · feasibility · practicability · sustainability · scale of impact · **user experience** · potential for future work progression |
| Prize | ₹1,50,000, paid only if Qualcomm likes the winning idea |
| Selection | 4–5 teams per PS reach the Grand Finale (proposed December 2026) |

**Two structural consequences the previous version of this kit got wrong.** First, there is **no
problem slide** — page two is already "Proposed Solution", so the problem has to be established
*inside* the solution. Second, the deck is read **cold, offline, with nobody presenting**, so every
visual has to carry its own labels. Those two facts drive the whole design.

### Three constraints the real PPTX added — one needs your decision

**1. The pointer sub-bullets must stay on every slide.** The instructions slide says you may use the
template *"without changing the idea details pointers."* So *"Detailed explanation of the proposed
solution"* and its siblings remain as text. They ship as Arial 32 pt in a full-width box; they can be
**moved and resized** — that is not changing them — but not deleted or reworded. Plan: **11 pt in a
2.7 in left rail.**

**2. The space is tighter than this kit assumed — measured, not guessed.** Canvas is 13.333 × 7.5 in
(16:9, so every image is the right aspect). After the 1.25 in title, the 0.55 in bottom bar and the
pointer rail, usable area is **10.23 × 5.55 in**:

| Attempt | Result |
|---|---|
| One full-width 16:9 image | 5.76 in tall — **does not fit** |
| **Two 16:9 side by side** | 4.99 × 2.81 in each — fits |
| **Plus one 4:1 band below** | 10.23 × 2.54 in — fits |
| Three full-width 16:9 stacked | needs 17.3 in — **impossible** |

**Real budget: two 16:9 panels + one wide band = three visuals, with no room for large tables.** The
slide files still specify three images *plus* two or three sizeable tables per content slide; **the
tables must compress to 3–4 rows of two short columns, or fold into the images.** The full BOM, risk
register and stack table live in `DATA.md` — a slide never needed line items.

Happily, the shapes already work: the pictogram/row pieces (P3.1, P4.1, P5.1, P5.2) crop to 4:1
bands cleanly, and the cinematic pieces (P2.1, P2.2) want the side-by-side slots. **Nothing needs
regenerating for shape.**

**3. The template is white. Our visual system is dark navy. Your call.**

Shipped: `schemeClr bg1` white background, Times New Roman 36 pt bold titles, a `#0070C0` bottom bar,
a *"Your Team Name"* oval top-left, and the official SIH 2026 brain-lightbulb logo (saffron/green/slate,
saved to `images/_sih2026-official-logo.png`).

| Option | Cost | Risk |
|---|---|---|
| **A — keep white chrome, images as framed dark figure panels** (1 px `#24324A` border, small radius) | Zero. No regeneration. Reads like a journal or conference poster, which is not a bad look for this content | **None.** Template untouched |
| **B — recolour the slide background to `#0B1220`** and keep every heading, pointer, footer, oval and logo exactly as shipped | Zero regeneration; ~20 min of restyling | **Low.** The rule's own qualifier scopes it to *the pointers*, not the palette — but "you can only use provided template" is the sentence, and a strict reader could call a recolour a change |

**Recommendation: A for the submission.** Not because B is likely to be penalised, but because A costs
nothing, removes the only compliance question in the deck, and the argument is carried by the figures
either way — a judge scores the pixel ladder and the survival wall identically on white or navy. Keep
B for the Grand Finale deck, where no template is imposed. **This is a rules-vs-principles call and
it is yours; say the word and I'll cut it either way.**

## Deck map

| # | Slide | Prompts | The one thing this page has to land |
|---|---|---|---|
| 1 | Title | — | Prescribed fields, quiet and typographic. Spend nothing here |
| 2 | Proposed Solution | P2.1 the frog · P2.2 the system · P2.3 the number | The gap isn't aircraft — it's resolution, corroboration and area. Kestrel fixes all three |
| 3 | Technical Approach | P3.1 pixel ladder · P3.2 the gate · P3.3 two airframes | The stack is Qualcomm's, and we sized the sensor with arithmetic — including rejecting our own first choice |
| 4 | Feasibility and Viability | P4.1 cost ladder · P4.2 when it fails · **P4.3 whose asset, whose money** | 27× cheaper per km². Seven named risks with real answers. One number volunteered against us. And it is a **DDMA** asset costing **0.12%** of a budget line that already exists |
| 5 | Impact and Benefits | P5.1 survival wall · **P5.2 the uncounted** · P5.3 the dashboard | **+64 survivors per 100 trapped.** A death toll counts bodies *found* — Nepal has 4,500 still missing. The counting gap is the search gap |
| 6 | Research and References | — | Everything is checkable, and three things we worked out ourselves |

---

## What changed, and why — read before regenerating anything

Six substantive changes from the previous kit. Full detail in `DATA.md` §0.

**1. Seven slides → six, and the problem slide is gone.** The template allows six including the
title. The old deck's slide 2 ("The Problem") does not exist in the prescribed format.

**2. The deck is now a Qualcomm deck.** The problem statement is owned by Qualcomm Inc; the old kit
specced NVIDIA Jetson throughout. Re-specced to the QCS6490 / RB3 Gen 2 (12 TOPS Hexagon NPU,
₹50,000 in India), models compiled through Qualcomm AI Hub and QNN, ModalAI VOXL 2 (QRB5165) named as
the production path, and a **second-hand Snapdragon handset as each scout's brain** — Hexagon NPU,
4K camera, IMU, GNSS and LTE modem in one 190 g ₹9,000 part. Jetson is named once, as the fallback.
This was the single largest available upgrade and it was entirely missing.

**3. Three claims that don't survive scrutiny are now corrections we show off.**

- The mothership **cannot** air-launch six S500 scouts — that is 7.2 kg against a 3 kg lift budget
  from our own PRD. Scouts are **truck-launched**. Operationally better too: a truck-launched scout
  gets five sorties, an air-dropped one gets one.
- Thermal detection at 50 m with a 32×24 MLX90640 is **impossible by optics** — at 30 m it is
  2.68 m/px, so a prone human fills 10% of one pixel (≈0.5 °C apparent, against ±3 °C debris
  clutter). Switched to a **FLIR Lepton 3.5** (160×120, 0.20 m/px at 30 m, ₹16,600 landed). The
  arithmetic is now a slide.
- Coverage rebuilt on the physically-correct thermal swath: **2.6 km²/h**, not 3.5.

**4. The dishonest comparison is gone.** A helicopter is **not** slower than us — it sweeps ~5× more
area per hour. It costs 27× more per km², can't fly at night or in monsoon IMC, and puts one pair of
human eyes at 300 m on the problem. "Helicopters are transport, they were never the sensor" is both
true and more persuasive than the claim it replaces.

**5. Every remaining `[ESTIMATE]` is either sourced or has a free path to a measurement.** The
ground-team baseline is now derived from published sweep-width methodology (Koester et al. 2014) and
independently reproduces how long Wayanad actually took. The helicopter rate comes from IAMSAR
method. On-device inference numbers become *measured* numbers before the finale via **Qualcomm AI
Hub's free profiling on real Snapdragon hardware** — no board purchase required.

**6. Wayanad is the spine, and this monsoon is the scale.** The old deck argued from 2024-25
aggregate mortality. The new one argues from one documented operation — 1,300 personnel, 40 teams,
6 zones, 5+ days, 206 never found, and a thermal scanner that reported three breath signals where
nothing was found — and scales with the monsoon running *now*: 430+ dead across six states,
Jul–Sep 2026.

**Kill the invented rubric weights.** SIH publishes no weightages. The nine criteria are listed
above; *user experience* is one of them, which is why Slide 5 carries a real dashboard.

---

## The visual doctrine, in one line

**No mute images, no naked charts.** Every visual is a third thing: a cinematic or diagrammatic scene
with its numbers rendered inside it. Bar charts, line charts and Gantt charts are banned outright —
nine other teams will submit those. Instead the data is made *physical*: stacked banknotes for cost,
a coarsening pixel grid over a human body for sensor resolution, blocks of 100 people going dark for
the survival curve, solid-versus-ghost figures for the counted and the missing, a descending
staircase for graceful degradation. Full rules in `STYLE.md`.

Six prompts are marked **`[DATA-EXACT]`** (P2.3, P3.1, P4.1, P4.3, P5.1, P5.2). If a single digit comes back
altered, reject the image — regenerate, or rebuild that one visual as native PPT shapes in the same
palette. **A wrong number is worse than a plain chart.**

---

## Generated assets — status

Renders live in `images/`, named by prompt ID. Reviewed 9 Sep 2026.

| Asset | Verdict | Note |
|---|---|---|
| `P2.1-frog.png` | **Ship** | Best image in the deck. All five labels correct |
| `P2.2-hero.png` | **Ship** | All five HUD tags correct, truck-launch reads clearly |
| `P2.3-15km2-twice.png` | **Retired — closest call in the kit** | Excellent render. Its comparison is made twice more (native text here, and in full on Slide 5). Slot goes to the SACHET loop because this slide's sub-bullet is *innovation and uniqueness* and novelty is criterion #1. **Use it to open the Grand Finale deck** |
| `P3.1-pixel-ladder.png` | **Ship** | All nine numerals correct. Human is drawn larger in panel 3 than the brief asked; the coarse-vs-fine grid point still lands in under two seconds |
| `P3.2-gate.png` | **Retired — superseded by v2** | All ten labels correct, but all three of its gates need line of sight, so it could not see a buried person. v2 shows what actually penetrates |
| `P3.3-airframes.png` | **Ship with a nit** | Rendered **8 arms, not 6** — it is an octocopter. Regenerate if there is time; a drone-literate Qualcomm judge may notice. Otherwise avoid the word "hexacopter" in the caption |
| `P4.1-cost-ladder-REDO.png` | **Reject — regenerate with v2** | Unit mismatch in the v1 brief: a rate compared against a capital cost. See v2 in the slide file |
| `P4.2-degradation.png` | **Ship** | Four rungs, unbroken arrow, all captions correct |
| `P4.3-flight-plan.png` | **Retired to the finale deck** | Good asset, all six labels correct — but its slot now carries the procurement argument, which cannot be a table. Roadmap becomes 5 native rows. Prompt archived in the slide file |
| `P5.1-survival-clock-REDO.png` | **Reject — regenerate with v3** | Radial form was wrong for the data; also rendered "Tangshaan". v3 adds the `+64 per 100` delta |
| `P5.2-monsoon-map.png` | **Retired — superseded by v2** | Correct, but it only said "India has disasters". Replaced by *The Uncounted*; its monsoon figures survive as native text |
| `P5.3-dashboard.png` | **Ship** | Mission timer 00:58:14 correct, all three confidence values correct, 71% swept present |

**6 ship as-is · 6 prompts to generate** (P2.3 v2, P3.2 v2, P4.1 v2, P4.3 new, P5.1 v3, P5.2 v2) **· 4 retired to the finale deck · 1 optional nit.**

### Third research pass — 9 Sep 2026 · the input streams

**A real hole in the design, not a deck problem.** The fusion gate ran on thermal + RGB + a second
scout — **all three need line of sight.** A person under a slab has none, so the gate had a coverage
hole over exactly the population the survival curve is about. Both of the deck's anchors sit in that
hole: Wayanad's 206 and Nepal's 4,500 were not people lying visible on a surface.

**The principle that fixes it:** more sensors do not mean more confidence. Sensors that fail for the
*same reason* add almost nothing — thermal and RGB are one vote in two coats. **Independence is what
buys confidence.** Combined by Bayesian evidence accumulation on a geospatial grid, a weak but
*independent* stream can never make the estimate worse. Ten streams, penetration depths, costs and
failure modes are registered in `DATA.md` §11a, with an eleven-item ideation bench in §11g.

| New | Displaces | Why |
|---|---|---|
| **P3.2 v2 — what reaches a buried person** | the three-gate flow | Cutaway showing which streams stop at the surface (RGB, thermal) and which reach the void: **phone WiFi/BLE through 3 m at ₹0**, FINDER-class vital radar to **9 m**, CO2 plume at **3 ppb**, dropped acoustic pods. Closes the frog loop: the only deep stream is also the one that lied at Wayanad — hence one weighted vote, never the decision |
| **P2.3 v2 — the SACHET loop** | 15 km² twice | **The single most novel idea in the project.** C-DOT's cell broadcast, operationalised by NDMA as SACHET, already reaches **1.43 bn citizens across all 36 states via 14.5 M tower cells** and overrides silent/DND. It is used to say *evacuate*. Nobody uses it to make survivors **detectable** — one broadcast saying *"turn Bluetooth on"* turns every handset in the footprint into a beacon, and the scout's own Snapdragon radio is already the receiver |

### Second research pass — 9 Sep 2026

Three new arguments earned a place, and each one *displaces* something rather than adding a seventh
slide. The cap is six pages; the deck is capacity-constrained, not idea-constrained.

| New | Displaces | Why the trade is worth it |
|---|---|---|
| **P4.3 — Whose asset, whose money** | the flight-path roadmap image | Answers *feasibility, practicability, sustainability* and *future work progression* in one frame, and answers the question a government judge is actually holding. ₹19.86 Cr for all 738 districts = **0.12%** of the ₹16,015 Cr preparedness line that already exists. A roadmap tables perfectly; this cannot |
| **P5.2 v2 — The uncounted** | the monsoon map | Nepal, right now: **1,114 confirmed dead, ~4,500 still missing**, after 21,000 personnel and 16 helicopters. A death toll counts bodies *found* — so the counting gap and the search gap are the same gap. The map only said "India has disasters" |
| **P5.1 v3 — the `+64` delta** | nothing — amends an ungenerated prompt | **+64 survivors per 100 people trapped alive.** 99 at 6 h vs 35 at day 3. The single most important output of the project, and it had no visual |

New data in `DATA.md`: §2f Nepal · §2g Assam · §2h the counting gap · §6g the lives-saved rate ·
§9 institutional structure, 15th Finance Commission budget lines, and the CSR route.

---

## Workflow

1. **Confirm the SPOC exists.** Nothing else in this folder matters until the college has a
   registered SPOC and we are nominated out of the internal hackathon.
2. Download the **actual portal template PPTX** the moment team-leader credentials arrive and diff
   its section headings against the six above. If they differ, the slide files re-map; the data does
   not move.
3. Open `STYLE.md`, copy the global prefix, and paste it before every P-prompt.
4. Fire **P2.1 (the frog) first** — it is the most important image in the deck and deserves three
   attempts. Then P2.2. Attach P2.2 to every later cinematic prompt with *"match the lighting,
   palette, material finish and realism of the attached image."*
5. Route prompts to whichever image model in front of you renders in-image text most faithfully.
   Generate 2–3 variants each, cherry-pick, delete the rejects.
6. **Real vendor photographs** for the RB3 Gen 2 board, the Pixhawk, the FLIR Lepton and the phone —
   never generated. A Qualcomm judge knows what their own dev kit looks like.
7. Build the tables and all body text natively in the PPT. Nothing paragraph-shaped; the template
   explicitly asks for points, diagrams and infographics.
8. Export to PDF. Check: **6 pages, under 10 MB, nothing below 14 pt.** Read every page at 25% zoom —
   if the argument isn't legible as shapes and numbers at that size, the hierarchy is wrong.

## Before submitting

- [ ] Re-run `../scripts/verify.py` for the live idea count on SIH26177 — the PS freezes at 500
- [ ] Profile YOLOv8n INT8 on QCS6490 via Qualcomm AI Hub and replace the last inference estimate
- [ ] Screenshot a second-hand Snapdragon 8-series listing to back the ₹9,000 BOM line
- [ ] Team block filled: 6 members, same college, ≥1 female, SPOC letter number
- [ ] Idea title and description entered on the portal, matching the deck
- [ ] Every `[DATA-EXACT]` numeral on every generated image checked against `DATA.md`

## Two things worth knowing before you point a company at this

- **A win splits IP 50/50 with Qualcomm** (guidelines, p.17). Fine for a hackathon artefact. Keep
  Drone Syndicate roadmap detail out of the deck — what is here is the hackathon build, and that is
  deliberate.
- **The idea must be new** and not previously presented in any event or programme. Kestrel as specced
  here — truck-launched, Qualcomm-native, corroboration-gated — has not been submitted anywhere.
