#!/usr/bin/env python3
"""Kalp şeklinde QR kod üretici.

Kullanım: python3 tools/kalp-qr.py https://site-adresin -o kalp-qr.png -t "Defne için"
Gerekenler: pip install qrcode pillow
"""
import sys, random, math
import qrcode
from PIL import Image, ImageDraw, ImageFont

import argparse
ap = argparse.ArgumentParser(description="Kalp şeklinde, okunabilir bir QR kod üretir.")
ap.add_argument("url", help="QR kodun açacağı adres")
ap.add_argument("-o", "--out", default="kalp-qr.png", help="çıktı dosyası (PNG)")
ap.add_argument("-t", "--text", default="", help="kalbin altına yazılacak kısa yazı")
ap.add_argument("--gap", type=int, default=1, help="QR ile kalp kulakları arasındaki boşluk (modül)")
args = ap.parse_args()
URL, OUT, GAP = args.url, args.out, args.gap
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=0)
qr.add_data(URL); qr.make(fit=True)
M = qr.get_matrix(); N = len(M)
R = N / 2
rnd = random.Random(1101)

cells = set()
for v in range(N):
    for u in range(N):
        if M[v][u]: cells.add((u, v))
# Kulaklar: kalbin üst kenarlarına yarım daireler (aynı modül ızgarasında)
for v in range(-N, N):
    for u in range(-N, N):
        cu, cv = u + .5, v + .5
        top = cv < -GAP and (cu - R) ** 2 + cv ** 2 <= R * R and 0 <= cu <= N
        left = cu < -GAP and cu ** 2 + (cv - R) ** 2 <= R * R and 0 <= cv <= N
        if (top or left) and rnd.random() < 0.5:
            cells.add((u, v))

S = 34                      # modül boyu (px)
k = S / math.sqrt(2)
def P(u, v): return ((u - v) * k, (u + v) * k)
pts = [P(u + a, v + b) for (u, v) in cells for a in (0, 1) for b in (0, 1)]
minx = min(p[0] for p in pts); maxx = max(p[0] for p in pts)
miny = min(p[1] for p in pts); maxy = max(p[1] for p in pts)
MARGIN = 140
W = int(maxx - minx + 2 * MARGIN); H = int(maxy - miny + 2 * MARGIN + (140 if args.text else 0))
pink = (214, 51, 108); bg = (255, 246, 250)
img = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(img)
ox, oy = MARGIN - minx, MARGIN - miny
for (u, v) in cells:
    poly = [P(u, v), P(u + 1, v), P(u + 1, v + 1), P(u, v + 1)]
    d.polygon([(x + ox, y + oy) for x, y in poly], fill=pink)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold Italic.ttf", 84)
except Exception:
    font = ImageFont.load_default()
if args.text:
    tw = d.textlength(args.text, font=font)
    d.text(((W - tw) / 2, maxy + oy + 50), args.text, font=font, fill=pink)
img.save(OUT); print("N", N, "size", img.size)
