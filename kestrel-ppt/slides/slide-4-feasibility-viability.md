# Slide 4 — Feasibility and Viability

**Official section:** "Feasibility and Viability"
Template sub-bullets, verbatim: *analysis of the feasibility of the idea · potential challenges and
risks · strategies for overcoming these challenges*

**Prompts: 3.** `P4.1` the cost ladder · `P4.2` what happens when it fails · `P4.3` the flight plan.

---

## The argument this page has to land

Two thirds of this section is explicitly about **risk**. Most decks answer it with a table of
non-risks ("scalability", "user adoption") and lose the marks. The way to win it is to name the
things that can genuinely kill this system, in the order of how likely they are, and show that each
one has an engineered answer — and to volunteer the one number that argues against us before a judge
finds it.

**The volunteered number:** a single scout costs **₹430 per km²**; the full swarm costs **₹502**. The
mothership is overhead. **We are not selling cheapness — we are buying time**, and time is the only
currency the survival curve accepts. Saying this on the page converts our weakest number into
evidence that we did the arithmetic honestly.

**And the helicopter is not slower than us.** A charter helicopter sweeps ~13.7 km²/h against our
2.6 — five times more area per hour. It costs 27× more per km², cannot fly at night or in monsoon
IMC, takes 1–3 hours to position, and puts one pair of human eyes at 300 m on the problem, where a
1.7 m person subtends about 20 arcminutes — the edge of human acuity, against clutter, at 74 km/h.
**Helicopters are transport. They were never the sensor.** Getting this right is worth more than the
easy false claim.

---

## Layout

```
┌──────────────────────────────┬────────────────────────────────┐
│  P4.1  THE COST LADDER       │  P4.2  WHEN IT FAILS           │
│  27x per km², 86-min meter   │  four degradation rungs        │
├──────────────────────────────┴────────────────────────────────┤
│  P4.3  WHOSE ASSET, WHOSE MONEY — DDMA + the 0.12%            │
├───────────────────┬───────────────────┬───────────────────────┤
│ table: BOM        │ table: ROADMAP    │ table: RISK REGISTER  │
└───────────────────┴───────────────────┴───────────────────────┘
```

*Three images, three tables. If this reads tight in the real template, the BOM compresses to its
three group totals — the per-line detail lives in `DATA.md` §7 and nobody scores a slide on line
items.*

---

## P4.1 — The cost ladder `[DATA-EXACT — physical infographic]` · **v2**

> **Why v1 failed — the fault was in the brief, not the render.** v1 stacked **₹1.89 L/hr** (a *rate*)
> against **₹2.69 L** (a *one-time capital cost*). Those are different units, so no arrangement of
> heights can be read correctly: 1.89 is the smaller number but the bigger cost, and the model
> resolved the contradiction by making the helicopter stack *taller* than its own label justified.
> Either way the page argues the opposite of the truth. **v2 compares like with like** — ₹ per km²
> surveyed, which is the number `DATA.md` §6c actually derives — and demotes the "86 minutes" line to
> a separate, explicitly-labelled meter strip where it cannot be misread as a height comparison.

Paste the STYLE.md global prefix first.

