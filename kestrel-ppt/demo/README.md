# demo/ — the live public link, and the algorithms that are ours

**Live:** https://huggingface.co/spaces/anshumanatrey/kestrel-survivor-detection
Public, no login, no server. YOLOv8n and all four algorithms run **in the judge's browser**
via ONNX Runtime Web — which is itself a demonstration of the PS's *"on-device AI inference
without dependence on cloud connectivity"* bullet.

## Why this exists

Software teams put a live URL on their slide. We are Hardware category, so this is the
equivalent — and it answers the harder question: *what in this project is yours, not YOLO's?*

Stock YOLOv8n gives boxes. `kestrel.js` is everything that turns boxes into a search decision.

| Algorithm | Structure | Complexity | Grounded in |
|---|---|---|---|
| **Two-pass descent** | greedy min-window-cover · spatial hash · union-find · weighted box fusion | O(n log n) plan, O(n α(n)) merge | SAHI, arXiv 2202.06934 (+6.8% AP on VisDrone) · WBF, arXiv 1910.13302 |
| **Correlated fusion** | sparse `Map` on packed int keys · adaptive-ridge Gauss-Jordan | O(1)/update, O(k³) k≤8 | generalises Chair-Varshney 1986; inverse-covariance weighting |
| **Route planning** | prize-collecting bitmask DP | O(2^k·k²), k≤15 | Held-Karp, with return-to-base as a hard DP constraint |
| **Link budget** | 1-D rolling knapsack + choice table | O(n·B) | 0/1 knapsack over `DATA.md` §23 record sizes |

## Correctness

`selfTest()` — **9/9**, runnable from the page. The route planner is checked against exhaustive
permutation search and the knapsack against exhaustive subset enumeration. The fusion rule is
asserted to collapse to classical Chair-Varshney when the correlation matrix is the identity,
so we generalise the published rule rather than contradicting it.

**Two real bugs the integration test caught, both fixed:**
1. Raw GLS returned a **negative** weight for a near-collinear stream — it wanted to *subtract*
   redundant thermal. Correct for minimum-variance estimation, meaningless as evidence. Fixed
   with the smallest Tikhonov ridge that keeps every weight non-negative; λ=0 is tried first so
   the Chair-Varshney reduction still holds exactly.
2. `(v << 16)` **overflows int32** once v > 32767 and JS sign-extends on `>>`, so every positive
   grid coordinate decoded to garbage and the route planner reported nothing reachable. Packing
   is now plain arithmetic, exact to 2^53.

## Honest limits

- Weights are **stock COCO**. The algorithms are the contribution; fine-tuning on aerial SAR
  imagery is `DATA.md` §26's open item and needs a GPU we have not spent yet.
- Thermal and BLE streams are **slider-driven**. RGB and the descent pass are computed from the
  uploaded image. The page says so.
- The browser is not a Hexagon NPU. The Qualcomm table on the page is from AI Hub on real
  devices; the page is the pipeline. Stated on the page, not buried.
