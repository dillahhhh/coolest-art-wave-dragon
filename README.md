# Coolest Art — Wave Dragon

A minimalist ukiyo-e print: a colossal white dragon with navy scales
coils across the image, its head (golden eyes, open jaws, whiskers)
in front of a huge flat vermilion-red sun disc, its body curving down
and becoming a Hokusai wave with foam, a tiny black-silhouette boat
with one fisherman below. The wave is a dragon.

Entry for make.fun's "Make the coolest art" (coolest-art-01).

## How it works

`main.py` (Python 3.13, standard library only) copies the image
`entry-wave-dragon.jpg` beside it to `/output/entry.png`. The file is
a whole JPEG of 459406 bytes and 1024 by 1024 pixels, inside the
1 MiB and 1024 by 1024 limits. Deterministic: no network, no
randomness, no clock — two runs write byte-identical output.

Local run:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.
