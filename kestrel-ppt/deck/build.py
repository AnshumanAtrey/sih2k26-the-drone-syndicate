#!/usr/bin/env python3
"""Build the SIH 2026 idea deck. Absolute inch geometry so overlap is checkable."""
import html, json, pathlib

W, H = 13.333, 7.5
M      = 0.28           # side margin
TITLE_H= 0.84           # official template title band
BAR_Y, BAR_H = 7.10, 0.40
KEY_Y, KEY_H = 0.88, 0.26
R1_LAB, R1_Y, R1_H = 1.16, 1.34, 3.38
R2_LAB, R2_Y = 4.86, 5.04
R2_H   = 7.00 - R2_Y
CW     = W - 2*M
GAP    = 0.16
COL    = (CW - GAP) / 2                       # 6.2865 in
boxes  = []                                    # for the overlap checker
SLIDE  = [0]                                   # current slide index, for the checker

def px(v): return f"{v:.4f}in"

def el(cls, x, y, w, h, inner="", style="", tag="div", track=True):
    if track: boxes.append(dict(slide=SLIDE[0], cls=cls, x=x, y=y, w=w, h=h))
    return (f'<{tag} class="ab {cls}" style="left:{px(x)};top:{px(y)};'
            f'width:{px(w)};height:{px(h)};{style}">{inner}</{tag}>')

def img(src, x, y, w, h, fit="contain"):
    return el("im", x, y, w, h,
              f'<img src="{src}" style="width:100%;height:100%;object-fit:{fit}">')

def lab(t, x, y, w):
    return el("lab", x, y, w, 0.16, html.escape(t))

def slide(title, body, n):
    return f'''<section class="s">
  <div class="oval">Drone<br>Syndicate</div>
  <img class="slogo" src="img/sih-logo.png">
  <div class="tb"><h1>{html.escape(title)}</h1></div>
  {body}
  <div class="bar"></div>
  <div class="ft">@SIH Idea submission · PS 26177 · Qualcomm Inc · Hardware · Robotics &amp; Drones · <b>Drone Syndicate</b></div>
  <div class="pg">{n}</div>
</section>'''

def bullets(items):
    return "".join(f'<p><b>{html.escape(h)}</b> {b}</p>' for h, b in items)

def chips(groups):
    """Visible tech-stack strip. Every winning hardware deck shows the stack as
    blocks, never buried in prose."""
    out = []
    for head, items in groups:
        out.append(f'<div class="cg"><em>{html.escape(head)}</em>'
                   + "".join(f'<span>{i}</span>' for i in items) + '</div>')
    return '<div class="chips">' + "".join(out) + '</div>'

S = []

# ---------------------------------------------------------------- 1 TITLE
S.append(f'''<section class="s title">
  <img class="tlogo" src="img/sih-logo.png">
  <img class="tmark" src="img/sih-mark.png">
  <h1 class="tev">SMART INDIA HACKATHON 2026</h1>
  <div class="tsub">TITLE PAGE</div>
  <ul class="tlist">
    <li><b>Problem Statement ID</b> &ndash; 26177</li>
    <li><b>Problem Statement Title</b> &ndash; A deployable AI-powered autonomous drone that aids
        search-and-rescue operations by detecting people and hazards, thereby improving responder
        safety and reducing victim discovery time.</li>
    <li><b>Theme</b> &ndash; Robotics and Drones</li>
    <li><b>PS Category</b> &ndash; Hardware</li>
    <li><b>Team ID</b> &ndash; </li>
    <li><b>Team Name</b> &ndash; Drone Syndicate</li>
  </ul>
</section>''')