```
A 16:9 editorial infographic on deep navy, split into two clearly separated regions by generous negative space: a LEFT REGION occupying about 55% of the width, and a RIGHT REGION occupying about 40%, with a wide dark gutter between them.

LEFT REGION — a physical money comparison, two columns standing on one shared thin slate-grey baseline, both columns exactly the same width and built from identical photorealistic bundles of Indian rupee banknotes, lit from the side with real weight and shadow:
- the FIRST column is extremely tall and slender, towering nearly to the top of the frame, made of many stacked bundles. Resting on top of it, small, a warm amber-lit single-engine utility helicopter.
- the SECOND column is almost flat — a single thin bundle, barely a slab above the baseline, roughly one twenty-seventh the height of the first. Resting on it, laid out in a neat row and lit cyan, one hexacopter and six small quadcopters.
The extreme height difference between the two columns is the entire point of this region and must be unmistakable.

RIGHT REGION — a horizontal meter strip, drawn as a long slim rounded bar lying on its side, divided by fine tick marks into three equal labelled hours. The leftmost portion of the bar, covering slightly under half of the first two hours, is filled solid cyan; the remainder of the bar is filled amber and continues to the frame's right edge. A thin vertical cyan cut-line marks the boundary between the cyan and amber fills, with a small hexacopter-and-six-quadcopters icon sitting just above the cyan portion and a small amber helicopter icon sitting just above the amber portion.

Render style: premium product-photography lighting on the banknote columns and the vehicles; flat precise editorial typography and flat vector treatment for the meter strip. The columns must read as real stacked money, not as bars. No axes, no gridlines, no legend box.

Text labels (render exactly):
LEFT REGION:
- above the first tall column, amber, large: "13,800"
- directly beneath that, amber, small: "CHARTER HELICOPTER"
- above the short second column, cyan, large: "502"
- directly beneath that, cyan, small: "KESTREL SWARM"
- centred above the whole left region, in #E2E8F0: "RUPEES PER KM2 SURVEYED"
- floating in the gutter beside the tall column, amber, large: "27x"
RIGHT REGION:
- above the meter strip, in #E2E8F0: "SAME MONEY, DIFFERENT PURCHASE"
- under the cyan portion of the strip, cyan, stacked two lines: "2.69 LAKH — 86 MIN" / "THE ENTIRE SYSTEM, ONCE"
- under the amber portion of the strip, amber, stacked two lines: "1.89 LAKH PER HOUR" / "AND IT KEEPS RUNNING"
- tick labels along the strip, small slate grey: "1 H" then "2 H" then "3 H"
FOOTNOTES:
- lower-left corner, small slate grey: "CHARTER 1.6 L/HR + 18% GST, IAMSAR SWEEP RATE"
- lower-right corner, small slate grey: "KESTREL CAPEX OVER 300 FLIGHT HOURS"

Constraint tail: 16:9. Only the labels listed. No watermark, no border, no confetti, no coins raining.
```

*Two things to verify on every generation, because the whole argument rests on them: the **tall column
must be the amber helicopter one** (₹13,800 is the big number now, so tall = expensive = correct), and
the cyan column must be nearly flat. If the model equalises the heights or inverts them, regenerate.
Numbers check against `DATA.md` §6c and §7 — `[DATA-EXACT]`.*

---

## P4.2 — When it fails `[isometric ladder, four rungs]`

```
An isometric technical illustration on deep navy, 16:9, showing four scenes arranged as descending steps from upper-left down to lower-right, like four rungs of a staircase, each rung a small self-contained diorama on its own floating platform. A single thick arrow runs down the whole staircase, starting bright cyan at the top and fading through pale cyan to amber at the bottom — but never breaking.

RUNG 1 (top, brightest): one hexacopter and six quadcopters over a debris field, all connected by a bright dense cyan mesh web, plus a link running off-frame to a cell tower.
RUNG 2: the same formation but the mesh is thinner and dimmer, the cell tower is gone and crossed out, and only sparse long-range links remain between the aircraft.
RUNG 3: the mesh is gone entirely. The quadcopters continue flying their lanes alone. A small glowing data-core cylinder is visible inside each one, and a dotted return path arcs from one quadcopter back to a small truck icon.
RUNG 4 (bottom, dimmest): two of the six quadcopters are shown fallen and dark on the rubble. The remaining four continue their lanes, and their lanes have visibly widened to redistribute the same coverage area between fewer aircraft.

Render style: clean isometric technical diorama, restrained, generous space between rungs. The descending arrow must be continuous and unbroken across all four rungs.

Text labels (render exactly, one caption beside each rung, plus one closing line):
- rung 1, cyan: "FULL MESH + 5G — MBPS"
- rung 2, cyan: "TOWER DOWN — LoRa KBPS"
- rung 3, slate grey: "NO LINK — DATA CORE FLIES HOME"
- rung 4, amber: "SCOUTS LOST — LANES WIDEN"
- along the bottom edge, centred, #E2E8F0: "IT GETS SLOWER. IT DOES NOT STOP."

Constraint tail: 16:9. Only the labels listed. No explosions, no fire, no weapons. No watermark, no border.
```

*This visual is the answer to "potential challenges and risks" and to the PS's *Offline Resilience*
bullet in one frame. The unbroken arrow is the argument: every rung degrades throughput, none of them
ends the mission.*

---

## P4.3 — Whose asset, whose money `[DATA-EXACT — institutional infographic]` · **NEW**

