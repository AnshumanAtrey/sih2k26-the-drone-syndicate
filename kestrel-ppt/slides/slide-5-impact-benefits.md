# Slide 5 — Impact and Benefits

**Official section:** "Impact and Benefits"
Template sub-bullets, verbatim: *potential impact on the target audience · benefits of the solution
(social, economic, environmental, etc.)*

**Prompts: 3.** `P5.1` the survival clock · `P5.2` this monsoon · `P5.3` what the commander sees.

---

## The argument this page has to land

Impact here is not a list of adjectives. It is one conversion, done twice:

**Hours → survival probability.** A 15 km² zone swept in 5.8 hours completes inside the window where
extrication survival is ~99%. The same zone searched by 1,300 people completes on day 3+, where it is
~35%. Kestrel does not search faster as an end in itself — it moves the completion of the search from
one side of the survival curve to the other. That is the entire benefit and everything else is
downstream of it.

**Then scale it.** 85% of India's 738 districts are vulnerable to extreme events, and this monsoon
alone — the one running while a judge reads this page — has killed **430+ people across six states**.
Every district-level NDRF/SDRF unit is the same customer, and the same airframe re-tasks for flood,
landslide, earthquake, cyclone and fire without a hardware change.

P5.3 also carries **user experience**, which is one of the nine named criteria in the official
guidelines and which almost no hardware deck bothers to answer.

---

## Layout

```
┌───────────────────────────────────────────────────────────────┐
│  P5.1  THE SURVIVAL WALL — +64 per 100      (full width)      │
├───────────────────────────────────────────────────────────────┤
│  P5.2  THE UNCOUNTED — Nepal + Wayanad      (full width)      │
├───────────────────────────────────────────────────────────────┤
│  P5.3  WHAT THE COMMANDER SEES              (full width)      │
├───────────────────────────────────────────────────────────────┤
│  native strip: FOUR BENEFITS + scale line                     │
└───────────────────────────────────────────────────────────────┘
```

*All three are now wide pictogram/UI bands rather than two squares plus a strip — they stack cleanly
at full width, and each one is legible at 25% zoom because it is a row of countable objects.*

---

## P5.1 — The survival wall `[DATA-EXACT — pictogram infographic]` · **v2**

> **Why v1 failed.** A radial dial was the wrong form for this data. A circle implies *cyclic* time, so
> nothing tells the reader to read clockwise as elapsed hours; it forces the percentages into curved
> text that nobody reads; the bezel and ticks make it look like a speedometer or a radar scope; and the
> cyan hand sitting near vertical reads as "gauge at full", not "finished early". It also carried no
> title, so there was nothing to decode it with. **v2 abandons the circle for a pictogram wall** —
> horizontal, so time reads left to right the way every reader already expects, all text straight, and
> the quantity expressed as *people* rather than as percent. You count the survivors going dark.

Paste the STYLE.md global prefix first.