# ---------------------------------------------------------------- 2 SOLUTION
SLIDE[0]=2
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>At Wayanad, 206 people were never found. Not because nobody looked. It was because 1,300 responders could not cover 15 km&sup2; before the window closed.</b>")
b += lab("① ONE AIRCRAFT · COMPLETE WITH THE TRUCK SWITCHED OFF", M, R1_LAB, COL)
b += lab("② SIX OF THEM · 15 km² SWEPT IN 5.8 HOURS", M+COL+GAP, R1_LAB, COL)
b += img("img/s1-one-drone.png", M, R1_Y, COL, R1_H)
b += img("img/c4-swarm.jpg",     M+COL+GAP, R1_Y, COL, R1_H, "cover")
IW = R2_H*1.778
IW2 = IW                                  # two half-width panels on row 2
b += lab("③ ONE AIRCRAFT, THREE PAYLOADS", M, R2_LAB, IW2)
b += lab("④ THE IDEA NOBODY HAS USED", M+IW2+GAP, R2_LAB, IW2)
b += el("shead", M+2*(IW2+GAP), R2_LAB-0.03, CW-2*(IW2+GAP), 0.20,
        "&#10022; <u>Proposed Solution</u> (Describe your Idea/Solution/Prototype)")
b += img("img/f3-payload.png", M, R2_Y, IW2, R2_H)
b += img("img/f1-sachet.png",  M+IW2+GAP, R2_Y, IW2, R2_H)
b += el("tx", M+2*(IW2+GAP), R2_Y, CW-2*(IW2+GAP), R2_H, bullets([
  ("Detailed explanation:",
   "One scout is an <b>Arduino UNO Q</b> (Qualcomm Dragonwing QRB2210 + real-time STM32U585) "
   "carrying RGB, thermal and its own Wi-Fi/BLE radio. PX4 flies on the MCU at 1 kHz; detection, "
   "odometry and the decision tree run on Linux. <b>It is not only a swarm.</b> A single aircraft "
   "also carries swappable payloads: breadcrumb radios, acoustic and CO&#8322; pods, a tethered "
   "crawler. The truck is an accelerator, never a dependency."),
  ("How it addresses the problem:",
   "Wayanad 2024: 1,300 responders, 6 zones, <b>5+ days</b>, 206 never found. One scout sweeps "
   "0.43 km&sup2;/h alone; six sweep the full 15 km&sup2; in <b>5.8 hours</b>, for "
   "<b>+64 survivors per 100 trapped</b>."),
  ("Innovation and uniqueness:",
   "<b>SACHET cell broadcast, inverted.</b> NDMA already reaches 1.43 bn handsets to say "
   "<i>evacuate</i>. One message saying <i>turn Bluetooth on</i> makes every phone a beacon, and "
   "the scout's own Qualcomm radio is already the receiver. <b>Zero added hardware.</b>"),
]))
S.append(slide("PROPOSED SOLUTION", b, 2))

# ---------------------------------------------------------------- 3 TECHNICAL
SLIDE[0]=3
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>Detection is off-the-shelf. The decision layer is ours, and it is measured on Qualcomm silicon.</b>")
b += lab("① HOW ONE AIRCRAFT DECIDES · 1 Hz, DETERMINISTIC", M, R1_LAB, COL)
b += lab("② WHAT ACTUALLY REACHES A BURIED PERSON", M+COL+GAP, R1_LAB, COL)
b += img("img/s2-loop.png",   M, R1_Y, COL, R1_H)
b += img("img/f2-buried.png", M+COL+GAP, R1_Y, COL, R1_H)
QW = 1.02
b += lab("RUNS IN THE JUDGE'S BROWSER", M, R2_LAB, QW*2)
b += el("shead", M+QW*2+GAP, R2_LAB-0.03, CW-QW*2-GAP, 0.20, "&#10022; <u>Technical Approach</u>")
b += img("img/qr-demo.png", M, R2_Y, QW, QW)
b += el("qc", M, R2_Y+QW+0.03, QW*2, 0.30,
        "<b>Live demo</b><br>hf.co/spaces/anshumanatrey/<br>kestrel-survivor-detection")