> **This replaces the roadmap image as slide 4's third visual, and the roadmap becomes a native
> table.** The trade is deliberate: a roadmap is inherently tabular and loses nothing as five rows of
> dates, while *this* argument cannot be a table — "0.12% of a budget line that already exists" only
> lands if you can see it. It answers four of the nine official criteria at once — **feasibility,
> practicability, sustainability, and potential for future work progression** — and it is the answer
> to the question every government judge is actually holding: *who buys this, and with what money?*
> The already-rendered flight-path roadmap is a good asset; keep it for the finale deck, where the
> slide budget is not six pages. Its prompt is archived at the bottom of this file.

Paste the STYLE.md global prefix first.

```
A 16:9 editorial infographic on deep navy, divided into two clearly separated halves by generous negative space.

LEFT HALF — an institutional hierarchy drawn as three stacked horizontal tiers connected by thin vertical cyan lines, the tiers getting visibly wider toward the bottom:
- TOP tier: a narrow plaque containing a small government-building icon and, beside it, a tight cluster of exactly 16 small identical shield icons.
- MIDDLE tier: a wider plaque containing a map-of-a-state icon and a small group of 4 human-figure icons.
- BOTTOM tier: by far the widest plaque, filled edge to edge with a dense uniform grid of many tiny identical building icons, several hundred of them, packed tight. Sitting on top of this bottom plaque, rendered larger and glowing cyan so it clearly belongs to this tier and no other, one hexacopter with six small quadcopters beside it.
A thin amber arrow curves from the top tier down toward the bottom tier, drawn as a long dashed travelling path with a small clock icon on it. A separate short solid cyan arrow sits entirely within the bottom tier, drawn as a tight loop with a small lightning icon on it.

RIGHT HALF — a money-scale comparison. One very large horizontal bar spanning almost the full width of this half, filled solid slate grey, standing for a big budget. Immediately beneath its far-left end, a second bar of the same height that is almost invisibly short — a bright cyan sliver only a hair wide, with a thin cyan leader line pulling out to a label because it is too small to letter directly. Below both bars, a single row of three small flat chips.

Render style: flat precise editorial infographic, institutional-report discipline, restrained. Not a bar chart with axes — the two bars are a direct physical size comparison. No axes, no gridlines, no legend box.

Text labels (render exactly):
LEFT HALF:
- above the left half, in #E2E8F0: "WHOSE ASSET"
- on the TOP tier, slate grey: "NDMA + NDRF — 16 BATTALIONS"
- on the MIDDLE tier, slate grey: "SDMA + SDRF — STATE"
- on the BOTTOM tier, cyan: "DDMA — ALL 738 DISTRICTS"
- on the dashed amber travelling arrow, amber: "NDRF MUST TRAVEL"
- on the short cyan loop arrow, cyan: "DDMA IS ALREADY THERE"
RIGHT HALF:
- above the right half, in #E2E8F0: "WHOSE MONEY"
- above the large grey bar, slate grey: "16,015 CRORE — PREPAREDNESS LINE 2021-26"
- on the leader line from the cyan sliver, cyan, stacked two lines: "19.86 CRORE" / "ALL 738 DISTRICTS"
- floating beside the sliver, cyan, large: "0.12%"
- the three chips in a row, small, in #E2E8F0: "NO NEW BUDGET HEAD" then "90:10 FOR NE + HIMALAYAN STATES" then "CSR-ELIGIBLE, SCHEDULE VII (xii)"

Constraint tail: 16:9. Only the labels listed. The cyan sliver must be almost imperceptibly small next to the grey bar. Do not draw any national map or border. No watermark, no border.
```

*Verify: the bottom tier must be visibly the widest and must be the one carrying the drones — that
placement is the argument. And the cyan sliver must look almost too small to see; if the model gives
it a readable width, the 0.12% has been lost. Numbers trace to `DATA.md` §9b and §9c —
`[DATA-EXACT]`.*

**The two claims this image makes, both sourced.**

1. **NDRF has 16 battalions for 738 districts, so it is always *arriving*** — the Wayanad response
   included a 31-member team dispatched from Bengaluru. The **DDMA is mandated in every district by
   the Disaster Management Act 2005** and is present on hour zero. Kestrel is therefore a **DDMA
   asset, flown by SDRF, feeding the district EOC under the Incident Response System** — the tier that
   already owns the first six hours and today has no aerial search capability of its own.