```
A 16:9 editorial infographic on deep navy, laid out as four large square blocks in a single horizontal row, evenly spaced with generous negative space between them, all sitting on one shared thin slate-grey baseline.

Each block is a precise 10-by-10 grid of 100 small identical human figure icons — simple, flat, front-facing pictogram people, all exactly the same size in all four blocks. Within each block, a number of figures counted from the bottom-left upward are lit and saturated, and the remainder above them are rendered very dark and flat, almost dissolved into the navy background — so each block reads instantly as a partially-drained vessel of people.

- BLOCK 1: 99 of the 100 figures lit in bright green; 1 dark.
- BLOCK 2: 85 lit in green; 15 dark.
- BLOCK 3: 53 lit in amber; 47 dark.
- BLOCK 4: 35 lit in red; 65 dark.

Above the row, two ribbon banners hang down and point to specific blocks with a short stem:
- a CYAN banner positioned over BLOCK 1, containing a small hexacopter icon
- an AMBER banner positioned over BLOCK 4, containing a small human-figure icon

Spanning the space between BLOCK 1 and BLOCK 4, below the two banners but above the blocks, a single horizontal double-headed measuring arrow in bright green, with a small green callout box sitting at its midpoint.

Along the very top of the frame, a single flat title line. Along the bottom, beneath the baseline, a thin footnote line.

Render style: flat editorial pictogram infographic — the visual language of a serious newspaper isotype graphic. Precise alignment, no perspective, no 3D, no glow, no gradients on the figures. Not a bar chart, not a dial. No axes, no legend box.

Text labels (render exactly):
- title line at the top, in #E2E8F0: "OUT OF 100 TRAPPED PEOPLE, HOW MANY ARE STILL ALIVE"
- under BLOCK 1, stacked two lines, green then slate grey: "99 ALIVE" / "AT 6 HOURS"
- under BLOCK 2, stacked two lines, green then slate grey: "85 ALIVE" / "AT 24 HOURS"
- under BLOCK 3, stacked two lines, amber then slate grey: "53 ALIVE" / "AT 48 HOURS"
- under BLOCK 4, stacked two lines, red then slate grey: "35 ALIVE" / "AT 72 HOURS"
- inside the CYAN banner, cyan, stacked two lines: "KESTREL FINISHES" / "5.8 HOURS"
- inside the AMBER banner, amber, stacked two lines: "1,300 PERSONNEL FINISH" / "DAY 3"
- inside the green callout box on the measuring arrow, green, stacked two lines: "+64 SURVIVORS" / "PER 100 TRAPPED"
- footnote line at the bottom, small slate grey: "Survival by extrication time — USAR literature; Tangshan 1976; Campania-Irpinia 1980"

Constraint tail: 16:9. Only the labels listed. All 100 figure positions must be present in every block, lit or dark. No watermark, no border.
```

*Three things to verify: the **figures are the same size in all four blocks** (only the lit count
changes), the **cyan banner sits over the leftmost block and the amber over the rightmost**, and
"Tangshan" is spelled correctly — v1 rendered it "Tangshaan". Percentages trace to `DATA.md` §3;
they are stated here as counts out of 100, which is the same number said in a way a reader feels.
`[DATA-EXACT]`.*

**The `+64` measuring arrow is the whole reason this slide exists.** 99 − 35 = 64, and it is the
single most important output of the project: completing the search in 6 hours instead of 3 days moves
64 people in every 100 trapped from the wrong side of the survival curve to the right one.

**The boundary of that claim, and we state it out loud rather than let a judge find it.** We do *not*
multiply 64% by Wayanad's 206 missing or Nepal's 4,500 — most of those people were carried into river
systems, not held in extractable voids, and presenting them as recoverable would be false. The
population the rate applies to is the entrapped-and-still-alive subset, **which no agency counts**.
So the honest sentence is: *"how many people that is per disaster, nobody currently measures — which
is the second thing this system fixes."* See `DATA.md` §6g.

---

## P5.2 — The uncounted `[DATA-EXACT — pictogram infographic]` · **v2, replaces the monsoon map**

> **Why this replaces v1.** The monsoon map said "India has disasters", which every judge on the panel
> already knows — it was the least load-bearing visual in the deck. This says something a judge has
> almost certainly never had put to them, using figures published by the responding authorities
> themselves, and it is *causal to the product*: **the counting gap and the search gap are the same
> gap.** The current-monsoon scale figures survive as native text in the benefits strip below.

Paste the STYLE.md global prefix first.

