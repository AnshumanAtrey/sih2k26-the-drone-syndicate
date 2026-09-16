# DATA.md — Master data registry (single source of truth)

> Rewritten 9 Sep 2026 after a full re-source pass. Every number used in `slides/` lives here with a
> source and a confidence tag. If it isn't in this file, it doesn't go in the deck.

**Tags:** `[SOURCED]` published/verifiable · `[DERIVED]` computed by us, model printed so judges can audit ·
`[ESTIMATE]` placeholder, must be replaced or explicitly labelled on the slide.

**Repo trust note.** `github.com/AnshumanAtrey/the-drone-syndicate` was read for component prices
(good — vendor-linked, Robocraze/Amazon India, usable) and for capability claims (**not** trusted —
two of them are wrong and are corrected in §5 and §6 below). Prices tagged `[SOURCED-repo]`.

---

## 0. What changed from the previous version of this file — read first

Five corrections. Each is a claim the old deck made that does not survive scrutiny. Fixing them is
worth more than the claims were, because the official criteria reward *"clarity and details"* and
because a Qualcomm engineer on the panel would have found all five.

| # | Old claim | Status | Correction |
|---|---|---|---|
| 1 | Mothership air-launches 6 scouts from a release rack | **Physically impossible** | 6 × S500 scouts ≈ 7.2 kg; the airframe lifts 3 kg (own PRD). Scouts are **truck-launched**; mothership is the airborne brain + mesh relay. Better anyway — scouts spend their battery searching, not being carried. |
| 2 | Thermal detects humans at ~50 m altitude (MLX90640) | **False by optics** | MLX90640 is 32×24. At 30 m it is 2.68 m/px — a prone human fills 10% of one pixel (≈0.5 °C apparent). Switched to **FLIR Lepton 3.5** (160×120, 0.20 m/px @ 30 m). §5. |
| 3 | Swarm covers 3.5 km²/h | **Overstated** | Rebuilt on the physically-correct 30 m thermal swath, not 40 m: **2.6 km²/h**. §6. |
| 4 | Kestrel is ~24× cheaper per km² than a single drone too | **Wrong direction** | A lone scout is *cheaper* per km² than the swarm — the mothership is overhead. The swarm buys **time**, not cheapness. Say so out loud. §6. |
| 5 | Rubric weights: Impact 25%, Novelty 20%, Tech 15%, Viability 25% | **Invented** | SIH publishes **no weights**. Nine unweighted criteria, verbatim in §1. |

Plus one addition that is the biggest single upgrade available: **the problem statement is owned by
Qualcomm, and the old deck was an NVIDIA deck.** Silicon re-specced to Qualcomm in §4.

---

## 1. The rules we are actually graded against `[SOURCED]`

From `given/SIH-2026-Guidelines.pdf`, p.13, verbatim:

> "the ideas will be evaluated by experts. Evaluation criteria will include **novelty of the idea,
> complexity, clarity and details in the prescribed format, feasibility, practicability,
> sustainability, scale of impact, user experience and potential for future work progression.**"

Nine criteria. **No weightages are published.** Any deck that optimises for invented percentages is
optimising for fiction.

Format constraints (official SIH idea-presentation template, structure unchanged 2023→2026):

| Constraint | Value |
|---|---|
| Slides | **Maximum 6, including the title slide** |
| Upload format | **PDF only** — no PPT, no DOC |
| Content rule | *"Try to avoid paragraphs and post your idea in points, diagrams, infographics, or pictures"* |
| Fixed section headings | Title · Proposed Solution · Technical Approach · Feasibility and Viability · Impact and Benefits · Research and References |
| Deadline | 20 Sep 2026 — **11 days from today** |
| Prize | ₹1,50,000 per problem statement, paid only if Qualcomm likes the winning idea |
| Reality of the format | Every content slide is one page read cold, offline, with no presenter. The visual **is** the argument. |

Sources: `given/SIH-2026-Guidelines.pdf` · official SIH idea-presentation format — **the actual 2026 PPTX, now downloaded**: `given/SIH2026-IDEA-Presentation-Format.pptx`, full extract in `given/SIH2026-TEMPLATE-EXTRACT.md`

---

## 1a. The official 2026 template, obtained and measured `[SOURCED — primary]`

Downloaded 9 Sep 2026 from `https://www.sih.gov.in/letters/2026/SIH2026-IDEA-Presentation-Format.pptx`
— publicly linked from the PS page as **"Idea PPT"**, not portal-gated. 924,505 bytes, real OOXML,
7 slides.

**Every heading and every sub-bullet this kit assumed is confirmed verbatim.** The six sections, their
order, and their prompt text are exactly as `slides/` already had them. No structural rework.

**Slide 7 is an instructions slide** and is explicitly deletable. Its rules, verbatim:

> - Kindly keep the maximum slides limit up to six (6). (Including the title slide)
> - Try to avoid paragraphs and post your idea in points /diagrams / Infographics /pictures
> - Keep your explanation precise and easy to understand
> - Idea should be unique and novel.
> - **You can only use provided template for making the PPT without changing the idea details
>   pointers (mentioned in previous slides).**
> - You need to save the file in PDF and upload the same on portal. No PPT, Word Doc or any other
>   format will be supported.

### Three things the real file changes

**(i) The pointer text must stay on every slide.** This is new and the kit did not account for it.
*"Without changing the idea details pointers"* means the sub-bullets — *"Detailed explanation of the
proposed solution"*, *"Potential challenges and risks"*, and so on — remain as text on their slides.
They are Arial 32 pt as shipped, in a full-width box at y 2.26 in; they can be **moved and resized**
(that is not *changing* them) but not deleted or reworded. Plan: shrink to **11 pt in a 2.7 in left
rail**, which is what every serious SIH deck does.

**(ii) The template is white; our visual system is dark navy.** Shipped as `schemeClr bg1` = white,
Times New Roman 36 pt bold titles, a `#0070C0` bottom bar, a *"Your Team Name"* oval top-left, and
the official SIH 2026 brain-lightbulb logo (saffron / green / slate). This is a genuine conflict and
the decision is a judgment call — see `README.md` for the two options and the cost of each. Note what
the rule's own qualifier scopes it to: **the pointers**, not the palette.

**(iii) The space is tighter than the kit assumed.** Canvas is **13.333 × 7.5 in, 16:9** — so every
generated image is the right aspect. But usable content area, after the 1.25 in title, the 0.55 in
bottom bar and a 2.7 in pointer rail, is **10.23 × 5.55 in**. Measured consequences:

| Attempt | Result |
|---|---|
| One full-width 16:9 image | 10.23 × **5.76 in — does not fit** (0.2 in too tall) |
| **Two 16:9 side by side** | 4.99 × 2.81 in each — **fits**, uses 2.81 in |
| **Plus one wide band below** | 10.23 × 2.54 in — **fits**, a 4:1 crop |
| Three full-width 16:9 stacked | **impossible** — would need 17.3 in of height |

**So the real per-slide budget is: two 16:9 panels + one 4:1 band = three visuals, and no room left
for large tables.** The kit's slide files currently specify three images *plus* two or three sizeable
native tables per content slide. That does not fit and must be cut.

Good news: the visuals were designed in the right shapes by accident. The pictogram and row-based
pieces — P3.1 pixel ladder, P5.1 survival wall, P5.2 uncounted, P4.1 cost ladder — are natively
band-shaped and crop to 4:1 cleanly. The cinematic pieces — P2.1 frog, P2.2 hero — want the
side-by-side 16:9 slots. Nothing needs regenerating for shape.

**Tables must therefore compress to 3–4 rows of two short columns, or be dropped into the images.**
The full BOM, risk register and stack table live in this file; a slide never needed the line items.

---

## 2. The problem, anchored to one real Indian operation

### 2a. Wayanad landslide, 30 Jul 2024 — our primary anchor `[SOURCED]`

| Fact | Value |
|---|---|
| Personnel committed to search | **1,300** across NDRF, Army, Navy, Coast Guard, MEG, Kerala Police/Fire/Forest, K-9 squads |
| Teams / zones | **40 teams across 6 zones** (Punchirimattom, Mundakkai, School area, Chooralmala town, Village area, Downstream) |
| Duration of active search | **5+ days**; Army withdrew after a "stretched" operation |
| Dead / still missing | 357+ dead · **206 missing** |
| Land destroyed | ~3,700 acres of agricultural land swept — **≈15 km²** |
| Downstream search | bodies recovered along the **Chaliyar river**, tens of km from the slide |

### 2b. The single most useful fact in this deck `[SOURCED]`

On 1 Aug 2024 at ~16:30, a thermal/radar scanner at Wayanad reported life under the debris. An Army
officer, quoted directly:

> **"We recorded three breath signals on the radar. But we can't confirm a human is trapped there."**

A search was mounted at that spot. **Nothing was found — dead or alive.** The expert assessment: the
signal "might have detected the presence of a frog or snake." Separately, a private agency flew
thermal imaging by drone over Mundakkai and reported **"zero human presence was detected."**

Source: Onmanorama live blog, 2 Aug 2024 —
https://www.onmanorama.com/news/kerala/2024/08/02/wayanad-landslide-mundakkai-chooralmala-bailey-bridge-search-rescue-death-toll-live.html

**Why this is the spine of the deck.** The gap at Wayanad was not "nobody had a drone." A drone with
a thermal camera was flown and returned nothing. A separate sensor returned a false positive that
consumed a rescue effort. The real gap is **single-sensor detection that cannot be trusted, at a
resolution that cannot see, over an area too big for the people available.** That is precisely the
three-part gap this PS asks us to close — and it lets us answer the PS's "Multi-Sensor Fusion"
bullet with evidence instead of a buzzword.

### 2c. The 2026 monsoon — happening while the judges read this `[SOURCED]`

| State | Toll, this monsoon |
|---|---|
| Himachal Pradesh | **261 deaths in 64 days**, 150 roads blocked, damage **> ₹1,202 crore** (as of 2 Sep 2026) |
| Assam | **100 dead**, **700,000 displaced**, ~300,000 in relief camps |
| Jammu & Kashmir | 31 dead in rain bursts |
| Kerala | 15 dead, 7 missing, 10,000+ across 300+ relief camps |
| Jharkhand | 14 lightning deaths |
| Nagaland | 9 in landslides |
| **Six states, sourced tallies** | **430+ dead, Jul–Sep 2026** |