2. **The money already exists.** 15th Finance Commission, 2021-26: SDRF ₹1,28,122.40 Cr + SDMF
   ₹32,030.60 Cr, a ₹1,60,153 Cr pool, of which **10% — ₹16,015 crore — is earmarked for
   "Preparedness and Capacity-building."** One system in all 738 districts costs **₹19.86 crore =
   0.12% of that line.** North-eastern and Himalayan states — Assam, Himachal, Uttarakhand, J&K,
   Nagaland, exactly this monsoon's worst-hit — fund at 90:10, so a state pays **₹26,910 per
   district.** And **Schedule VII (xii) of the Companies Act** (MCA GSR-390(E), 30 May 2019) makes
   disaster-management capability a **CSR-eligible spend** — so a ₹2.69 lakh district deployment is a
   CSR line item, and **Qualcomm India clears the Section 135 thresholds itself.**

---

## Native table — the roadmap (replaces the P4.3 image)

| When | Milestone |
|---|---|
| **Sep 2026** | Scout v0 flying — S500 airframe, PX4, phone-as-compute |
| **Oct–Nov 2026** | Fusion gate running on the Hexagon NPU; AI Hub profiling replaces every inference estimate |
| **Dec 2026** | **SIH Grand Finale** — v0 demonstrated |
| **Q1 2027** | Mothership + 2 scouts; LoRa mesh; district-EOC dashboard |
| **Q2–Q3 2027** | Full 6-scout swarm, field trials, **SDRF pilot with one DDMA** |

---

## Archived — P4.3 v1, the flight-path roadmap `[already rendered: images/P4.3-flight-plan.png]`

Keep for the Grand Finale deck, where the page budget is not six. Not used in the idea submission.

```
A 16:9 technical illustration on deep navy: a single continuous flight path drawn as a smooth cyan ribbon sweeping from the lower-left corner up and across to the upper-right, over a very faint topographic contour-line map in dark teal.

Along the ribbon sit five waypoint markers, evenly spaced, each drawn as a small circular navigation node with a thin vertical stem connecting it to its label. Each node contains a tiny distinct icon: (1) a single quadcopter, (2) a quadcopter with a camera symbol, (3) a trophy, (4) a hexacopter with two quadcopters, (5) a hexacopter with six quadcopters over a small map.

Waypoint 3 is rendered differently from the others — a larger amber diamond instead of a cyan circle — and the ribbon brightens as it passes through it.

After the fifth waypoint the ribbon continues briefly and fades out toward the upper-right corner, with a small green flag at its end.

Render style: precise aeronautical-chart aesthetic, thin linework, lots of dark negative space, restrained.

Text labels (render exactly, one under each waypoint stem, plus the flag label):
- waypoint 1, cyan: "SEP 2026 — SCOUT V0 FLYING"
- waypoint 2, cyan: "OCT-NOV — FUSION GATE ON NPU"
- waypoint 3, amber: "DEC 2026 — SIH GRAND FINALE"
- waypoint 4, cyan: "Q1 2027 — MOTHERSHIP + 2 SCOUTS"
- waypoint 5, cyan: "Q2-Q3 2027 — FULL 6-SCOUT SWARM"
- at the green flag, green: "SDRF FIELD PILOT"

Constraint tail: 16:9. Only the labels listed. No watermark, no border, no compass rose.
```

---

## Native table — bill of materials

Full per-line detail in `DATA.md` §7. On the slide, the compressed version:

| Group | Key lines | ₹ |
|---|---|---|
| **Mothership** | Qualcomm RB3 Gen 2 (12 TOPS) **50,000** · FLIR Lepton 3.5 **16,600** · Pixhawk 2.4.8 **8,514** · S550 airframe + 6× propulsion **11,632** · RGB 12 MP, LoRa hub, EC200U LTE, GPS, 2× 4S 5000 mAh, PDB, telemetry | **1,11,500** |
| **Scout × 6** | S500 frame **3,419** · propulsion **3,338** · FC **4,000** · **recycled Snapdragon phone 9,000** · LoRa node, 2× 4S 2200 mAh, PDB | **25,600 ea → 1,53,600** |
| Ground station | LoRa base + antenna (laptop owned) | 4,000 |
| **Total** | | **≈ ₹2,69,100** |

Prices are Indian-vendor sourced (Robocraze / Robu / Thundercomm / GroupGets), not indicative.
Three lines are still `[ESTIMATE]` and are tagged as such in `DATA.md` — they total under ₹20,000.

