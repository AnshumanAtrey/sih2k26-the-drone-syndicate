#!/usr/bin/env python3
"""Erase the four orange reticle ticks (fixed corner squares) and trim the white
margin so each diagram fills more of its slide box. Reads img/raw/*.png -> img/*.png."""
from PIL import Image
import numpy as np, glob, os

CORNER = 74      # px square at each corner to whiten (covers the ~40px tick + inset)
PAD    = 6       # px of white kept around the trimmed content
THRESH = 245     # a pixel is "content" if any channel is below this

for f in sorted(glob.glob('img/raw/*.png')):
    im = Image.open(f).convert('RGB')
    a = np.asarray(im).copy()
    H, W, _ = a.shape
    for ys, ye, xs, xe in [(0, CORNER, 0, CORNER), (0, CORNER, W-CORNER, W),
                           (H-CORNER, H, 0, CORNER), (H-CORNER, H, W-CORNER, W)]:
        a[ys:ye, xs:xe] = 255
    mask = a.min(axis=2) < THRESH
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    if len(rows) and len(cols):
        y0, y1 = max(0, rows[0]-PAD), min(H-1, rows[-1]+PAD)
        x0, x1 = max(0, cols[0]-PAD), min(W-1, cols[-1]+PAD)
        a = a[y0:y1+1, x0:x1+1]
    out = f.replace('/raw/', '/')
    Image.fromarray(a).save(out)
    print(os.path.basename(out), '->', f'{a.shape[1]}x{a.shape[0]}  ({a.shape[1]/a.shape[0]:.2f})')
