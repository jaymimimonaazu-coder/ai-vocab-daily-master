"""One-off script to generate PWA icons. Not part of the shipped app."""
from PIL import Image, ImageDraw, ImageFont

INDIGO = (79, 70, 229)
VIOLET = (124, 58, 237)
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def gradient_square(size):
    img = Image.new("RGB", (size, size))
    px = img.load()
    for y in range(size):
        t = y / (size - 1)
        r = round(INDIGO[0] + (VIOLET[0] - INDIGO[0]) * t)
        g = round(INDIGO[1] + (VIOLET[1] - INDIGO[1]) * t)
        b = round(INDIGO[2] + (VIOLET[2] - INDIGO[2]) * t)
        for x in range(size):
            px[x, y] = (r, g, b)
    return img


def draw_icon(size, safe_ratio):
    img = gradient_square(size)
    draw = ImageDraw.Draw(img)

    text = "AI"
    font_size = int(size * safe_ratio * 0.42)
    font = ImageFont.truetype(FONT_PATH, font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(
        (size / 2 - tw / 2 - bbox[0], size / 2 - th / 2 - bbox[1] - size * 0.05),
        text,
        font=font,
        fill=(255, 255, 255),
    )

    # three small dots underneath, echoing "3 words a day"
    dot_r = size * 0.028
    gap = size * 0.11
    cy = size / 2 + size * safe_ratio * 0.28
    for i in range(3):
        cx = size / 2 + (i - 1) * gap
        draw.ellipse(
            [cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r],
            fill=(255, 255, 255),
        )
    return img


for size in (192, 512):
    draw_icon(size, safe_ratio=1.0).save(f"icons/icon-{size}.png")
    draw_icon(size, safe_ratio=0.6).save(f"icons/icon-{size}-maskable.png")

print("done")