**Endurance and how sustained search is actually achieved.** From our own hexacopter PRD anchor
(12–15 min at 3 kg, T/W 1.5:1, 4S 5000 mAh): the mothership carries ~1.5 kg of sensors and holds
**~24 min** on a dual pack while hovering as a relay. Scouts hold **~18 min** per sortie. Continuous
coverage is not an endurance claim — it is **battery rotation**: scouts land at the truck, swap in
under a minute, and relaunch. Two spare packs per scout gives ~90 minutes of rolling coverage before
anything needs a charger. **This is the reason the scouts are truck-launched and not air-launched: an
air-dropped scout gets one life, a truck-launched scout gets five.**

---

## Native table — risk register

| # | Risk — named honestly | Likelihood | Strategy |
|---|---|---|---|
| 1 | **Daylight thermal inversion.** Sun-soaked rubble reaches 45–55 °C; skin is ~33 °C. In daylight the survivor is *colder* than the debris and every hot-spot filter inverts. This is documented operator testimony, not theory | **High — every clear afternoon** | Band-pass on 30–40 °C rather than "hottest pixel", and RGB pose carries the daylight decision while thermal carries the night. The gate (P3.2) requires agreement, so neither sensor can fail the mission alone |
| 2 | **False positives cost lives by consuming rescuers.** The Wayanad precedent: three "breath signals", 1,300 people, nothing there | **High** | Three-gate corroboration; publish a confidence score and the evidence tiles with every marker. A rescue commander re-tasks on evidence, never on a bare pin |
| 3 | **BVLOS is not freely permitted in India.** Only three national BVLOS corridors exist; beyond-visual-line-of-sight needs specific approval | **Certain — regulatory, not technical** | Green-zone ceiling is 120 m AGL and we fly 30–100 m, so altitude is compliant. Scouts stay inside the mothership's relay bubble and the operator's visual envelope; deployment path is state disaster-agency authorisation, the same route NDRF assets already fly under. *Wording to be verified against current Digital Sky text — `DATA.md` §8* |
| 4 | **VIO fails in fog, dust and featureless scenes** — exactly the conditions of a fresh landslide | Medium-high | Triple redundancy: PMW3901 optical flow + TFMini-S LiDAR altitude hold + IMU dead-reckoning, with a hard rule that a scout losing pose holds altitude and climbs to reacquire GNSS rather than continuing blind |
| 5 | **On-device inference throughput is currently an estimate** (30–45 FPS for YOLOv8n INT8 on QCS6490) | Medium | **Qualcomm AI Hub profiles models on real Snapdragon hardware for free.** Every inference number in this deck becomes a measured number before the finale, without us owning the board |
| 6 | **The swarm is not the cheapest option per km² — a single scout is** (₹430 vs ₹502) | Certain — it is arithmetic | Stated openly. The swarm is bought for **time**, not cost: 5.8 hours against 25 for one scout on a Wayanad-sized zone. Cost-effectiveness against the *deployed alternative* is the real comparison, and there it is 27× |
| 7 | **Six aircraft, two operators, one radio band** | Medium | Detections travel as JSON, never video — a marker is a few hundred bytes, so the mesh is never the bottleneck. Scouts fly pre-planned lanes autonomously; operators supervise and re-task, they do not pilot |

---

## 30-second script

> "The whole system is two-point-seven lakh — eighty-six minutes of helicopter charter, and every
> price is from an Indian vendor. Now the honest part. A single scout is *cheaper* per square
> kilometre than the swarm; the mothership is overhead. We're not buying cheapness, we're buying
> time. And a helicopter actually sweeps five times more area per hour than we do — it just costs
> twenty-seven times more per square kilometre, can't fly at night, takes hours to position, and puts
> one pair of human eyes at three hundred metres on a problem where a person is twenty arcminutes
> wide. The real risks are daylight thermal inversion, false positives, and BVLOS permission — all
> three are on the slide with what we do about them. And when links drop or scouts are lost, the
> lanes widen and the mission gets slower. It doesn't stop.
>
> Last thing — who buys it. NDRF has sixteen battalions for seven hundred and thirty-eight districts,
> so NDRF is always arriving; at Wayanad a team was dispatched from Bengaluru. The DDMA is mandated in
> every district by law and is already there. So this is a district asset. And the money exists: the
> Finance Commission has sixteen thousand crore earmarked for preparedness and capacity-building
> through 2026. One system in every district in India is nineteen point eight six crore — nought
> point one two percent of that line. North-eastern and Himalayan states pay a tenth, so it's
> twenty-seven thousand rupees to a state per district. And disaster management is CSR-eligible under
> Schedule VII, which means Qualcomm could fund this out of its own CSR budget."
