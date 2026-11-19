"""Draw the GTA 6 meme (meme.png, 1024x1024) from the AI-generated West
Coast boardwalk scene in assets/scene.jpg (Venice Beach style, GTA-style
wanted chase: a pink lowrider convertible speeding away with a young man
driving and a young woman beside him, a police cruiser with flashing
lights chasing them, a police helicopter with a searchlight, and
pedestrians reacting to the chase — people scattering, a surfer dropping
his board, a skateboarder jumping aside, a cyclist swerving, a dog
running, a vendor ducking — pier, ocean, tall palms, golden hour) plus
make.fun's official ghost mark in assets/makefun-mark-1024.png (from
https://make.fun/press/). The captions keep the GTA 6 setting (Leonida);
the picture's look is West Coast on purpose.

Layout, classic top/bottom meme so it stays readable at 480 px:
- top black bar:    CALLED IN SICK / FOR GTA 6
- middle: Vice City sunset scene, with the make.fun ghost mark pasted over
  the sun, so the ghost IS the sun over Leonida (worked into the scene,
  not a corner sticker)
- bottom black bar: five gold wanted stars, then WANTED IN LEONIDA

Facts in the joke, all verified 2026-11-19/20: GTA VI launched 19 Nov 2026
on PS5 / Xbox Series X|S after a 13-year wait since GTA V (2013) and two
delays; launch-day sick days were a real news story (companies gave staff
the day off). The 13 years / 212 GB / $80 detail lives in the post text.

Run: python3 draw_meme.py  (writes meme.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SCENE = os.path.join(HERE, "assets", "scene.jpg")
MARK = os.path.join(HERE, "assets", "makefun-mark-1024.png")
OUT = os.path.join(HERE, "meme.png")

SIZE = 1024
BAR = 140          # top and bottom black bar height
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(px):
    return ImageFont.truetype(BOLD, px)


def centred(draw, y, text, fnt, fill, stroke=4):
    draw.text((SIZE // 2, y), text, font=fnt, fill=fill, anchor="ma",
              stroke_width=stroke, stroke_fill="black")


def main():
    scene = Image.open(SCENE).convert("RGB").resize((SIZE, SIZE - 2 * BAR))
    mark = Image.open(MARK).convert("RGBA")

    canvas = Image.new("RGB", (SIZE, SIZE), "black")
    canvas.paste(scene, (0, BAR))

    # The ghost mark becomes the sun: the scene's sun sits near the top
    # centre, so centre the disc just below it (clear of the top caption)
    # and let it cover the sun.
    sun_x, sun_y = 509, BAR + 110
    disc = 170
    mark = mark.resize((disc, disc), Image.LANCZOS)
    canvas.paste(mark, (sun_x - disc // 2, sun_y - disc // 2), mark)

    draw = ImageDraw.Draw(canvas)
    centred(draw, 8, "CALLED IN SICK", font(76), "white")
    centred(draw, 84, "FOR GTA 6", font(76), "white")
    # Bottom bar: five gold wanted stars, then the punchline.
    centred(draw, SIZE - BAR + 6, "\u2605 \u2605 \u2605 \u2605 \u2605", font(52), "#ffd21f")
    centred(draw, SIZE - BAR + 66, "WANTED IN LEONIDA", font(58), "white")

    canvas.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, canvas.size, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