TX = M+QW*2+GAP; TXW = CW-QW*2-GAP
b += el("chipbar", TX, R2_Y, TXW, 0.50, chips([
  ("SILICON",   ["Dragonwing QRB2210", "QCS6490", "IQ-8275", "STM32U585"]),
  ("AI",        ["YOLOv8n INT8", "Qualcomm AI Hub", "QNN", "MobileCLIP"]),
  ("FLIGHT",    ["PX4", "ROS 2", "VINS-Fusion VIO"]),
  ("RADIO",     ["Wi-Fi 5", "BT 5.1", "LoRa SX1262", "breadcrumb relays"]),
]))
b += el("tx", TX, R2_Y+0.56, TXW, R2_H-0.56, bullets([
  ("Methodology:",
   "<b>Four algorithms, not a wrapper.</b> <b>(1)</b> two-pass descent, SAHI-style, with min-window-cover crop planning, union-find "
   "cross-pass merging and weighted box fusion · <b>(2)</b> correlated Bayesian fusion solving "
   "<b>Σw = 1</b>, which discounts sensors that fail together and reduces to Chair-Varshney when "
   "they do not · <b>(3)</b> prize-collecting <b>Held-Karp</b> route DP, exact, battery reserve "
   "inside the DP · <b>(4)</b> 0/1 knapsack for the LoRa frame. <b>9/9 self-tests against brute force.</b>"),
  ("Measured, not estimated:",
   "YOLOv8n INT8 @640 on <b>Qualcomm AI Hub, real devices</b>: Arduino Ventuno Q (IQ-8275) "
   "<b>1.85 ms / 539 FPS</b>; Dragonwing RB3 Gen 2 (QCS6490) <b>11.21 ms / 89 FPS</b>. "
   "<b>247 of 247 layers on the Hexagon NPU, zero CPU fallback.</b> The sweep needs 0.22 Hz, so "
   "the headroom runs detection, VIO and the radio scanner at once."),
]))
S.append(slide("TECHNICAL APPROACH", b, 3))

# ---------------------------------------------------------------- 4 FEASIBILITY
SLIDE[0]=4
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>We built four architectures, scored them against our own criteria, and shipped the one that survives losing pieces.</b>")
b += lab("① THE ALTERNATIVES WE TESTED · AND WHY OURS WON", M, R1_LAB, COL)
b += lab("② WHAT IT COSTS AGAINST THE ALTERNATIVE", M+COL+GAP, R1_LAB, COL)
b += img("img/r3-alternatives.png", M, R1_Y, COL, R1_H)
b += img("img/f4-cost.png",         M+COL+GAP, R1_Y, COL, R1_H)
b += lab("③ WHEN PIECES FAIL", M, R2_LAB, IW)
b += el("shead", M+IW+GAP, R2_LAB-0.03, CW-IW-GAP, 0.20, "&#10022; <u>Feasibility and Viability</u>")
b += img("img/f5-degrade.png", M, R2_Y, IW, R2_H)
b += el("tx", M+IW+GAP, R2_Y, CW-IW-GAP, R2_H, bullets([
  ("Feasibility:",
   "<b>₹2.68 lakh</b> total, Indian-vendor sourced (Robu / Robocraze / Thundercomm). That is "
   "<b>86 minutes</b> of charter helicopter. Airframe, flight stack and radios are all commodity; "
   "the detector is already profiled on real Qualcomm hardware."),
  ("Potential challenges and risks:",
   "Thermal <b>inverts</b> on sun-heated rubble in daylight · VIO drifts ~0.5% of path, which is "
   "21 m over a full sortie · FINDER-class radar <b>reported three breath signals at Wayanad where "
   "nothing was found</b> · a 500 mm airframe cannot enter a collapsed doorway."),
  ("Strategies for overcoming them:",
   "Independence weighting means <b>no single stream ever decides</b>. The radar that lied is one "
   "weighted vote · GPS-denied excursions are bounded to 1–3 min by breadcrumb anchors and loop "
   "closure at the truck, giving <b>1.2–3.6 m</b>, inside the re-inspect radius · interiors are "
   "reached by <b>dropped breadcrumb pods</b>, not by flying the sweep frame indoors · and the "
   "degradation ladder is designed so the system gets <b>slower, never offline</b>."),
]))
S.append(slide("FEASIBILITY AND VIABILITY", b, 4))

