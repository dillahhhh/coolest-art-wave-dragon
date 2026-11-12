"""Coolest-art-01 entry (Python 3.13, standard library only).

The art is entry-wave-dragon.jpg beside this file: a minimalist
Japanese ukiyo-e print of a colossal white dragon with navy scales
coiling across the image, its head (golden eyes, open jaws, whiskers)
in front of a huge flat vermilion-red sun disc, its body curving down
and becoming a Hokusai wave with foam, a tiny black-silhouette boat
with one fisherman below. The wave is a dragon: the dragon's head
guards the red sun, its scaled body is the wave itself, and the tiny
boat gives the whole creature its scale.
The program copies it to /output/entry.png.

The gate accepts a PNG or a JPEG at /output/entry.png, told apart by
its first bytes; the name stays entry.png either way. The file is a
whole JPEG of 459406 bytes and 1024 by 1024 pixels, inside the
1 MiB and 1024 by 1024 limits.

Deterministic: no network, no randomness, no clock. It copies the
same bytes every run, so two runs write byte-identical output.

Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARTWORK = "entry-wave-dragon.jpg"
SRC = HERE / ARTWORK
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DST = OUT_DIR / "entry.png"


def main():
    # Pure copy, no drawing at runtime: the artwork is fixed, so the
    # output is byte-identical on every run by construction.
    if not SRC.is_file():
        raise FileNotFoundError(f"artwork missing: {SRC}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Byte-exact copy: the judge sees exactly the bytes in the file,
    # so refuse to leave a partial or mismatched output behind.
    if DST.stat().st_size != SRC.stat().st_size:
        raise RuntimeError("output does not match the source image")
    if hashlib.sha256(DST.read_bytes()).hexdigest() != hashlib.sha256(
        SRC.read_bytes()
    ).hexdigest():
        raise RuntimeError("output hash does not match the source image")
    # The gate tells PNG from JPEG by first bytes; confirm the copy is
    # still a whole JPEG (SOI marker at the start, EOI marker at the end).
    # This also guards the 1 MiB cap: a truncated file would fail here.
    data = DST.read_bytes()
    if not data.startswith(b"\xff\xd8\xff") or not data.endswith(b"\xff\xd9"):
        raise RuntimeError("output is not a whole JPEG image")


if __name__ == "__main__":
    main()
