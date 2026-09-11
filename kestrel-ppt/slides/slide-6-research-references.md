# Slide 6 — Research and References

**Official section:** "Research and References"
Template sub-bullet, verbatim: *details / links of the reference and research work*

**Prompts: none.** This is a view slide — all native text. Do not generate a decorative background
band; it costs file size and legibility and buys nothing on a page whose only job is to be checkable.

---

## Why this page matters more than it looks

*"Clarity and details in the prescribed format"* is one of the nine named criteria. This page is where
a sceptical judge goes to test whether the numbers on the previous four pages are real. Every claim
in the deck traces to a line here, and two of them trace to arithmetic we show rather than assert.
Ground: flat `#0B1220`, two columns, Inter 10–11 pt in `#94A3B8`, numbered.

---

## Layout

```
┌───────────────────────────────────┬───────────────────────────┐
│  REFERENCES (1-12, numbered)      │  TEAM — 6 members         │
│  two-column flow if needed        │  roles + SPOC letter no.  │
│                                   ├───────────────────────────┤
│                                   │  WHAT WE MEASURED         │
│                                   │  OURSELVES (3 lines)      │
└───────────────────────────────────┴───────────────────────────┘
```

---

## References — native text, keep the numbering

**The problem**

1. Onmanorama live coverage, Wayanad landslide, 2 Aug 2024 — the three radar breath signals, the
   nil result at that location, the "frog or snake" assessment, the private thermal-drone survey
   returning zero human presence, and the 1,300 personnel / 40 teams / 6 zones figures.
   `onmanorama.com/news/kerala/2024/08/02/wayanad-landslide-mundakkai-chooralmala-bailey-bridge-search-rescue-death-toll-live.html`
2. NDRF, Government of India — official operation record, landslide in Wayanad, Kerala.
   `ndrf.gov.in/en/operations/landslide-wayanad-kerala`
3. Monsoon 2026 state tolls — Himachal Pradesh 261 deaths / ₹1,202 crore damage (2 Sep 2026);
   Assam 100 dead and 700,000 displaced; J&K, Kerala, Jharkhand, Nagaland.
   `thenewsmill.com` · `news.webindia123.com` · `npr.org/2026/08/10/g-s1-138015` · `aljazeera.com`
4. IPE Global–Esri India — extreme-weather event days (322 in 2024) and district vulnerability
   (85% of 738). Lok Sabha replies on hydro-meteorological mortality, 2024-25 series.
5. NDMA India — national vulnerability profile: 58.6% of land seismic-prone, 12% flood-prone,
   5,700 km of 7,520 km coastline cyclone-prone.

**Survival and search methodology**

6. USAR / disaster-medicine literature on entrapped-victim survival by extrication time; historical
   datasets Tangshan 1976 and Campania-Irpinia 1980 — via DOAJ, *Methods Used in Urban Search and
   Rescue*. **Selection bias noted:** early-window survival is flattered because the easiest victims
   are found first — which is itself an argument for searching faster.
7. Koester, Chiacchia, Twardy, Cooper, Frost & Robe — *Use of the Visual Range of Detection to
   Estimate Effective Sweep Width for Land Search and Rescue*, Wilderness & Environmental Medicine,
   2014. Source of the W = 1.1 × Rd low-visibility relation our ground-team baseline is built on.
8. IAMSAR Manual — search-rate planning as track spacing × speed; the basis of the 13.7 km²/h
   helicopter figure.

**Technology**

9. Qualcomm RB3 Gen 2 / QCS6490 — 12 TOPS Hexagon NPU, 6 GB, Linux, ₹50,000 in India.
   `thundercomm.com/product/qualcomm-rb3-gen-2` · `cnx-software.com/2024/04/15`
10. Qualcomm AI Hub and QNN / SNPE — on-device compilation to the Hexagon NPU, INT8 for HTP
    acceleration, and free profiling on real Snapdragon devices. Official YOLO→QNN export path.
    `github.com/quic/ai-hub-models` · `docs.ultralytics.com/integrations/qnn`
11. ModalAI VOXL 2 (Qualcomm QRB5165) — 15 TOPS, PX4 on the sensors DSP, 5G-ready, 16 g; the
    production path. `modalai.com/products/voxl-2` · `docs.px4.io` ModalAI VOXL 2
12. Measured edge benchmarks: YOLOv8 at 65+ FPS on a Snapdragon NPU vs 2 FPS on its CPU;
    Llama 3.2 3B Q4_K_M at 2.0 GB / 28.7 tok/s generate / 580 tok/s prefill. FLIR Lepton 3.5
    (160×120, NETD < 50 mK, $164) and MLX90640 (32×24) datasheets. PX4, ROS 2, MAVROS, ORB-SLAM3,
    VINS-Fusion. DGCA Drone Rules 2021 / Digital Sky — 120 m green-zone ceiling, BVLOS approval regime.

---

## Team block — fill from the college roster

- **6 members, all from the same college, at least one female member** — both mandatory under the
  SIH 2026 guidelines
- Roles to print: flight & avionics · edge AI / Qualcomm toolchain · perception & sensor fusion ·
  comms & mesh · dashboard & full-stack · mission ops & flight testing
- Internal-hackathon nomination reference + **SPOC authorisation letter number** (college letterhead,
  principal-signed, sealed)
- Up to 2 mentors may be added after shortlisting — optional, and only worth doing for someone with
  real UAV or edge-AI depth

---

## "What we measured ourselves" — three lines, and they earn the page

This block is the reason a judge believes the rest. Keep it.

1. **We recomputed the thermal sensor from ground-sample-distance maths and rejected our own first
   choice** — a 32×24 array puts a prone human at 10% of one pixel at 30 m. Working shown on Slide 3.
2. **Our ground-team baseline predicts the real operation.** 15 km² ÷ 0.1 km²/h = 150 search-hours
   ≈ 6 days of shift work, which is what Wayanad actually took. The model was not tuned to flatter us.
3. **We publish the number that argues against us.** A single scout costs ₹430/km²; the swarm costs
   ₹502. The base station is overhead. The swarm buys time, not cost.

---

## 30-second script

> "Every number in this deck traces to a line on this page — Onmanorama and NDRF for Wayanad,
> published sweep-width methodology for the ground baseline, IAMSAR for the helicopter, Qualcomm's
> own documentation and measured benchmarks for the silicon. Three things we worked out ourselves:
> we rejected our own first thermal sensor on the optics, our ground-search model reproduces how long
> Wayanad actually took, and we've printed the one figure that doesn't flatter us. Six of us, from
> [college], shortlisted through our internal hackathon. Thank you."