# ---------------------------------------------------------------- 5 IMPACT
SLIDE[0]=5
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>The 72-hour window is the entire problem. We move first contact from day three to hour six.</b>")
b += lab("① OUT OF 100 TRAPPED PEOPLE, HOW MANY ARE STILL ALIVE", M, R1_LAB, COL)
b += lab("② WHAT THE COMMANDER SEES · ON-DEVICE, NO NETWORK", M+COL+GAP, R1_LAB, COL)
b += img("img/r1-survival.png",  M, R1_Y, COL, R1_H)
b += img("img/p5-dashboard.jpg", M+COL+GAP, R1_Y, COL, R1_H, "cover")
b += lab("③ WHAT IT IS ALL FOR", M, R2_LAB, IW)
b += el("shead", M+IW+GAP, R2_LAB-0.03, CW-IW-GAP, 0.20, "&#10022; <u>Impact and Benefits</u>")
b += img("img/c6-void.jpg", M, R2_Y, IW, R2_H, "cover")
b += el("tx", M+IW+GAP, R2_Y, CW-IW-GAP, R2_H, bullets([
  ("Impact on the target audience:",
   "NDRF, SDRF and the Army search at roughly 0.1 km²/h per team. Kestrel sweeps <b>2.6 km²/h</b>. "
   "On the Wayanad footprint that is <b>5.8 hours instead of five days</b>: <b>99 alive per 100</b> "
   "at six hours against <b>35 at seventy-two</b>."),
  ("Social:",
   "Responders stop walking unstable debris and live power lines to find out whether anyone is there. "
   "The aircraft takes that risk, and it takes it at night, in monsoon, without fatigue."),
  ("Economic:",
   "<b>₹502 per km²</b> against <b>₹13,800</b> by charter helicopter, <b>27×</b>. Equipping all "
   "<b>738 districts</b> costs ≈ <b>₹19.86 Cr</b>, which is <b>0.12%</b> of the national disaster "
   "preparedness line. It is already funded; it is a procurement decision, not a budget request."),
  ("Environmental:",
   "Battery-electric, no fuel burn, and the scout's brain is a ₹5,190 board rather than a ₹50,000 one."),
]))
S.append(slide("IMPACT AND BENEFITS", b, 5))