```
A 16:9 editorial infographic on deep navy, laid out as two horizontal bands stacked one above the other with generous space between them, both bands sharing the same left margin and the same icon scale.

In each band, a long horizontal run of small identical human-figure pictogram icons, all exactly the same size, reading left to right in a single continuous row that wraps into a second tight row if it runs out of width. Within each band the icons come in exactly two treatments, and the switch between them is abrupt and obvious:
- SOLID icons, filled bright amber, at the start of the run
- GHOST icons, drawn as thin dim grey outlines only with hollow centres, continuing after the solid ones and running much further

UPPER BAND: 11 solid amber icons, then 45 ghost outline icons. The ghost run is dramatically longer than the solid run and should visually dominate the entire frame.
LOWER BAND: 4 solid amber icons, then 2 ghost outline icons. This band is short and sits as a small quiet echo of the one above.

At the far left of each band, outside the icon run, a small vertical tick and a stacked two-line label naming the disaster.

Along the top of the frame, one flat title line. Bottom-left, a small scale key showing one solid icon and one ghost icon side by side. Bottom-right, one short thesis line.

Render style: flat editorial pictogram infographic, newspaper-isotype discipline. Precise alignment, no perspective, no 3D, no glow. Not a bar chart. No axes, no legend box.

Text labels (render exactly):
- title line at the top, in #E2E8F0: "A DEATH TOLL COUNTS THE BODIES THAT WERE FOUND"
- left of the UPPER band, stacked two lines, #E2E8F0 then slate grey: "NEPAL-TIBET" / "AUG 2026"
- above the solid icons in the UPPER band, amber: "1,114 CONFIRMED DEAD"
- above the ghost icons in the UPPER band, slate grey: "4,500 STILL MISSING"
- left of the LOWER band, stacked two lines, #E2E8F0 then slate grey: "WAYANAD" / "JUL 2024"
- above the solid icons in the LOWER band, amber: "357 CONFIRMED DEAD"
- above the ghost icons in the LOWER band, slate grey: "206 STILL MISSING"
- at the scale key, bottom-left, small slate grey: "ONE FIGURE = 100 PEOPLE"
- bottom-right thesis line, cyan, stacked two lines: "21,000 PERSONNEL. 16 HELICOPTERS." / "THE LIMIT IS SEARCH CAPACITY, NOT WILL."

Constraint tail: 16:9. Only the labels listed. Both bands must use the identical icon size. No bodies, no gore, no faces — flat pictograms only. No watermark, no border.
```

*Verify: the two bands must be at the **same icon scale** — Wayanad genuinely was a smaller event and
the lower band looking small is correct, not an error. The ghost run in the upper band must clearly
dwarf everything else on the page; that overflow is the argument.*

**Why this argument is safe and the obvious version is not.** There is real, peer-reviewed evidence
of official under-counting in India — but it sits in *heat* mortality (official 360 heatstroke deaths
Mar–Jul 2023 vs 733 in a media compilation vs ~3,400 excess deaths per extreme-heat day in modelling).
Heat waves are not a search-and-rescue problem, so citing that here is a bait-and-switch a judge will
catch, and it costs more credibility than it buys. And alleging deliberate concealment is unprovable
and, in a government-run hackathon, self-harming.

**The definitional version needs no accusation and cannot be attacked.** A disaster death toll is a
count of bodies recovered and identified; a person never found is never counted as dead, only as
*missing*, in a separate column, often permanently. Nepal committed 21,000 personnel and 16
helicopters and still has ~4,500 people unaccounted for. Nepal's own foreign minister noted the
country *"does not have enough refrigerators to store the dead bodies and identify and test their
DNA."* Nobody is hiding anything. **The count is limited by the capacity to search — which is exactly
what we sell.** Full reasoning and sources in `DATA.md` §2h.

*Nepal's figures move daily. Re-check the NDRRMA toll on the morning of submission and print the
"as of" date on the slide.*

---

## P5.3 — What the commander sees `[high-fidelity UI mockup]`

