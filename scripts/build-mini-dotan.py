#!/usr/bin/env python3
"""Export transparent README loops from Mini Dotan's original website sprites.

Usage: python scripts/build-mini-dotan.py /path/to/source-directory
Requires Pillow. Sources (not duplicated in this repository):
https://github.com/DotanVG/Dotan-Personal-Website/tree/main/public/pets/mini-dotan
Expected source files: spritesheet.webp and typing.webp.
"""
import sys
from pathlib import Path
from PIL import Image

source = Path(sys.argv[1])
out = Path(__file__).resolve().parents[1] / 'assets/profile'
atlas = Image.open(source / 'spritesheet.webp').convert('RGBA')
typing = Image.open(source / 'typing.webp').convert('RGBA')


def cell(image, row, column):
    return image.crop((column * 192, row * 208, (column + 1) * 192,
                       (row + 1) * 208)).resize((144, 156), Image.Resampling.LANCZOS)


def export(name, frames, durations):
    # One shared palette prevents color shimmer; index 255 stays transparent.
    strip = Image.new('RGB', (144 * len(frames), 156))
    for i, frame in enumerate(frames):
        strip.paste(frame.convert('RGB'), (i * 144, 0))
    palette = strip.quantize(colors=255)
    indexed = []
    for frame in frames:
        result = frame.convert('RGB').quantize(palette=palette, dither=Image.Dither.NONE)
        mask = frame.getchannel('A').point(lambda a: 255 if a < 128 else 0)
        result.paste(255, mask=mask)
        indexed.append(result)
    target = out / name
    indexed[0].save(target, save_all=True, append_images=indexed[1:],
                    duration=durations, loop=0, transparency=255,
                    disposal=2, optimize=False)
    with Image.open(target) as check:
        assert check.n_frames == len(frames)
        for i in range(check.n_frames):
            check.seek(i)
            assert check.convert('RGBA').getpixel((0, 0))[3] == 0
    print(f'{name}: {target.stat().st_size:,} bytes, {len(frames)} frames')


export('mini-dotan-greeting.gif',
       [cell(atlas, 0, i) for i in range(6)] +
       [cell(atlas, 3, i) for i in [0, 1, 2, 1, 2, 3]],
       [600, 110, 110, 140, 140, 320, 140, 200, 200, 200, 200, 1400])
export('mini-dotan-typing.gif', [cell(typing, 0, i) for i in range(6)],
       [350, 180, 180, 180, 180, 650])