# ---------------------------------------------------------------- 6 REFERENCES
SLIDE[0]=6
RC = (CW - GAP*2) / 3
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>Every number in this deck traces to a source. Every claim about our own silicon is a job ID you can open.</b>")
refs = [
 ("Peer-reviewed &amp; field evidence", [
  "Team <b>CERBERUS</b>, winner, DARPA Subterranean Challenge 2021: base-station compute + breadcrumbed radio nodes",
  "Zhejiang Univ., <i>Swarm of micro flying robots in the wild</i>, <b>Science Robotics 2022</b>: decentralised, no central aircraft",
  "Akyon et al., <b>SAHI</b>, <a href='https://arxiv.org/abs/2202.06934'>arXiv <b>2202.06934</b></a>: slicing raises AP <b>+6.8%</b> on VisDrone with no retraining",
  "Solovyev et al., <b>Weighted Boxes Fusion</b>, <a href='https://arxiv.org/abs/1910.13302'>arXiv 1910.13302</a>",
  "<b>Chair &amp; Varshney</b>, IEEE TAES 1986: optimal LLR decision fusion; we generalise it to correlated streams",
  "<i>Sensors</i> <b>18(3) 852</b>: CO₂ + thermal + microphone fusion for trapped-victim detection",
  "NASA JPL / DHS <b>FINDER</b>: 9 m rubble penetration; four men found alive, Nepal 2015",
  "<b>ACHORD</b> / CARA (JPL CoSTAR): communication-aware coordination with droppable radios",
  "Held &amp; Karp, <i>J. SIAM</i> 1962: exact DP for the sequencing problem we solve per sortie",
  "UAV-VLRR <a href='https://arxiv.org/abs/2503.02465'>arXiv 2503.02465</a> · <b>AVERY</b> <a href='https://arxiv.org/abs/2511.18151'>arXiv 2511.18151</a>: VLM split computing for disaster response",
 ]),
 ("Indian operational &amp; policy record", [
  "<b>Wayanad landslide</b>, 30 Jul 2024: 1,300 personnel, 40 teams, 6 zones, 5+ days, 357 dead, <b>206 missing</b>, ~15 km²",
  "<a href='https://sachet.ndma.gov.in/'><b>C-DOT SACHET</b></a> / NDMA cell broadcast: 1.43 bn citizens, 36 states, 14.5 M tower cells",
  "<b>15th Finance Commission</b> 2021–26: NDRF/SDRF preparedness allocation",
  "<b>DGCA</b> UAS Rules 2021 · Drone Rules amendment: micro/small category, RPC training",
  "<a href='https://keralarescue.in/'><b>keralarescue.in</b></a>, Kerala 2018: crowd-sourced rescue requests, IEEE Kerala + Kerala IT Mission",
  "<b>Nepal–Tibet glacial flood</b>, Aug–Sep 2026 · <b>Assam floods</b>, Jul–Aug 2026: the live monsoon record",
  "<b>NDMA</b> / NDRF deployment doctrine: 40 teams across 6 zones is the Wayanad baseline we measure against",
  "<b>IAMSAR</b> sweep-width methodology: the ground-team rate our 0.1 km²/h figure derives from",
  "<b>ISRO Bhuvan</b> · Copernicus <b>Sentinel-1 SAR</b>: free pre-flight damage priors",
 ]),
 ("Qualcomm platform &amp; our own measurements", [
  "<a href='https://aihub.qualcomm.com/'><b>Qualcomm AI Hub</b></a>: YOLOv8n INT8 @640, QNN DLC, <code>--quantize_io</code>, profiled on physical devices",
  "Arduino <b>Ventuno Q</b> (Dragonwing IQ-8275, Hexagon v75): <b>1.85 ms · 539 FPS · 247/247 NPU</b>",
  "Dragonwing <b>RB3 Gen 2</b> (QCS6490, Hexagon v68): <b>11.21 ms · 89 FPS · 247/247 NPU</b>",
  "Arduino <b>UNO Q</b>: QRB2210 + STM32U585, Wi-Fi 5 + BT 5.1, ₹5,190 (4 GB / 32 GB)",
  "<a href='https://px4.io/'><b>PX4 / ROS 2 / VINS-Fusion</b></a>: open flight and odometry stack",
  "<i>Third-party</i>: Foundries.io measured YOLOv5 Pico at <b>~17 FPS</b> on a physical UNO Q",
  "<b>SARD</b> search-and-rescue aerial dataset: 1,980 images, 6,525 person instances, fine-tune in progress",
  "<b>ONNX Runtime Web</b>: the demo executes in the judge's browser, no server and no upload",
  "<i>Honest limit</i>: <b>QRB2210 is not offered on AI Hub</b>, so the scout figure stays third-party",
 ]),
]
for i, (h_, items) in enumerate(refs):
    x = M + i*(RC+GAP)
    b += lab(h_.replace("&amp;","&"), x, R1_LAB, RC)
    b += el("rf", x, R1_Y + 0.02, RC, 2.66,
            "".join(f"<p>{t}</p>" for t in items))