```
A high-fidelity dark-mode mission-control dashboard filling a 16:9 widescreen frame, designed to the standard of a premium modern web application — real interface, not a stylised impression of one.

TOP BAR: dark slate, with a small cyan wordmark at the left, a mission timer, and a row of seven small status pills (one wider, six narrow).

LEFT COLUMN, narrow: a vertical stack of six small video thumbnails in a 2-by-3 arrangement, one of them visibly a monochrome thermal frame with a bright human-shaped signature, the rest muddy aerial RGB frames.

CENTRE, largest region: a dark tactical map of a landslide-hit valley — pale grey debris polygons, a river, a road. On it: six thin cyan flight-lane ribbons with small drone icons, three pulsing green survivor pins, two red translucent hazard polygons, and one green dashed route line running from a truck icon at the map edge to the nearest green pin. A faint 100 m grid underlies the map.

RIGHT COLUMN: a vertical list of three priority cards, each a rounded dark panel containing a small thumbnail on the left and two lines of text on the right, with a coloured left edge — the top card's edge green, the next two amber. Below the cards, a short block of monospaced generated text in a slightly recessed panel.

Render style: crisp, modern, high-contrast product UI. Real 8-point spacing discipline, legible small type, no skeuomorphism, no glowing sci-fi frames.

Text labels (render exactly):
- top bar: "KESTREL" then "MISSION 00:58:14" then a pill reading "SCOUTS 6/6"
- above the left column, slate grey: "FEEDS"
- above the centre map, slate grey: "LIVE ZONE — 15 KM2 — 71% SWEPT"
- above the right column, slate grey: "RESCUE QUEUE"
- inside the top priority card, two lines: "SURVIVOR 01 — PRONE" and "CONF 0.94 — 3 GATES PASSED"
- inside the second card, two lines: "SURVIVOR 02 — MOBILE" and "CONF 0.81 — HAZARD 40 M"
- inside the third card, two lines: "SURVIVOR 03 — PRONE" and "CONF 0.77 — REVIEW"
- above the monospaced panel, slate grey: "ON-DEVICE REPORT"
- on the green dashed route, green: "SAFE ROUTE"
- on one red polygon, red: "EXPOSED LINES"

Constraint tail: 16:9. Only the labels listed. No cursor, no browser chrome, no operating-system window frame. No watermark, no border.
```

*Two details are load-bearing and must survive the generation: the **mission timer reads 00:58:14**,
which is the expected time-to-first-survivor from `DATA.md` §6d, and **every priority card shows a
confidence value** rather than a bare pin. That is the Wayanad lesson rendered as an interface.*

---

## Native strip — four benefits, one line each

| | Benefit | The number behind it |
|---|---|---|
| **Social** | A 15 km² zone finishes its first full sweep inside the ~99% survival window instead of on day 3 at ~35% | 5.8 h vs 5+ days, on the real Wayanad footprint |
| **Economic** | ₹502/km² against ₹13,800/km² for the deployed alternative, and the capital cost of the whole system is 86 minutes of that alternative | 27× per km²; ₹2.69 L total |
| **Responder safety** | The PS's own first line. Scouts enter unstable debris, flood channels, and structures at risk of secondary collapse; people do not, until a location is confirmed with evidence | 6 expendable ₹25,600 airframes ahead of every entry |
| **Scale & sustainability** | One platform, every Indian disaster profile — flood, landslide, earthquake, cyclone, fire — re-tasked in software, not hardware. Procurable per district under an existing funded budget head, and the scouts are built around parts India already throws away | 85% of 738 districts · scout brain is a second-hand handset · ₹19.86 Cr for national coverage |

**Scale line — native text, one line under the strip.** Carries the current-monsoon figures the map
used to hold, and dates the deck to the week it is read:

> **This monsoon alone, Jul–Sep 2026: 430+ dead across six states** — Himachal Pradesh 261 in 64 days
> (₹1,202 Cr damage), Assam 100 dead with **700,000 displaced, 794 villages and 1,190 km² of cropland
> under water**, J&K 31, Kerala 15, Jharkhand 14, Nagaland 9. **85% of India's 738 districts are
> vulnerable to extreme events.**

*Optional, only if a hole remains in the layout:* one small real photograph of an NDRF team working a
debris field, greyscale, 20% opacity, behind the benefits strip. Not a prompt — do not generate a
rescue scene. On a six-page deck read cold, mood costs space that a number would use better.

---

## 30-second script

> "Here is the whole pitch in one number. Out of a hundred people trapped alive, thirty-five are still
> alive when a search finishes on day three. Ninety-nine are still alive when it finishes in six
> hours. That difference — sixty-four people in every hundred — is what speed actually buys.
>
> How many people that is per disaster, nobody measures, and that's the second thing this fixes. A
> death toll counts the bodies that were found. Right now in Nepal: eleven hundred and fourteen
> confirmed dead, and four and a half thousand people still missing — after twenty-one thousand
> personnel and sixteen helicopters. Nobody is hiding those numbers. The count is limited by the
> capacity to search.
>
> Scale it: eighty-five percent of India's districts are vulnerable, and this monsoon alone has killed
> over four hundred and thirty people across six states. The commander never gets a bare pin — every
> marker arrives with a confidence score and the evidence that produced it."