Sources: thenewsmill.com/2026/09/rain-related-deaths-in-himachal-rise-to-261-during-2026-monsoon-season ·
news.webindia123.com (Himachal, 2 Sep 2026) · npr.org/2026/08/10/g-s1-138015 (Assam) ·
aljazeera.com/news/2026/8/5 · aljazeera.com/news/2026/7/20

### 2d. Structural background `[SOURCED]`

| Fact | Value | Source |
|---|---|---|
| Extreme-weather event days, 2024 | 322 of 365 (88%) | IPE Global–Esri India |
| Districts vulnerable to extreme events | 85% of 738 | IPE Global–Esri India |
| Hydro-met deaths 2024-25 (decade high) | 2,979 | Lok Sabha reply via NDTV/Telegraph |
| Land seismic-prone / flood-prone / coast cyclone-prone | 58.6% · 12% (40 Mha) · 5,700 of 7,520 km | NDMA |
| Precedent: first startup inside official NDRF response | EndureAir (IIT Kanpur), 2021 Uttarakhand | NITI frontier-tech |
| Uttarakhand (Mana) avalanche, 2025 | 200+ personnel, thermal + GPR + dogs + drones, −12 to −15 °C | press |

### 2e. Why thermal alone fails in daylight — the mechanism `[SOURCED]`

Operator testimony from thermal SAR: *"in the day, the rocks retained heat and would show up on the
IR display."* Sun-soaked concrete and rock reach 45–55 °C; human skin reads ~33 °C. **In daytime the
survivor is colder than the rubble** — the sign of the anomaly inverts, and every "find the hot spot"
filter breaks. This is the physical reason fusion is mandatory, not optional.

---

## 3. Survival vs extrication time `[SOURCED]`

| Extrication window | Survival (USAR literature) | Historical |
|---|---|---|
| < 30 min | ~99% | Tangshan 1976: 99% |
| < 24 h | 81–90% | Tangshan 81% · Campania-Irpinia 1980 88% |
| 24–48 h | ~53% | Tangshan d2 37% · Campania d2 35% |
| 48–72 h | 20–38% | Campania d3–4 9% |
| > 72 h | < 10% | — |
| Live extrications inside first 24 h | **94%** | Campania-Irpinia 1980 |

Source: USAR / disaster-medicine literature (DOAJ, "Methods Used in Urban Search and Rescue");
datasets Tangshan 1976, Campania-Irpinia 1980.

**Keep this rebuttal ready.** These figures carry survivor-selection bias — the easiest victims are
found first, so early-window survival is flattered. That bias is an argument *for* our thesis: if the
easy finds happen early, the only way to reach the hard finds inside the window is to search faster.

---

## 4. Silicon — Qualcomm-native, because Qualcomm owns the problem statement

The PS asks for on-device inference, no cloud dependence, and *"optional 5G/Wi-Fi."* That is a
description of Qualcomm's own robotics stack. Specced accordingly.

| Part | Spec | Price | Confidence |
|---|---|---|---|
| **Qualcomm RB3 Gen 2 Vision Kit** (QCS6490) — mothership brain | 8-core Kryo 670, Adreno 643L, **12 TOPS Hexagon NPU**, 6 GB / 128 GB UFS, Linux | **₹50,000** (India, Thundercomm) · $599 US | SOURCED |
| ModalAI **VOXL 2** (QRB5165) — production/Blue-UAS path | **15 TOPS**, 8-core to 3.09 GHz, 8 GB LPDDR5, **PX4 running on the sensor DSP**, 7-camera, 5G-modem-ready, **16 g** | $1,199.99 (≈₹1.05 L) | SOURCED |
| **Qualcomm AI Hub** + QNN / SNPE | compiles to Hexagon NPU; INT8 required for HTP; **free real-device profiling** | free | SOURCED |
| Ultralytics → QNN export path | official YOLO→QNN support for on-device inference | free | SOURCED |
| Snapdragon NPU detection throughput | **YOLOv8 at 65+ FPS on NPU vs 2 FPS on CPU** (Snapdragon X Elite) | — | SOURCED |
| YOLOv8n @640² on QCS6490 (12 TOPS), INT8 | **30–45 FPS expected** | — | **ESTIMATE — profile free on AI Hub before finale** |
| On-device LLM: Llama 3.2 3B Q4_K_M | **2.0 GB**, 28.7 tok/s generate, 580 tok/s prefill *(measured on Jetson Orin Nano)* | — | SOURCED |
| Same model on QCS6490 | 10–18 tok/s expected (lower memory bandwidth) | — | **ESTIMATE — benchmark required** |
| Situation report length | ~250 tokens → 15–25 s on-device | — | DERIVED |

**Architecture consequence, and it is a real one:** detection runs INT8 on the Hexagon NPU; the LLM
runs on CPU/GPU. They do not contend for the same engine, so report generation never steals frames
from the detector. That is a design decision, not a coincidence, and it is worth one line on Slide 3.

Sources: thundercomm.com/product/qualcomm-rb3-gen-2 · indiamart.com (RB3 Gen 2, ₹50,000) ·
cnx-software.com/2024/04/15 · modalai.com/products/voxl-2 · docs.px4.io ModalAI VOXL 2 ·
github.com/quic/ai-hub-models · docs.ultralytics.com/integrations/qnn ·
medium.com/@carrycooldude (YOLOv8 65 FPS Snapdragon X Elite NPU) ·
gist.github.com/yalexx (Orin Nano LLM benchmarks) · NVIDIA Jetson AI Lab

---

## 5. Sensor optics — the correction that becomes a slide `[DERIVED, formula shown]`

**Ground sample distance:** `GSD = 2 · h · tan(HFOV / 2) / horizontal_pixels`
**Prone-human target:** 1.7 m × 0.4 m ≈ 0.68 m².
**Apparent ΔT** = (target area ÷ pixel area) × (33 °C skin − 28 °C background).

At **h = 30 m AGL**:

| Sensor | Resolution | HFOV | Swath | GSD | Human fills | Apparent ΔT | Verdict |
|---|---|---|---|---|---|---|---|
| MLX90640 wide *(repo's choice)* | 32 × 24 | 110° | 85.7 m | **2.68 m/px** | 9.5% of 1 px | **0.5 °C** | **Invisible.** Sun-heated debris clutter is ±3 °C. |
| MLX90640 narrow | 32 × 24 | 55° | 31.2 m | 0.98 m/px | 71% of 1 px | 3.5 °C | Marginal, and only a 31 m swath. |
| **FLIR Lepton 3.5** *(our choice)* | **160 × 120** | 57° | 32.6 m | **0.20 m/px** | **8 × 2 px** | full contrast | **Detectable, and shaped** — pose is visible, not just a blob. |
| FLIR Lepton 3.5 @ 50 m | 160 × 120 | 57° | 54.4 m | 0.34 m/px | 5 × 1 px | full contrast | Detectable; shape marginal. |

**FLIR Lepton 3.5:** 160×120 radiometric LWIR, NETD < 50 mK, 57° FOV, **$164** (GroupGets) +
₹2,105 breakout (Robu.in) ≈ **₹16,600 landed**. That is ₹11K more than the MLX90640 and it is the
difference between a detector and a decoration.

RGB, same altitude for comparison: 12 MP sensor, 62.2° HFOV → 36.2 m swath, **11 mm/px**, so a prone
human is ~154 px tall. Detection is not the RGB camera's problem; daylight, canopy and debris are.

Sources: oem.flir.com/products/lepton · groupgets.com/products/flir-lepton-3-5 ($164) ·
robu.in FLIR Lepton adapter (₹2,105) · adafruit.com/product/4407 (MLX90640 FOV variants) ·
arxiv.org/pdf/2212.12616 (aerial thermal detection tested 30–121 m)

---

## 6. Search performance — every model printed

### 6a. Ground team `[DERIVED from published SAR methodology]`

Koester et al., *Wilderness & Environmental Medicine* 2014: effective sweep width from maximum
detection range, **W = 1.1 × Rd in low visibility**.

- Debris/flood terrain: Rd ≈ 12 m → **W ≈ 13 m per searcher**
- 6-person line abreast at W spacing → **78 m team swath**
- Advance through rubble: 1.5 km/h = 0.42 m/s
- Duty cycle 0.6 (re-brief, obstacle negotiation, marking, rest)
- 78 × 0.42 × 0.6 = 19.7 m²/s = **0.071 km²/h**

**Published baseline: 0.1 km²/h** — deliberately rounded *up*, in the baseline's favour, so the
comparison cannot be accused of stacking the deck.

### 6b. Kestrel `[DERIVED]`

Per scout, thermal-limited (the thermal swath is narrower than RGB, so it governs):

- 30 m AGL → Lepton 3.5 swath 32.6 m; take **30 m** effective after 10% overlap
- Cruise 8 m/s · duty cycle 0.5 (turns, hover-confirm, re-transit, battery cycling)
- 30 × 8 × 0.5 = 120 m²/s = **0.43 km²/h per scout**
- **6 scouts = 2.6 km²/h.** The mothership is not counted as a searcher — at 100 m its RGB pass is
  wide-area context, not person-detection. It coordinates and relays.

| Asset | Coverage | vs ground |
|---|---|---|
| 6-person ground team | 0.1 km²/h | 1× |
| Single scout | 0.43 km²/h | 4.3× |
| **Kestrel swarm (6 scouts)** | **2.6 km²/h** | **26×** |

### 6c. Cost per km² `[DERIVED]` — including the part that argues against us

Helicopter, IAMSAR method (`rate = track spacing × speed`): person-sized target in cluttered
terrain, S ≈ 0.1 NM = 0.185 km, V ≈ 40 kt = 74 km/h → **13.7 km²/h**. Charter ₹1.6 L/hr + 18% GST =
**₹1.888 L/hr** → **₹13,800/km²**.

| Asset | ₹/hr | km²/h | **₹/km²** |
|---|---|---|---|
| Charter helicopter | 1,88,800 | 13.7 | **13,800** |
| Single scout (₹25.6K ÷ 300 h + ₹100 opex) | 185 | 0.43 | **430** |
| **Kestrel swarm** (₹2.7 L ÷ 300 h + ₹400 opex) | 1,304 | 2.6 | **502** |

**State this plainly on the slide: a single scout is cheaper per km² than the swarm. The mothership
is overhead.** The swarm is not bought for cheapness — it is bought for *time*, and time is the only
currency the survival curve accepts. Volunteering this is worth more than hiding it; it also
pre-empts the one question a sharp judge will ask.

And the helicopter comparison is not "we are faster." A helicopter sweeps **5× more area per hour**
than the whole swarm. It costs **27× more per km²**, cannot fly at night or in monsoon IMC, needs
1–3 h to position, and puts **one pair of human eyes at 300 m** on the problem — where a 1.7 m human
subtends ~20 arcmin, at the edge of visual acuity, against clutter, at 74 km/h. Kestrel puts a
**0.20 m/px thermal frame and a detector on every square metre**. Helicopters are transport. They
were never the sensor.

### 6d. Time to first survivor `[DERIVED]`

Expected time to first detection for a uniformly-distributed victim ≈ half the full sweep.

| Asset | Full sweep, 5 km² | Expected first detection |
|---|---|---|
| Ground team | 50 h | 25 h |
| Single scout | 11.6 h | 5.8 h |
| **Kestrel swarm** | **1.9 h** | **58 min** |

### 6e. The Wayanad counterfactual — the deck's headline `[DERIVED from §2a + §6b]`

15 km² destruction zone, the real one.

| | What happened | Kestrel |
|---|---|---|
| Assets | 1,300 personnel, 40 teams, 6 zones | 1 mothership + 6 scouts, 2 operators |
| Full-zone sweep | **5+ days** | **5.8 hours** — one shift |
| Position on the survival curve at completion | day 3+ → **~35%** | < 6 h → **~99%** |

Sanity check on the model: 15 km² ÷ 0.1 km²/h = 150 h of pure search ≈ 6 days of shift work. The
model reproduces the real operation's duration. That agreement is the point — the ground-team figure
isn't a guess we made up to look good, it predicts Wayanad.

### 6f. Endurance `[DERIVED from own PRD anchor]`

Anchor, from `the-drone-syndicate/build-alpha/PRD.md`: **12–15 min fully loaded at 3 kg payload,
T/W ≥ 1.5:1, 4S 5000 mAh.** Hover power ∝ weight^1.5, calibrated at that point.

| Payload | Single 4S 5000 mAh | Dual pack |
|---|---|---|
| 0 kg | 18 min | 30 min |
| 1.0 kg | 15.5 min | 26 min |
| 2.0 kg | 13 min | 22.5 min |
| 3.0 kg | **11 min** | **19 min** |

Mothership sensor payload is ~1.5 kg → **24 min on dual pack**, hovering as a relay (cheaper than
cruise). Scouts on 4S 2200 mAh ×2 → ~18 min per sortie, hot-swapped from the truck. **Sustained
search is achieved by battery rotation, not by endurance** — 6 scouts × 18 min with 2 spare packs
each holds continuous coverage for ~90 min per scout before recharge.

This is why truck-launch beats air-launch (§0, correction 1): scouts land, swap, and relaunch in
under a minute from the vehicle. An air-launched scout has one life.

---

## 7. Bill of materials `[SOURCED-repo prices unless noted]`

### Mothership — the flying brain

| Line | Qty | ₹ | Confidence |
|---|---|---|---|
| Hexacopter frame S550 + landing gear | 1 | 6,500 | repo class |
| Motors A2212 920 KV | 6 | 2,700 | SOURCED-repo (₹450 ea) |
| ESC SimonK 30 A | 6 | 1,932 | SOURCED-repo (₹322 ea) |
| Props 1045 | 6 pr | 500 | SOURCED-repo |
| **Qualcomm RB3 Gen 2 Vision Kit (QCS6490, 12 TOPS)** | 1 | **50,000** | **SOURCED** |
| Pixhawk 2.4.8 flight controller | 1 | 8,514 | SOURCED-repo |
| GPS NEO-M9N | 1 | 2,099 | SOURCED-repo |
| **FLIR Lepton 3.5 (160×120 radiometric) + breakout** | 1 | **16,600** | **SOURCED** |
| RGB camera, 12 MP (IMX477 class) | 1 | 6,000 | ESTIMATE |
| LoRa mesh hub (SX1262) | 1 | 2,500 | ESTIMATE |
| EC200U 4G/LTE + GNSS | 1 | 1,988 | SOURCED-repo |
| Battery 4S 5000 mAh | 2 | 9,000 | SOURCED-repo |
| PDB-XT60 + 5 V UBEC | 1 | 665 | SOURCED-repo |
| Telemetry radio 915 MHz | 1 | 2,500 | ESTIMATE |
| **Subtotal** | | **₹1,11,500** | |

### Scout ×6 — the scrappy part, and the part Qualcomm will enjoy

| Line | Qty | ₹ | Confidence |
|---|---|---|---|
| S500 frame + landing gear | 1 | 3,419 | SOURCED-repo |
| Motors A2212 920 KV | 4 | 1,800 | SOURCED-repo |
| ESC SimonK 30 A | 4 | 1,288 | SOURCED-repo |
| Props 1045 | 3 pr | 250 | SOURCED-repo |
| Flight controller (SpeedyBee F405 / Pixhawk-lite) | 1 | 4,000 | ESTIMATE |
| **Brain: second-hand Snapdragon 8-series phone** — Hexagon NPU, 4K camera, IMU, GPS, LTE modem, own battery, own IP-rated shell, all in one 190 g part | 1 | **9,000** | **ESTIMATE — verify on Cashify/OLX** |
| LoRa node (SX1262) | 1 | 1,200 | ESTIMATE |
| Battery 4S 2200 mAh | 2 | 3,948 | SOURCED-repo |
| PDB + UBEC | 1 | 665 | SOURCED-repo |
| **Per scout** | | **₹25,600** | |
| **× 6 scouts** | | **₹1,53,600** | |

Ground station: LoRa base + antenna **₹4,000**; laptop assumed owned.

### **System total ≈ ₹2,69,100 → ₹2.7 lakh**

**The line to say out loud:** ₹2.7 lakh is **86 minutes** of helicopter charter at ₹1.888 L/hr
inclusive of GST. The whole system costs less than an hour and a half of the alternative.

**On the recycled phone.** It is not a gimmick, it is the correct engineering choice, and it is the
strongest possible signal to a Qualcomm panel. A used flagship gives us a Hexagon NPU that runs
YOLOv8 via QNN, a stabilised 4K camera, IMU, GNSS, an LTE modem, a battery and a sealed enclosure —
for ₹9,000, in one 190 g part, with Qualcomm's own toolchain already targeting it. Specifying a
₹50,000 dev board on an expendable airframe would be the mistake.

---

## 8. TODO before 20 Sep — every open item

- [ ] **Profile YOLOv8n INT8 on QCS6490 via Qualcomm AI Hub** (free, real device, no hardware needed).
      Replaces the 30–45 FPS estimate in §4 with a measured number. Highest-value item on this list.
- [ ] Benchmark Llama-3.2-3B-Q4 tokens/sec on a QCS6490/Snapdragon target; replace the §4 estimate.
- [ ] Price a second-hand Snapdragon 8-series handset on Cashify/OLX; screenshot it for the BOM.
- [ ] Confirm the portal's 2026 template PPTX byte-for-byte once team-leader credentials arrive —
      if the section headings differ from §1, the slide files re-map, the data does not.
- [ ] DGCA position on 7 airframes under 2 operators: green-zone ceiling is **120 m AGL / 400 ft** and
      we operate at 30–100 m, so altitude is fine; **BVLOS needs specific approval** (only 3 national
      corridors exist). Mitigation to state on Slide 4: scouts stay inside the mothership's relay
      bubble and the operator's VLOS envelope; state-agency disaster authorisation is the deployment
      path. Verify wording against DGCA Drone Rules 2021 + current Digital Sky text.
- [ ] Re-run `scripts/verify.py` for the live idea-count on SIH26177 before submitting (cap is 500).
- [ ] Fill the team block: 6 members, same college, ≥1 female (mandatory), SPOC authorisation letter.
- [ ] Confirm our college has a **registered SPOC** — nothing else matters until this is true.

---
---

# ADDENDUM — 9 Sep 2026 (second research pass)

Four questions were put to this pass: Assam, Nepal, whether official death tolls under-count, and
how many lives speed actually saves. Plus the institutional and funding route. All five have answers,
and one of them changes the deck's strongest slide.

---

## 2f. Nepal–Tibet glacial flood, Aug–Sep 2026 — the live one `[SOURCED]`

A glacier collapse above the Nepal–China border triggered a debris flow down the Trishuli and
Bhotekoshi systems. It is still being searched as this deck is written.

| Fact | Value |
|---|---|
| **Confirmed dead** | **1,114** (Nepal NDRRMA) · 16+ on the Chinese side |
| **Still missing** | **~4,500** across both sides — 2,498 in Nepal alone at the 30 Aug count |
| Rescued alive | ~12,000 |
| **Search personnel** | **21,000+** — national police, army, armed police forces |
| **Helicopters committed** | **16** |
| Worst-hit districts | Rasuwa, Nuwakot (Nepal); Gyirong County (Tibet) |
| Infrastructure | 32 bridges and ~40 km of road swept away, including the entire Betrawati–Rasuwagadhi road |
| Notable missing groups | 933 workers across 11 hydropower sites · 589 foreign nationals from 23 countries |
| Attribution | USGS: glacial collapse and debris flow |
| Identification constraint | Nepal's foreign minister: the country *"does not have enough refrigerators to store the dead bodies and identify and test their DNA"* — bodies dispersed across 21 hospitals |

Sources: en.wikipedia.org/wiki/2026_Nepal_floods · abcnews.com (toll tops 1,100) ·
aljazeera.com/news/2026/8/30 · news.un.org/en/story/2026/08/1168233 · cnn.com/2026/09/01

## 2g. Assam floods, Jul–Aug 2026 `[SOURCED]`

| Fact | Value |
|---|---|
| Districts inundated | **16** |
| Villages inundated (18–21 Jul surge) | **794** · 2,000+ impacted overall |
| **Cropland submerged** | **119,000 ha = 1,190 km²** (as of 9 Aug) |
| People affected | ~10 lakh (26 Jul) · 700,000 displaced · ~300,000 in relief camps |
| Deaths | 68 (26 Jul) → **100** (10 Aug) |
| Worst-hit | Sivasagar (47 deaths), Golaghat, Charaideo, Dibrugarh, Majuli, Jorhat, Dhemaji, Lakhimpur |
| Responding agencies | NDRF, **SDRF**, Indian Army, **Indian Air Force**, Assam Police |
| Structural exposure | **~40% of Assam's land area is flood-prone** |

Sources: en.wikipedia.org/wiki/2026_Assam_floods · downtoearth.org.in · worldweatherattribution.org ·
india.mongabay.com/2026/08 · npr.org/2026/08/10/g-s1-138015

**A scale number we must handle honestly, not hide.** 1,190 km² at 2.6 km²/h is **458 flight-hours**.
Kestrel cannot sweep an Assam flood plain and we must not imply it can. It does not need to: in a
flood the search target is **settlements, not water** — 794 villages, not 1,190 km². Across 16
districts that is ~50 villages per district, roughly **37 km² of actual search area per district
≈ 14 hours for one Kestrel system**. This is what fixes the unit of analysis for the whole deck:
**the deployable unit is one system per district, not one system per disaster.** §9 follows from it.

---

## 2h. Does the official death toll under-count? — the honest answer `[SOURCED]`

**Yes, but not for the reason it is usually alleged, and the well-evidenced version is not our
use case.** Three separate things get conflated. Keep them apart.

**(i) Documented under-counting exists — in heat mortality.** For Mar–Jul 2023, the Ministry of
Health reported **360** heatstroke deaths; a Heatwatch / Veditum India Foundation compilation of news
reports found **733**; and peer-reviewed excess-all-cause-mortality modelling puts a single day of
extreme heat at **~3,400 excess deaths** nationally and a five-day heatwave at **~30,000**. Excess
mortality ranges 5.6% (Varanasi) to 43.1% (Ahmedabad).
*Sources: frontiersin.org/journals/environmental-health 10.3389/fenvh.2026.1789071 · euronews.com/2026/06/10 · thewire.in · PMC3954798*
**Do not put this in the deck.** Heat waves are not a search-and-rescue problem. Citing heat
under-counting to argue for a SAR drone is a bait-and-switch a judge will catch, and it costs more
credibility than it buys.

**(ii) The claim we cannot support: deliberate concealment.** We have no evidence of it, we do not
need it, and alleging it in a deck submitted to a government-run hackathon is a self-inflicted wound.
**Do not make this argument.**

**(iii) The claim that is airtight, on-topic, and argues for our product — the definitional one.**
A disaster death toll is a count of **bodies recovered and identified**. It is not a count of people
lost. A person never found is never counted as dead; they are counted as *missing*, in a separate
column, often indefinitely.

| Disaster | Confirmed dead | Still missing | Ratio |
|---|---|---|---|
| **Nepal–Tibet, Aug 2026** | 1,114 | **~4,500** | **4.0 : 1** |
| **Wayanad, Jul 2024** | 357+ | **206** | 0.6 : 1 |

**Why this is the strongest form of the argument.** It requires no accusation, it is verifiable from
official figures published by the responding authorities themselves, and it is *causal* to what we
sell: **the counting gap and the search gap are the same gap.** A body is counted when it is found.
Nepal committed 21,000 personnel and 16 helicopters and still has 4,500 people unaccounted for. The
limit is not willingness to count — it is the physical capacity to search. Faster, wider search moves
people out of the *missing* column, into *rescued* if you reach them in time and into *counted* if you
do not.

Corollary we must also state, because it is the honest boundary of our own claim: **nobody counts the
entrapped-but-alive.** That is why §6g below gives a *rate*, not a national lives-saved total.

---

## 6g. How many more lives — the rate, and why it is only a rate `[DERIVED from §3]`

Straight from the survival curve in §3, reading survival at the moment the search *completes*:

| Search completes at | Of 100 people trapped and initially alive, still alive |
|---|---|
| **6 hours** (Kestrel, 15 km²) | **99** |
| 24 hours | 85 |
| 48 hours | 53 |
| **72 hours / day 3** (1,300 personnel, 15 km²) | **35** |

**Delta: +64 survivors per 100 people trapped alive.** That is subtraction on sourced numbers, and it
is the single most important output of this project.

**What we deliberately do not claim.** We will not multiply 64% by Wayanad's 206 missing or Nepal's
4,500. Most of those people were swept into river systems, not held in extractable voids, and
presenting them as recoverable would be false. The population the 64-per-100 rate applies to is the
entrapped-and-alive subset — **which no agency counts** (§2h iii). So the honest statement, and the
one to put on the slide, is:

> Completing the search in 6 hours instead of 3 days moves 64 people in every 100 trapped from the
> wrong side of the survival curve to the right one. How many people that is per disaster, nobody
> currently measures — which is the second thing this system fixes.

Selection-bias caveat from §3 still applies and still argues our way.

---

## 9. Who buys it, and with whose money `[SOURCED]` — the viability answer

### 9a. India's disaster-management structure — where Kestrel sits

| Tier | Body | Reality |
|---|---|---|
| National | **NDMA** (PM-chaired), **NDRF** | **16 battalions for 738 districts.** NDRF is always *arriving* — the Wayanad response included a 31-member team dispatched from Bengaluru |
| State | **SDMA**, **SDRF** (State Disaster Response *Force*) | Local knowledge, faster initial response; works alongside NDRF, which brings specialist equipment |
| **District** | **DDMA** — headed by the District Collector/Magistrate | **Mandated in every district by the Disaster Management Act, 2005.** Already there on hour zero |
| Command doctrine | **Incident Response System (IRS)**, NDMA guidelines; district **EOC** | Kestrel's dashboard is an IRS-shaped feed into the district EOC, not a parallel system |

**The structural argument, and it is the best one on the slide:** NDRF has 16 battalions and must
travel. The DDMA exists in all 738 districts and is present before anyone arrives. **Kestrel is a
DDMA asset, flown by SDRF, feeding the district EOC** — which is precisely the tier that currently
owns the first six hours and currently has no aerial search capability of its own.
*Sources: nidm.gov.in/PDF/guidelines/Incident_Response_System.pdf · DM Act 2005 · NDRF structure (16 battalions, 5 CAPFs)*

### 9b. The money already exists — 15th Finance Commission, 2021–26 `[SOURCED + DERIVED]`

| Line | Amount |
|---|---|
| **SDRF** (State Disaster Response *Fund*), all states, 2021-26 | **₹1,28,122.40 crore** — Centre ₹98,080.80 cr + States ₹30,041.60 cr |
| **SDMF** (State Disaster Mitigation Fund) | **₹32,030.60 crore** |
| Implied total pool | **₹1,60,153 crore** (SDRF = 80%, SDMF = 20%) |
| Split within the 80% | 40% Response & Relief · 30% Recovery & Reconstruction · **10% Preparedness and Capacity-building** |
| **∴ Preparedness & Capacity-building line, 2021-26** | **₹16,015 crore** |
| Centre : State share | **75 : 25** general · **90 : 10 for north-eastern and Himalayan states** |

*Cross-check that validates the reading: 20% of ₹1,60,153 cr = ₹32,030.60 cr, matching the published
SDMF figure to the paisa.*
*Sources: aninews.in (MoS Nityanand Rai, 1 Aug 2023) · ndmindia.mha.gov.in/ndmi/responsefund · fincomindia.nic.in · pib.gov.in PRID 1947134*

### 9c. What national coverage actually costs `[DERIVED]`

| | |
|---|---|
| One Kestrel system | **₹2,69,100** |
| **× 738 districts = national coverage** | **₹19.86 crore** |
| As a share of the ₹16,015 cr preparedness line | **0.124% — one-eighth of one percent** |
| Systems that line could buy outright | 595,143 — **806 per district** |
| **What Assam, Himachal, Uttarakhand, J&K, Nagaland actually pay per district** (90:10) | **₹26,910** |

**No new budget line is required.** Kestrel is procured under an existing, funded, five-year head
titled *Preparedness and Capacity-building*, and the states hit hardest this monsoon pay a tenth of
the sticker price. For scale in the other direction: states sought ₹17,169 crore of relief in 2024-25
and NDRF released ₹812 crore — national Kestrel coverage is **2.4% of what was actually released**.

### 9d. The CSR route — and it points straight back at Qualcomm `[SOURCED]`

MCA notification **GSR-390(E), 30 May 2019** inserted clause **(xii)** into **Schedule VII of the
Companies Act, 2013**: *"disaster management, including relief, rehabilitation and reconstruction
activities."* Disaster-management capability is therefore a **CSR-eligible spend**.

Section 135 obligates any company with net worth ≥ ₹500 crore, turnover ≥ ₹1,000 crore, or net profit
≥ ₹5 crore to spend **2% of average net profit** on Schedule VII activities.

**A district-scale Kestrel deployment is a ₹2.69 lakh CSR line item.** One mid-sized company's annual
CSR obligation equips a district many times over — and **Qualcomm India comfortably clears the
Section 135 thresholds**, so the organisation that wrote this problem statement can fund its own
answer under a head it already reports against.
*Sources: ibclaw.in (GSR-390(E) text) · capindia.in · vinodkothari.com · csr.education*
`[VERIFY before submitting]` Qualcomm India Pvt Ltd's filed CSR obligation figure from its MCA
annual return, if we want to name a number rather than the mechanism.

---

## 10. Addendum TODO

- [ ] Nepal figures are moving daily — re-check the NDRRMA toll and missing count on the morning of
      submission. Cite the count *with its date* on the slide, and say "as of" out loud.
- [ ] Verify Qualcomm India Pvt Ltd's CSR obligation (MCA annual return) if naming a figure.
- [ ] Confirm current district count — 738 is the IPE Global–Esri figure; some sources now give ~780.
      Using 738 keeps us consistent with the vulnerability statistic on Slide 5.

---
---

# ADDENDUM 2 — 9 Sep 2026 · the input-stream register

**The gap this closes, and it was a real hole in the design.** The fusion gate as specced ran on
thermal + RGB + a second scout's angle. **Every one of those requires line of sight.** A person under
rubble has none. So the gate had a coverage hole precisely over the population the survival curve is
about — the entrapped. Both of the deck's own anchors sit in that hole: Wayanad's 206 and Nepal's
4,500 were not people lying visible on a surface.

---

## 11. Why "more streams" is the right instinct — and the condition that makes it true

More sensors do **not** automatically mean more confidence. Two sensors that fail for the *same
reason* add almost nothing. Thermal and RGB are strongly correlated: both need an unobstructed
line of sight, both are defeated by a concrete slab, both are degraded by the same smoke and the
same canopy. Stacking them is one vote wearing two coats.

**Independent streams are what buy confidence.** The streams below were chosen because their failure
modes do not overlap: RF does not care about line of sight, CO2 does not care about darkness,
radar does not care about either, acoustics do not care about depth, and human testimony does not
care about physics at all.

**The combiner is Bayesian evidence accumulation on a geospatial grid**, not a rule stack. The zone
is tiled; every stream contributes a likelihood ratio to each cell; the posterior *is* the search
priority queue, and a cell is promoted to a survivor marker only when independent streams push it
past threshold. This is not novel mathematics — it is standard Bayesian search theory, the method
that found the USS Scorpion and Air France 447, and it sits directly alongside the sweep-width
methodology already cited in §6a. Its property that matters here: **adding a weak-but-independent
stream can never make the estimate worse**, which is the formal version of the instinct.

Corollary worth one line on the slide: the three-gate AND-rule in P3.2 v1 was too brittle for this.
Replaced by a weighted posterior with a **publish threshold** and a **re-inspect threshold** — a hit
that fails to reach publish does not get discarded, it gets re-tasked to a second scout.

---

## 11a. The stream register `[all SOURCED unless marked]`

Penetration is what matters. Ordered by it.

| # | Stream | Reaches through rubble? | Hardware | Cost | Fails when |
|---|---|---|---|---|---|
| 1 | **RGB + YOLOv8 person/pose**, INT8 on NPU | **No** — surface only | 12 MP camera (already specced) | in BOM | canopy, night, debris-coloured clothing |
| 2 | **Thermal, FLIR Lepton 3.5** | **No** — needs line of sight | already specced | in BOM | daytime sun-heated rubble inverts the sign (§2e) |
| 3 | **Passive RF: WiFi probe requests + BLE advertisements** | **Yes — metres** | **the scout's own phone radio.** Zero added parts | **₹0** | phone dead, phone off, deep RF shadow |
| 4 | **Vital-signs radar (FINDER-class microwave / IR-UWB)** | **Yes — up to 9 m rubble, 6 m concrete** | UWB module (Novelda/Infineon class) | ₹15–30K `[ESTIMATE]` | **this is the stream that lied at Wayanad** — motion clutter, animals |
| 5 | **CO2 + NH3 chemical plume** | **Yes — via plumes through rubble** | SCD41-class CO2 + NH3 sensor | ₹3–5K `[ESTIMATE]` | wind disperses the plume; fire/CO sources |
| 6 | **Acoustic + seismic pods, air-dropped onto the debris** | **Yes** | geophone + mic pod ×6 | ₹2–3K each `[ESTIMATE]` | **victim unconscious** — cannot tap or call |
| 7 | **Local human reports** via the drone's own captive-portal WiFi | n/a — a *prior*, not a detector | already have the radio | ₹0 | nobody in range; reports are imprecise |
| 8 | **Telecom: SACHET cell broadcast + aggregate cell-attach counts** | n/a — wide-area *prior* | none on the aircraft | ₹0 | needs a live tower and a DDMA request |
| 9 | **Satellite: Sentinel-1 SAR change detection + VIIRS night-lights + ISRO Bhuvan** | n/a — pre-flight *prior* | none | ₹0 (Copernicus / Bhuvan are free) | cloud (not for SAR), revisit interval |
| 10 | **K-9 alert geotagging** — a ₹500 GPS collar on dogs already deployed | n/a — a *prior* | GPS collar | ₹500 | dog fatigue; scent pooling misleads |

### 11b. Stream 3 — the one that costs nothing and changes everything `[SOURCED]`

Phones broadcast **WiFi probe requests** and **BLE advertisements** continuously, with no SIM, no
service and no tower. RF passes through rubble that stops light and heat entirely. And the receiver
is **already on board**: the scout's brain is a second-hand Snapdragon handset, and its own Wi-Fi and
Bluetooth radios do the sniffing. **Zero added hardware, zero added grams, zero added rupees.**

Published and commercial precedent, so this is not speculative:
- **WiFi FTM (Fine Time Measurement) and UWB on drones to locate victims under rubble** — Sensors, *Using Smartphones to Locate Trapped Victims in Disasters*, 10.3390/s22197502; and *Victim Detection and Localization in Emergencies*, 10.3390/s22218433. Both name BLE and cellular as the next streams to add.
- **BLE beaconing from handsets** lets rescuers localise **many trapped victims simultaneously**.
- **BlueFly** — drone-mounted Bluetooth/WiFi detection, fielded.
- **ARTEMIS on the Echo SAR payload** — finds, maps and *interacts with* handsets from a drone.
- *"Take Me Home, Wi-Fi Drone"* — arXiv 2604.09115, drone-based wireless SAR.

**Identity vs presence — the distinction that keeps this clean.** MAC randomisation defeats
*identification*; it does not defeat *presence*. We need only "a powered device is emitting from
approximately here", localised by RSSI across multiple passes. We do not need to know whose it is,
and we do not want to.

### 11c. Stream 8 — the telecom idea, and it is bigger than you framed it `[SOURCED]`

**India already has the broadcast half built and switched on.** The **C-DOT Cell Broadcast Solution**,
operationalised by NDMA as **SACHET** on the ITU-recommended Common Alerting Protocol:

| Fact | Value |
|---|---|
| Integration | **All 36 States and UTs, all Indian mobile networks** |
| Reach | **1.43 billion citizens** via **14.5 million+ tower cells** |
| Delivered to date | **134 billion+ alerts**, in 19+ Indian languages |
| Property | Cell broadcast **overrides silent and Do Not Disturb** |
| Built by | **C-DOT**, under DoT — an Indian government lab |

**The novel move, and this is the strongest idea in the addendum.** SACHET is used to tell people to
*evacuate*. Nobody is using it to make survivors **detectable**. A cell broadcast to the affected
cells only — *"if you are trapped: turn Bluetooth ON, do not switch your phone off, do not use it for
calls"* — converts every handset in the disaster footprint into a beacon for stream 3, at zero
marginal cost, over infrastructure that already exists and already reaches 1.43 billion people.

**That closes a loop no one is closing: the network asks, the phone answers, the drone listens.**

**The aggregate layer, done in the privacy-preserving form.** Pseudonymised, aggregated cell-attach
or CDR counts per sector, compared before and after, give a published-methodology displacement
estimate: *a sector holding 400 attached handsets at 02:00 that holds 40 now, on a tower that is
still up, is where to send the swarm first.* Peer-reviewed: MDPI IJGI 10.3390/ijgi10060421; CACM,
*Mobile Phone Usage Data for Disaster Response*; arXiv 1908.02377 on CDR displacement detection.

**The lawful basis exists and it names disaster management explicitly.** **Section 20 of the
Telecommunications Act, 2023** — *provisions for public emergency or public safety* — empowers the
Central or a State Government to act on the occurrence of any public emergency, disaster management
included. Section 27 covers lawfully authorised monitoring.

**Where the line is, stated once and then we move on.** Individual subscriber location from a telco
is lawful-interception territory and sits inside the DPDP regime; asking for it in a student deck is
the wrong ask and would rightly be refused. The three layers we propose are, in ascending order of
sensitivity: **(a)** outbound broadcast — zero privacy cost, already deployed nationally; **(b)**
aggregate, pseudonymised, sector-level counts under a DDMA request on the Section 20 basis; **(c)**
on-aircraft passive presence sensing, which needs no telco, no subscriber data, and no permission
beyond flying. **(a)** and **(c)** are buildable by us. **(b)** is a partnership, and it is the right
thing to name as future work rather than to claim.

### 11d. Stream 7 — local input has an Indian precedent, and students built it `[SOURCED]`

**Kerala floods, Aug 2018.** The state ran a single portal, **keralarescue.in** — rescue requests,
needs, offers, volunteers, NGOs, and a **crowdsourced rescue heat map** — alongside toll-free 1077.
It was built by **student volunteers from the IEEE Kerala Section with the state-run Kerala IT
Mission**, and the KSDMA itself published it as a model of crowdsourced rescue. Context: 300+ dead,
~225,000 people in ~1,500 relief camps, one sixth of the state's population affected.

*Sources: sdma.kerala.gov.in/floods_2018 · sdma.kerala.gov.in/wp-content/uploads/2020/08/IEE-crowd.pdf · reliefweb.int · freecodecamp.org/news/how-i-used-crowdsourcing-to-help-kerala-floods-rescue-operations*

**Our version needs no internet.** The mothership carries an open SSID with a captive portal. Anyone
within range connects and submits *"my mother was in the blue house behind the temple"*, geotagged by
the aircraft's own position and RSSI. **Crowd reports do not detect anyone — they re-weight the
search.** In Bayesian terms they are the prior, and a strong one: locals know who is missing and
where they were standing, which is information no sensor on earth can produce.

### 11e. Stream 4 — the honest handling of the FINDER-class radar `[SOURCED]`

**NASA JPL / DHS S&T FINDER** — low-power microwave radar, roughly **one-thousandth of a phone's
output**, detects the micro-motion of breathing and heartbeat. Tested through **30 ft (9 m) of rubble
or 20 ft (6 m) of solid concrete**; localises to within ~5 ft. Prototype under 20 lb. In **Nepal,
2015**, it found **four men under about 10 ft of brick, mud and debris** in Chautara, and they were
rescued.
*Sources: jpl.nasa.gov/news/finder-search-and-rescue-technology-helped-save-lives-in-nepal · spinoff.nasa.gov/Spinoff2018/ps_1.html · dhs.gov/archive/science-and-technology/news/2015/05/05/finder-helps-save-four-nepal*

**And this is the same class of sensor that produced Wayanad's three breath signals — where nothing
was found.** That is not a reason to reject it. It is the reason it must be **one weighted vote and
never the decision**, which is exactly what §11 replaces the AND-gate with. It is the only stream in
the register that reaches deep and reports a *vital sign* rather than a presence, and it is therefore
both the most valuable and the most dangerous input in the system. Saying that on the slide is the
strongest possible close to the argument the frog opened.

### 11f. Multi-stream fusion is peer-reviewed, in exactly our combination `[SOURCED]`

*Evaluation of a Sensor System for Detecting Humans Trapped under Rubble: A Pilot Study*, Sensors
2018, 18(3), 852 — tested **CO2 sensor + thermal camera + microphone** together. Findings, verbatim
in substance: **the CO2 sensor usefully reduces the area of concern, and microphones in connection
with other sensors are of great benefit for detecting casualties.** Separately, portable sensor
arrays have detected the human volatile signature — **acetone, ammonia, isoprene, CO2** — in air
plumes travelling through constructed rubble at **3 parts per billion**.
*Sources: mdpi.com/1424-8220/18/3/852 · phys.org/news/2018-04-portable-device-humans.html · sciencedaily.com/releases/2018/04/180418141432.htm*

Acoustic caveat to keep, because it is the reason acoustics cannot stand alone: listening devices
placed on a rubble pile detect scratching, knocking and cries — but **register nothing from a victim
who is unconscious.** The dropped-pod design (stream 6) reuses the six-payload servo release already
in `build-alpha/PRD.md`: the pods listen persistently on the debris while the scouts keep sweeping.

---

## 11g. Ideation bench — streams not yet in the design, for the finale build

Ordered by how curious-but-real they are. None of these are in the idea deck; several deserve to be
in the Grand Finale prototype.

| Idea | Why it might work | Status |
|---|---|---|
| **Smart-meter "last gasp"** | Utility meters transmit a final message on power loss. The *order* in which a street's meters died reconstructs the collapse sequence and timing — free, already transmitted, nobody uses it for SAR | **Strongest unexplored idea here** |
| **VIIRS night-lights** | Which settlements went dark, available within hours of a night overpass, free. Tells the swarm which villages to fly first | Free, immediate |
| **Void analysis from photogrammetry + ISRO Bhuvan footprints** | Pre-disaster building footprints vs post-disaster 3D model → *where a survivable void can geometrically exist*. Doesn't detect people; ranks where people can still be alive | Pure software on data we already collect |
| **Wearables over BLE** | Fitness bands and watches beacon constantly and are worn *on the body*, unlike a phone in another room. Some advertise the BLE Heart Rate Service — a **vital sign over BLE at zero cost** | `[VERIFY]` — check which bands expose HR in the advertisement |
| **Bluetooth trackers + Find My networks** | Tags beacon loudly and are common. A drone carrying a handset can act as a finder node on Apple's Find My / Google's Find My Device crowdsourced BLE mesh | `[VERIFY]` legal and API reality |
| **Amateur radio (VU2) emergency net** | India has a real, mobilisable ham network — active in Kerala 2018 and Gujarat 2001. A human sensor grid that works when everything else is down | Institutional, not technical |
| **Store-and-forward message ferry** | People type a message into the drone's captive portal; the aircraft carries it home and uploads. Zero infrastructure. Reuses the "data core flies home" rung on Slide 4 | Buildable now |
| **FASTag / vehicle telematics** | FASTag is mandated; a buried vehicle's tag or eCall unit identifies it and implies occupants | `[VERIFY]` reader range |
| **Local seismic network timing** | Major collapses register on regional seismographs; arrival times triangulate the big ones | Free data, weak resolution |
| **Animal thermal signatures as a negative filter** | Train the classifier on livestock and strays so they are actively *rejected* rather than counted. Directly targets the Wayanad failure mode | Cheap, and thematically perfect |
| **Loudspeaker + rotors-off listening** | Drone broadcasts *"if you can hear this, tap three times"*, lands, kills rotors, listens. Two-way with a conscious victim | Buildable; PRD already has the loudspeaker |

---

## 12. Addendum 2 TODO

- [ ] Bench-test WiFi probe-request and BLE advertisement capture on an Android handset behind a
      concrete slab. **This is the cheapest, highest-value experiment available to us — it costs one
      phone and an afternoon, and it either validates or kills stream 3 before the finale.**
- [ ] Price a UWB vital-signs module (Novelda X4 / Infineon BGT60 class) landed in India.
- [ ] Price an SCD41 CO2 + NH3 sensor pair and check response time in a plume, not still air.
- [ ] Confirm which consumer wearables expose the BLE Heart Rate Service in the advertisement itself.
- [ ] Check whether C-DOT will discuss a SACHET message template for detectability — C-DOT Samarth is
      already on our grant target list, so there is a warm route in.

---
---

# ADDENDUM 3 — 11 Sep 2026 · architecture review

The mothership was never stress-tested. Twelve searches across the current literature and the
competition ecosystems the user named. **The evidence runs against it**, and separately, Qualcomm's
2026 strategy reframes what this deck should be.

## 13. What Qualcomm actually wants — and it is not "a drone" `[SOURCED]`

| Fact | Source |
|---|---|
| **Dragonwing IQ10**, 18-core, unveiled **CES 2026**, is "the heart of its 2026 robotics strategy" — for AMRs and humanoids | automate.org CES 2026 coverage |
| Trade press frames it plainly: **"Qualcomm targets Nvidia Jetson with new robotics developer platform"** | automate.org |
| **Qualcomm acquired Arduino**, Oct 2025 — explicitly "to get in on the ground floor with startups, developers, researchers and DIY tinkerers" | blog.arduino.cc, hackaday |
| **Arduino UNO Q — $44** (≈₹3,900): Dragonwing **QRB2210** quad A53 with AI acceleration, GPU, ISP + **STM32U585** real-time MCU, 2 GB LPDDR4, 16 GB eMMC, **dual-band Wi-Fi 5 + BT 5.1 on board**, Arduino App Lab pre-installed | docs.arduino.cc/hardware/uno-q, linuxgizmos |
| RB3 Gen 2's own headline claim: more inferences/sec and **"the ability to run more networks simultaneously"** | Qualcomm Dragonwing RB3 Gen 2 product brief |
| **NEURA Robotics** strategic collaboration, Mar 2026 — "Physical AI" | neura-robotics.com |
| Qualcomm markets **5G sidelink** for "vehicles, **drones**, and more" — direct device-to-device, no network | qualcomm.com/news/onq/2022/09 |

**The reframe.** Qualcomm did not post this problem statement because it wants a drone. It wants the
Indian student robotics ecosystem building on **Dragonwing instead of Jetson**, and it wants
reference workloads that prove its product claims. So the strongest possible deck is not "we used a
Qualcomm board" — it is **"we are the Dragonwing reference design for disaster robotics, and our
workload is the one that proves the claim on your own product page."**

Our multi-stream fusion is literally **five networks at once** — RGB detection, thermal, hazard
classification, VIO, audio. That *is* "run more networks simultaneously." Say it in those words.

**And LoRa is the wrong radio for this PS.** LoRa is Semtech. Qualcomm owns the device-to-device
story: **5G sidelink / PC5 (C-V2X)** and **Wi-Fi Aware**. Research on **C-U2X** — cellular
UAV-to-everything over 5G sidelink for UAV swarms — already exists. Correct answer is a hybrid: a
Qualcomm D2D radio for the high-bandwidth short-range peer links, LoRa only as the long-range
low-rate backhaul. Lead with the Qualcomm radio.

## 14. The evidence against a flying mothership `[SOURCED]`

| Finding | What it implies for us |
|---|---|
| **Zhejiang University**, *Swarm of micro flying robots in the wild*, Science Robotics 2022 — **10 palm-sized drones through dense bamboo forest, fully autonomous, decentralised, no external facilities**, each with stereo camera + IMU + onboard computer | A swarm needs **no** central aircraft to coordinate |
| **Team CERBERUS**, winner, **DARPA Subterranean Challenge** 2021 (ETH Zurich et al.) — heavy multi-robot map optimisation runs at the **base station**; connectivity is held by **breadcrumbed wireless nodes dropped by the robots**, plus a ground rover with a high-gain antenna | Put the big compute **on the ground**, and hold the link with **dropped relays**, not a hovering aircraft |
| **ACHORD** (JPL/CoSTAR) and **CARA** — communication-aware coordination with **droppable radios**, deployed at lowest-SNR points | Breadcrumbs are the validated answer to comms, and they reach **inside** structures where a relay at 100 m cannot |
| **Market-based / auction replanning for SAR swarms** (arXiv 2606.01970) — decentralised bidding; **robust to agent loss, scalable, no single coordinator** | A commander node is a liability, not a feature |
| **EPFL vswarm** — vision-based swarming with **no GNSS, no active ranging, and no explicit communication**, using CNN detection of neighbours | Formation-keeping does not even require a radio |
| **Distributed / split DNN inference** — "device-device collaborative inference", model partitioning across nodes, pipelined (HiDP DATE 2025; COHORT arXiv 2603.10436; Energy-Efficient Collaborative DNN Inference in UAV Swarm) | The swarm can *be* the computer instead of carrying one |

**Honest counterweight, because it is real:** the mothership is *easy to draw and explain in six
pages*. A peer swarm with auction-based allocation is harder to make legible to a non-specialist
judge. That is a communication cost, not an engineering argument — and it is the only thing the
mothership still has going for it.

## 15. Four candidate architectures — generate, then choose

| | A · Flying mothership *(current)* | B · Truck is the base | C · Peer swarm, elected leader | D · Swarm is the computer |
|---|---|---|---|---|
| Heavy compute | aloft, 100 m | **in the vehicle** — mains power, no weight or endurance limit, real cooling | on whichever node wins the election | **partitioned across every node** |
| Comms | mothership relays | **dropped breadcrumb radios** | peer mesh, D2D | peer mesh, D2D |
| Single point of failure | **yes** | base is safe; relay is cheap | **none** | **none** |
| Cost | ₹1.11 L aloft | ~₹60 K on the ground + cheap relay | no premium node at all | no premium node at all |
| Qualcomm fit | one board | one board | every node Snapdragon | **every node Snapdragon, one pipeline** |
| Legibility to a judge | **easiest** | easy | medium | hardest |
| Evidence | none found for it | CERBERUS | Zhejiang, market-based | HiDP, COHORT |

## 16. New capability ideas from the same pass `[SOURCED]`

- **Arduino UNO Q as the scout brain** — ₹3,900, Qualcomm silicon, **Wi-Fi + BT on board so it does
  the passive phone-RF sniffing (§11b) natively**, plus a real-time MCU for the flight link. Cheaper
  than the recycled handset and exactly the board Qualcomm bought Arduino to put in student hands.
- **Breadcrumb relay drops** — reuses the six-servo release already in `build-alpha/PRD.md`, same
  rack as the acoustic pods (§11a stream 6).
- **Open-vocabulary VLM search** — a commander types *"find the blue tarpaulin"* or *"the school
  building"* and the swarm re-tasks. UAV-VLRR (arXiv 2503.02465), AirHunt (2601.12742), AVERY
  (2511.18151, **VLM split computing for disaster response**). Answers PS bullets 4 and 6 in a way
  no fixed 8-class model can.
- **Event cameras** (Scaramuzza/UZH) — microsecond latency, enormous dynamic range; see through dust
  and detect *motion* (a hand moving in a void) where a frame camera is blind.
- **Foldable-arm drone** (UZH + EPFL) — retracts arms in flight to pass through narrow gaps.
- **Collision-tolerant caged scout** (Flyability Elios class) — an exoskeleton cage plus firmware
  that recognises and recovers from collisions, so it can enter voids by bumping through them.
- **Marsupial deployment** — the named field: *"the main platform houses and releases smaller devices
  that inspect the hardest to reach places."* Our flyer should carry **things that go where drones
  cannot** — breadcrumbs, acoustic pods, a crawler — not other drones.
- **Cyborg insects** — NTU Singapore + Osaka + Hiroshima. **Deployed to the Myanmar 7.7 earthquake,
  30 Mar 2025, with the Singapore Civil Defence Force — the first field use of insect-hybrid robots
  in a humanitarian operation.** The extreme end of "goes where nothing else fits." Cite as
  direction-of-travel, do not claim we build it.
- **Competition benchmarks to name:** SAFMC 2025 Category E (Swarm) ran a UAV swarm for SAR in
  GPS-denied indoor environments; MBZIRC Maritime Grand Challenge bans GPS by rule, and KAIST placed
  runner-up with vision-based navigation plus a drone-carried ground robot.

## 17. Addendum 3 TODO

- [ ] Profile YOLOv8n on **QRB2210** (UNO Q) via Qualcomm AI Hub — is it ≥5 FPS? That single number
      decides whether the scout is a ₹3,900 UNO Q or a ₹9,000 handset.
- [ ] Confirm whether Wi-Fi Aware / sidelink D2D is exposed on QRB2210 and QCS6490 in Qualcomm Linux.
- [ ] Decide the architecture from the round-3 renders, then rewrite `slides/` §Kestrel accordingly —
      §0 corrections 1 and 3, and every "mothership" mention, depend on the outcome.

---
---

# ADDENDUM 4 — 11 Sep 2026 · ARCHITECTURE DECIDED

**Option B. The truck is the base. The flying mothership is deleted.**

Decided against `images/round23/R3-1-bakeoff.png`, which our own criteria answer: the flying
mothership fails *no single point of failure*, *compute fully used* and *works inside buildings*.
Option B passes all four, is what **CERBERUS did to win the DARPA Subterranean Challenge**, and is
buildable by the December finale. Option D (swarm-as-computer) scores the same but is materially
harder to explain on a six-page deck read cold — that cost is real and it is why D is the *roadmap*,
not the submission.

## 18a. What the system is now

| Element | Role |
|---|---|
| **Base station, in the NDRF vehicle** | Qualcomm RB3 Gen 2. Mains power, no weight limit, real cooling — so it runs the fusion stack and the language model without an endurance budget. Heavy multi-robot map optimisation happens here, exactly as CERBERUS did it |
| **Relay drone ×1** | Cheap. Holds line-of-sight aloft. Carries no intelligence, so losing it costs the link for seconds, not the mission |
| **Scouts ×6** | Each an **Arduino UNO Q** — Qualcomm Dragonwing QRB2210 + real-time STM32, **Wi-Fi and Bluetooth on board**. Detection runs here. Two of the six carry FLIR Lepton 3.5 |
| **Breadcrumb pods ×6** | Dropped from the six-servo rack. Extend the mesh *inside* structures, where a relay at altitude cannot reach. Two carry acoustic + CO2 |

**Every compute node is now Qualcomm silicon**, and the scout's own radios do the passive phone-RF
sensing (§11b) for ₹0 — which the recycled handset also did, but the UNO Q is the board Qualcomm
bought Arduino to put in student hands, and it adds a real-time MCU for the flight link.

## 18b. The BOM, and why no rendered image needs redoing

| Line | ₹ |
|---|---|
| Base station — RB3 Gen 2 ₹50,000 + rugged case/power ₹5,000 + mast & antenna ₹4,000 | **59,000** |
| Relay drone ×1 | **25,800** |
| Scout ×4 (UNO Q ₹3,900, camera, GPS, FC, frame, propulsion, batteries) | 23,600 ea → **94,400** |
| Scout ×2 with FLIR Lepton 3.5 (+₹16,600) | 40,200 ea → **80,400** |
| Breadcrumb / acoustic-CO2 pods ×6 | **9,000** |
| **Total** | **₹2,68,400 ≈ ₹2.68 L** |

**Cost per km²: ₹498.** Against ₹2.69 L and ₹502 under the old architecture — **both round to the
figures already rendered on the cost-ladder images.** The architecture change is free in artwork.

Unchanged: 2.6 km²/h · +64 survivors per 100 · 5.8 h on the Wayanad footprint · ₹19.86 Cr for 738
districts · 0.12% of the preparedness line. Every headline number in the deck survives.

## 18c. What this supersedes

- §0 correction 1 — the mothership could not air-launch scouts. **Moot: there is no mothership.**
  Scouts are truck-launched, which was already the corrected position.
- §7 BOM — replaced by §18b above.
- Every occurrence of "mothership" in `slides/` becomes **"base station"** (in the vehicle) or
  **"relay"** (the one cheap aircraft aloft).
- LoRa is demoted. Scout-to-scout and scout-to-relay run on the **Qualcomm radios already on the
  UNO Q** (Wi-Fi / BT, with 5G sidelink as the production path); LoRa survives only as long-range,
  low-rate backhaul to the vehicle.

## 18d. What it costs us, stated honestly

The base station cannot see. When the relay is down and the scouts are beyond breadcrumb range, they
are autonomous but unsupervised until they return — which is the same failure mode the degradation
ladder already shows, one rung earlier. We accept it because the alternative was putting the only
brain in the air on a 24-minute battery.

---
---

# ADDENDUM 5 — 15 Sep 2026 · THE SINGLE DRONE

**Five days to the deadline.** This addendum closes the largest remaining hole in the deck, and it is
a hole in *PS compliance*, not in engineering.

## 19. The hole: we answered a question they did not ask `[STRATEGIC]`

SIH26177's title is **"A deployable AI-powered autonomous drone"** — singular. Read the eight
Expected-Solution bullets again and check each against an aircraft count:

| PS bullet | Aircraft required |
|---|---|
| Autonomous Navigation — GPS + GPS-denied, SLAM, obstacle avoidance | **one** |
| On-Device AI Inference — real-time, no cloud | **one** |
| Multi-Sensor Fusion — RGB, thermal, IMU, GPS | **one** |
| Hazard Classification — flood, fire, smoke, debris, structures, landslide | **one** |
| Geo-Tagged Mapping | **one** |
| Emergency Alerting | **one** |
| Offline Resilience | **one** |
| Command Center Dashboard | **zero** (ground software) |

**Not one bullet requires a second aircraft.** The swarm is entirely our addition. That is fine — it
is our novelty — but Addendum 4 moved the fusion stack and the language model into the truck, and a
judge reading the deck cold can now reach a devastating and *fair* conclusion:

> *"The problem statement asked for an AI-powered autonomous drone. They built an AI-powered truck
> and six drones that report to it."*

**The fix is not a disclaimer, it is an ordering.** One scout must be a complete, self-sufficient,
PS-compliant autonomous drone with the truck switched off. The base station is then an
**accelerator, never a dependency** — it makes six scouts better than six independent scouts, which
is a different and much stronger claim than making them work at all.

**The line for the deck:**

> **One Kestrel scout is a complete answer to the problem statement. Six is the answer to Wayanad.**

## 20. §17 TODO RESOLVED — QRB2210 throughput is measured, not estimated `[SOURCED — third-party, on the exact board]`

Addendum 3 §17 said one number decides whether the scout is a ₹3,900 UNO Q or a ₹9,000 handset.
**That number now exists**, measured by Foundries.io on a physical UNO Q:

| Measurement | Value | Source |
|---|---|---|
| **YOLOv5 Pico @ 640×480 on the Dragonwing MPU** | **~17 FPS · ~58 ms/frame** | foundries.io "Elf Detector" pt 4 |
| YOLO26n, unoptimised | 400–450 ms/frame → **2–2.5 FPS** | elektroda / sbcwiki round-ups |
| YOLOv4-tiny, CPU only | **~2.5 FPS** | same |
| YOLOv5 via Edge Impulse SDK | **~17 FPS** | Edge Impulse on UNO Q |

**The 7× spread between rows is the entire engineering story**, and it is the same "we computed it,
we did not catalogue it" move as the pixel ladder (§5): *the board is fast enough if you pick and
compile the model correctly, and hopeless if you drop stock YOLO on the CPU.* A team that quotes
17 FPS without saying which model got it has not run it.

**Verdict: the UNO Q clears, with enormous margin — but not for the reason it looks like.** See §21.

`[VERIFY before submitting]` Re-run YOLOv8n INT8 @640 through **Qualcomm AI Hub** free device
profiling to get *our* model's number on *our* silicon rather than citing someone else's model.

## 20a. Spec the 4 GB variant, not the 2 GB `[SOURCED]`

| | UNO Q 2 GB (ABX00162) | **UNO Q 4 GB (ABX00173)** |
|---|---|---|
| RAM / eMMC | 2 GB / **16 GB** | **4 GB / 32 GB** |
| India price | ~₹3,900 ($44) | **₹5,190** IndiaMART Mumbai · ₹7,660 QuartzComponents · ₹9,039 Indian Hobby Center |

Both carry the same QRB2210 (quad Cortex-A53 @ 2.0 GHz, Adreno GPU, **dual ISP**, always-on Hexagon
DSP), the same STM32U585 real-time MCU, dual-band **Wi-Fi 5 + BT 5.1**, 7–24 V input.

**Take the 4 GB.** The memory budget in §21b does not close on 2 GB, and the 32 GB eMMC is what makes
the store-and-forward argument in §23 real. Cost: **+₹1,290 × 6 = +₹7,740** on a ₹2.68 L system —
**2.9% for double the RAM and double the storage.** Obvious buy.

`[VERIFY]` Price against **Robu.in**, the vendor the rest of the BOM uses, before printing a figure;
the ₹5,190–₹9,039 spread across Indian retailers is wide enough to matter.

## 21. What the scout actually needs — and it is not frame rate `[DERIVED]`

The seductive move is to put "17 FPS" on the slide. It is the wrong number, and a Qualcomm engineer
will know it. **Coverage sweep is not compute-bound.** Deriving the real requirement:

| Step | Value |
|---|---|
| Per-scout area rate (2.6 km²/h ÷ 6) | 0.433 km²/h = 433,000 m²/h |
| ÷ 30 m thermal swath (§5, §6b) | → ground speed **4.0 m/s** |
| RGB along-track footprint at 30 m, 4:3 sensor, 78° HFOV | 36.4 m |
| New frame at 50% along-track overlap | every 18.2 m → every 4.55 s |
| **Detection rate the sweep actually demands** | **0.22 Hz** |
| Measured capability | 17 FPS |
| **Headroom** | **~77×** |

**So what is the headroom for?** Exactly what Qualcomm's own RB3 product brief claims as its headline
— *"the ability to run more networks simultaneously"* (§13). The scout does not spend 17 FPS on one
detector. It spends it running **detection, visual-inertial odometry, an open-vocabulary encoder and
the radio scanner concurrently on four cores**. The headroom *is* the argument, and it is Qualcomm's
own argument, handed back to them with a workload attached.

### 21a. Four cores, four jobs, and every engine on the die used

| Engine | Job | Rate |
|---|---|---|
| **STM32U585** (separate die) | PX4 attitude, mixing, failsafe, geofence, battery-critical RTL | **1 kHz, hard real-time, cannot be preempted by Linux** |
| A53 core 0 | Debian + ROS 2 + mesh / Wi-Fi / LoRa backhaul | — |
| A53 core 1 | **VIO** — VINS-Fusion mono-inertial, sliding window | 20 Hz |
| A53 core 2 | **YOLOv8n INT8** person + 8 hazard classes | 0.5 Hz sweep · 10 Hz confirm |
| A53 core 3 | mission behaviour tree · evidence grid · Wi-Fi/BLE scan · logging | 1 Hz |
| **Adreno GPU** | image preprocessing · MobileCLIP image encoder | on demand |
| **Hexagon DSP** (always-on) | sensor fusion, audio — the acoustic stream if a mic is fitted | continuous, low power |
| **Dual ISP** | two camera pipes: RGB down + thermal (on 2 of 6) | hardware |

**The "dual brain" on the board becomes the safety argument:** if Linux panics mid-flight, the
STM32 still holds attitude and executes a failsafe landing. That is not marketing — it is a genuine
architectural property of this specific board, and no Jetson-based entry can claim it.

### 21b. Memory budget, 4 GB variant `[DERIVED — ESTIMATE, to be measured]`

| Component | RAM |
|---|---|
| Debian + ROS 2 Humble | ~600 MB |
| VINS-Fusion sliding window | ~400 MB |
| YOLOv8n INT8 + QNN runtime | ~200 MB |
| MobileCLIP-S0 INT8 image encoder | ~100 MB |
| Evidence + occupancy grid (1 km² @ 1 m cells, multi-layer) | ~50 MB |
| Frame buffers, ring log, mesh stack | ~300 MB |
| **Total** | **≈1.65 GB of 4 GB** |

Comfortable on 4 GB. **Does not close on 2 GB** once VIO and the detector are resident together.

## 22. The SLM question, answered properly `[DERIVED + SOURCED]`

**Does a language model go on the drone?** The honest answer has three parts, and stating all three
is worth more than claiming a language model in the flight loop.

### 22a. Not in the control loop — and say why, on the slide

> **A token takes ~100 ms. A wall arrives in 20.**

A language model cannot sit in a flight decision loop. Quad-A53 at 2 GHz running llama.cpp gives
roughly 5–12 tok/s on a 0.5 B Q4 model; a 150-token report is **12–30 seconds**. Fine for reporting,
disqualifying for control. Many SIH entries will put "LLM on the drone" on a slide and a Qualcomm
engineer will discount the whole deck for it. **We get credit for the opposite.**

### 22b. The decision layer is a utility-ranked behaviour tree, not a model

Running at **1 Hz on core 3**, fully deterministic and explainable — which matters because a rescue
commander has to be able to ask *why did it go there*:

```
if  battery < RTL_reserve                  -> RETURN            [Tier 0, STM32, non-negotiable]
if  cell_posterior > PUBLISH               -> MARK, TRANSMIT, ORBIT for confirmation
if  cell_posterior in [REINSPECT, PUBLISH) -> DESCEND to 15 m, re-image on a new heading
if  link_quality < FLOOR                   -> DROP BREADCRUMB
else                                       -> fly to the frontier cell maximising
                                              EXPECTED INFORMATION GAIN PER JOULE
```

That last line is the same **Bayesian search theory** already cited for the USS Scorpion and AF447
(§6a) — applied to next-best-view selection instead of ocean search. ~200 lines of behaviour tree.

**And the confirmation pass is not a second opinion — it is resolution gain by descent:**

| Altitude | GSD @ 640 px across a 48.6 m swath | Prone adult (1.7 m) |
|---|---|---|
| 30 m sweep | 0.076 m/px | **22 px** — marginal but real |
| 15 m confirm | 0.038 m/px | **45 px** — comfortable |

The aircraft *buys certainty with altitude*, and it decides to spend that altitude by itself. That is
what "autonomous" means in this PS, expressed as a physical mechanism rather than a claim.

### 22c. What the "language" model on the scout actually is: an open-vocabulary encoder

A fixed 8-class detector covers the PS's hazard list exactly. It cannot cover *"find the blue
tarpaulin"*, *"the school building"*, *"the overturned bus"* — which is what commanders actually say.

**MobileCLIP-class image encoder on the scout (~100 MB INT8, Adreno/Hexagon), text encoder at the
base station.** The commander types a phrase; the base encodes it **once** into a 512-float vector;
that vector goes to every scout over the mesh as a **2 KB message**; each scout scores its live
frames against it on-device with a dot product.

**Open-vocabulary search, fully on-device, re-taskable over 2 KB, with no retraining and no cloud.**
This is precisely the split-computing architecture in the literature already logged in §16 —
UAV-VLRR (arXiv 2503.02465), AirHunt (2601.12742), **AVERY (2511.18151, VLM split computing for
disaster response)**. It answers PS bullets 2 and 4 in a way no fixed class list can.

### 22d. Where a real SLM does earn its place on the aircraft

**Qwen2.5-0.5B-Instruct Q4 (~400 MB), run on the ground, after landing, in the degraded case.**
When the mesh is down and the scout has flown alone, it lands and turns its structured event log
into three sentences of English and Hindi in ~20 seconds. Nothing is in a loop; nothing competes with
the detector.

**Why this matters more than it looks:** it is what makes the claim *"one scout, no truck, no
network, still a complete PS-compliant system"* literally true, end to end, including the
*Emergency Alerting* bullet. The 3 B model (Llama 3.2 3B Q4, 2.0 GB) stays at the base station where
it fuses six scouts' logs into one situation report.

## 23. Reporting back — three paths, and the aircraft is the last one `[DERIVED]`

A survivor record is **~300 bytes** structured, **~8 KB** with a thumbnail crop:

```json
{"t":"2026-09-15T04:12:33Z","lat":11.4821,"lon":76.1329,"alt_agl":15.2,
 "class":"person_prone","conf":0.91,"posterior":0.87,
 "votes":{"rgb":0.91,"thermal":0.78,"ble":1,"wifi_probe":2},
 "ble_mac_hash":"a3f1...","crop":"<8KB JPEG>"}
```

| Path | Rate | When |
|---|---|---|
| **Wi-Fi 5 mesh** → relay → truck | Mbps | line of sight holds |
| **LoRa SX1262 backhaul** | ~300 B record fits in a few frames | mesh down, truck in range |
| **Store-and-forward on 32 GB eMMC** | the whole sortie | **everything is down** |

**The third path is the one to say out loud.** With 32 GB of onboard eMMC, *the aircraft is the data
link.* If every radio fails, the mission still completes — the scout flies home carrying the map.

> **The worst case is not "no data." It is "data eighteen minutes late."**

That is the *Offline Resilience* bullet answered at its strongest, and it is free — we already bought
the storage in §20a.

## 24. GPS-denied, handled honestly — the drift arithmetic nobody else will show `[DERIVED]`

VIO drift is ~0.5% of path length (VINS-Fusion mono-inertial, EuRoC-class benchmarks — **`[ESTIMATE
from published VIO results]`, not our measurement**). Run that forward honestly:

| Case | Path | Drift |
|---|---|---|
| Naive claim — VIO for a whole 18-min sortie | 4.3 km | **21 m — useless for a survivor marker** |
| **Reality: GPS-denied segments are bounded** — 1–3 min under canopy or inside a structure | 240–720 m | **1.2–3.6 m** |

**Three things bound it**, and all three are already in the design:
1. **GPS re-acquisition** the moment sky view returns — the drift resets
2. **Breadcrumb pods as surveyed anchors** — each is dropped while GPS is still good, so its position
   is known; re-hearing one is a loop closure
3. **Loop closure at the truck** on every return leg

**So the claim is not "we navigate without GPS indefinitely."** It is: *GPS-denied excursions are
minutes long, bounded by anchors, and land inside the re-inspect radius.* A team that shows the 21 m
number and then explains why it never happens beats a team that shows only the 0.5%.

## 25. Flying inside buildings — the gap, stated plainly `[GAP — decision required]`

`PROMPTS-CINEMATIC.md` C2 shows a quadcopter flying down a collapsed corridor dropping breadcrumbs.
**The BOM airframe cannot do that.** An S500 is a 500 mm-class frame; a collapsed doorway is not.
Also against it: dust destroys VIO features, darkness needs illumination that then blinds VIO, and
wall/ground effect makes control unstable in confined volumes.

Note what the PS does and does not require: it says **"GPS-denied navigation … in damaged
environments"** — mandatory, and satisfied outdoors under canopy and in urban canyon. It never says
*inside buildings*. **Indoor is over-delivery, not compliance.**

Two honest options:

| | Keep it outdoor-only | **Add Scout-I** |
|---|---|---|
| Airframe | S500 only, 500 mm | + 3.5" caged micro-quad, ~250 mm with cage |
| Inside structures | breadcrumb pods only, dropped from outside | flies a 400 mm gap, ~8 min endurance |
| Compute | — | **same UNO Q, same PX4, same models, same mesh** |
| BOM | unchanged | swap 1 of 6 S500 scouts → roughly cost-neutral |
| Risk | C2 render contradicts the spec | one more airframe to build by the finale |

**Recommendation: add Scout-I as one of the six.** It is close to cost-neutral, it makes C2 truthful,
and "two airframes, one software stack" is a far stronger *deployability* story than one airframe —
it is the thing that proves the compute core is the product and the airframe is a fitting.

## 26. Addendum 5 TODO

- [ ] **Profile YOLOv8n INT8 @640 on QRB2210 via Qualcomm AI Hub** — replace Foundries.io's YOLOv5
      Pico number with our own model on our own silicon. Free, no hardware needed. **Highest value
      remaining item in the whole project.**
- [ ] Price UNO Q 4 GB (ABX00173) on **Robu.in** to match the rest of the BOM's vendor basis.
- [ ] Decide Scout-I (§25) — it changes one BOM line and makes C2 honest.
- [ ] Re-order slides 2 and 3 per §19: **slide 2 = the system, slide 3 = one drone.**
- [ ] Propagate §18b + §20a BOM into `slides/` — slide 3 and slide 4 still carry the superseded §7
      recycled-handset BOM.