QY = 4.09
b += el("tx qrrow", M, QY, CW, 0.98, f'''
  <div class="qrs">
    <div><img src="img/qr-demo.png"><div><b>Live demo · runs in your browser</b><br>
      Two-pass descent, correlated fusion, Held-Karp routing and the knapsack link budget,
      executing on <i>your</i> device. No server, no login.<br>
      <a href='https://huggingface.co/spaces/anshumanatrey/kestrel-survivor-detection'>huggingface.co/spaces/anshumanatrey/kestrel-survivor-detection</a></div></div>
    <div><img src="img/qr-repo.png"><div><b>Engineering record</b><br>
      Sourced data registry, BOM, every prompt, and the algorithm module with its
      brute-force self-tests.<br>
      <a href='https://github.com/AnshumanAtrey/sih2k26-the-drone-syndicate'>github.com/AnshumanAtrey/sih2k26-the-drone-syndicate</a></div></div>
  </div>''')
b += lab("OUR OWN MEASUREMENTS · QUALCOMM AI HUB, PHYSICAL DEVICES, JOB IDS ON REQUEST", M, 5.12, CW)
b += el("tbl", M, 5.32, CW, 1.54, """
 <table>
  <tr><th>Device</th><th>Silicon</th><th>Precision</th><th>Latency</th><th>Throughput</th><th>Compute units</th><th>Peak memory</th></tr>
  <tr class="hi"><td>Arduino Ventuno Q</td><td>Dragonwing IQ-8275 · Hexagon v75</td><td>INT8</td>
      <td><b>1.85 ms</b></td><td><b>539.7 FPS</b></td><td><b>247 / 247 NPU</b></td><td>7.5 MB</td></tr>
  <tr><td>Dragonwing RB3 Gen 2</td><td>QCS6490 · Hexagon v68</td><td>INT8</td>
      <td>11.21 ms</td><td>89.2 FPS</td><td>247 / 247 NPU</td><td>9.1 MB</td></tr>
  <tr><td>Arduino Ventuno Q</td><td>Dragonwing IQ-8275 · Hexagon v75</td><td>fp16</td>
      <td>6.77 ms</td><td>147.8 FPS</td><td>247 / 247 NPU</td><td>16.5 MB</td></tr>
  <tr class="mu"><td>Dragonwing RB3 Gen 2</td><td>QCS6490 · Hexagon v68</td><td>fp16</td>
      <td colspan="4">graph will not compose on Hexagon v68: reported as a negative result, not omitted</td></tr>
 </table>""")
S.append(slide("RESEARCH AND REFERENCES", b, 6))

CSS = """
@page{size:13.333in 7.5in;margin:0}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;padding:0;background:#fff;
 font-family:Arial,Helvetica,"Segoe UI",sans-serif;color:#15233b}
.s{position:relative;width:13.333in;height:7.5in;overflow:hidden;background:#fff;
 page-break-after:always;break-after:page}
.s:last-child{page-break-after:auto}
.tb{left:1.72in;top:0;width:9.9in;height:.84in;display:flex;align-items:center;
 justify-content:center}
.tb h1{font-family:"Times New Roman",Times,serif;font-weight:700;font-size:30pt;margin:0;
 letter-spacing:.005em;color:#0f2038;text-align:center}
.oval{left:.26in;top:.09in;width:1.3in;height:.66in;border:.014in solid #8A87C4;
 border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;
 font-size:8.4pt;font-weight:700;line-height:1.14;color:#0f2038}
.slogo{left:11.72in;top:.1in;width:1.34in}
.bar{left:0;top:7.10in;width:13.333in;height:.40in;background:#0070C0}
.ft{left:.3in;top:7.185in;font-size:8pt;color:#fff;letter-spacing:.02em}
.pg{right:.32in;top:7.17in;font-size:11pt;color:#fff;font-weight:700}
.ab,.tb,.bar,.ft,.pg,.oval,.slogo{position:absolute}
.key{font-size:11.2pt;line-height:1.2;color:#0070C0;display:flex;align-items:center;
 border-left:.035in solid #0070C0;padding-left:.11in}
.shead{font-size:9pt;font-weight:700;color:#1F497D;letter-spacing:.005em;
 overflow:hidden;white-space:nowrap}
.lab{font-size:7.3pt;font-weight:700;letter-spacing:.055em;color:#5b6b83;
 text-transform:uppercase;overflow:hidden;white-space:nowrap}
.im{overflow:hidden;border:.008in solid #d6dde8;border-radius:.035in;background:#fff}
.im img{display:block}
.tx{overflow:hidden}
.tx p{margin:0 0 .058in;font-size:8.1pt;line-height:1.31;color:#25344d;
 padding-left:.125in;text-indent:-.125in}
.tx p::before{content:"▪  ";color:#0070C0;font-weight:700}
.tx p b{color:#0f2038}
.rf{overflow:hidden}
.rf p{margin:0 0 .052in;font-size:7.2pt;line-height:1.29;color:#25344d;
 padding-left:.1in;text-indent:-.1in}
.rf p::before{content:"▸ ";color:#0070C0;font-weight:700}
.qc{font-size:6.6pt;line-height:1.24;color:#5b6b83;text-align:center}
.chipbar{overflow:hidden}
.chips{display:flex;gap:.17in;flex-wrap:wrap}
.cg{display:flex;align-items:center;gap:.05in}
.cg em{font-style:normal;font-size:6.3pt;font-weight:700;letter-spacing:.07em;color:#7c8aa0;
 margin-right:.02in}
.cg span{font-size:7pt;font-weight:600;color:#0f2038;background:#eef4fa;
 border:.006in solid #cfe0ef;border-radius:.03in;padding:.026in .06in;white-space:nowrap}
.qrs{display:flex;gap:.34in;height:100%}
.qrs>div{display:flex;gap:.13in;flex:1;align-items:flex-start}
.qrs img{width:.95in;height:.95in;flex:none}
.qrs>div>div{font-size:7.6pt;line-height:1.3;color:#25344d}
.qrs a{font-size:6.8pt;color:#0070C0;word-break:break-all;text-decoration:underline;
 font-family:ui-monospace,Menlo,monospace}
a{color:#0070C0;text-decoration:underline}
.tbl table{border-collapse:collapse;width:100%}
.tbl th{font-size:6.6pt;text-transform:uppercase;letter-spacing:.05em;color:#7c8aa0;
 text-align:left;padding:.028in .07in;border-bottom:.012in solid #0070C0;font-weight:700}
.tbl td{font-size:7.4pt;padding:.036in .07in;border-bottom:.006in solid #e3e8ef;color:#25344d}
.tbl tr.hi td{background:#eef6fc}
.tbl tr.mu td{color:#7c8aa0;font-style:italic}
/* ---- title slide: matched to the template's own layout ---- */
.title{display:block}
.tlogo{position:absolute;right:.42in;top:.30in;width:2.05in}
.tmark{position:absolute;right:1.15in;top:2.05in;width:3.55in;opacity:.95}
.tev{position:absolute;left:0;top:.34in;width:10.72in;text-align:center;margin:0;
 font-family:Garamond,"Times New Roman",Times,serif;font-size:40pt;font-weight:700;color:#1F497D}
.tsub{position:absolute;left:0;top:1.30in;width:10.72in;text-align:center;
 font-family:"Times New Roman",Times,serif;font-size:32pt;font-weight:700;color:#0f2038}
.tlist{position:absolute;left:.72in;top:2.30in;width:7.25in;margin:0;padding:0;list-style:none}
.tlist li{font-size:19pt;line-height:1.26;color:#111;margin-bottom:.155in;
 padding-left:.32in;text-indent:-.32in}
.tlist li::before{content:"•  ";font-weight:700}
.tlist b{font-weight:700}
"""
out = ("<!doctype html><html><head><meta charset='utf-8'><title>Kestrel · SIH 2026</title>"
       f"<style>{CSS}</style></head><body>" + "".join(S) + "</body></html>")
pathlib.Path("deck.html").write_text(out)
json.dump(boxes, open("boxes.json","w"), indent=1)
print(f"deck.html written · {len(S)} slides · {len(boxes)} tracked boxes")
