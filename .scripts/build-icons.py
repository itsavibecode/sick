"""
Generate the full favicon + PWA icon set for Illness Tracker.

Output (written to repo root):
  favicon.ico         (16+32 multi-res)
  favicon-16.png
  favicon-32.png
  apple-touch-icon.png  (180x180, iOS home-screen)
  icon-192.png        (PWA)
  icon-512.png        (PWA)
  icon-maskable.png   (512x512 with safe-zone padding for Android adaptive icons)

Design: same blue->purple gradient as the inline SVG favicon, with the
stethoscope emoji rendered via Segoe UI Emoji (Windows) for visual parity
with the existing brand.
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = r"T:\ClaudeCodeRepo\sick"
EMOJI_FONT = r"C:\Windows\Fonts\seguiemj.ttf"

# Brand colors
COLOR_A = (88, 166, 255)   # #58a6ff
COLOR_B = (163, 113, 247)  # #a371f7


def gradient_square(size, radius_ratio=0.22):
    """Solid rounded square with a diagonal gradient from A to B."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    grad = Image.new("RGBA", (size, size), 0)
    pix = grad.load()
    for y in range(size):
        for x in range(size):
            t = (x + y) / (2 * (size - 1))
            r = int(COLOR_A[0] * (1 - t) + COLOR_B[0] * t)
            g = int(COLOR_A[1] * (1 - t) + COLOR_B[1] * t)
            b = int(COLOR_A[2] * (1 - t) + COLOR_B[2] * t)
            pix[x, y] = (r, g, b, 255)
    # Rounded corners
    mask = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(mask)
    r = int(size * radius_ratio)
    md.rounded_rectangle((0, 0, size - 1, size - 1), radius=r, fill=255)
    img.paste(grad, (0, 0), mask)
    return img


def stamp_emoji(img, emoji, size_ratio=0.62, y_ratio=0.56):
    """Paste an emoji centered on the image."""
    size = img.size[0]
    font_size = int(size * size_ratio)
    try:
        font = ImageFont.truetype(EMOJI_FONT, font_size)
    except OSError:
        return img  # Fall back to no emoji on non-Windows
    # Pillow's emoji rendering needs RGBA + the special embedded color flag
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), emoji, font=font, embedded_color=True)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (size - w) // 2 - bbox[0]
    y = int(size * y_ratio) - h // 2 - bbox[1]
    draw.text((x, y), emoji, font=font, embedded_color=True)
    return img


def make_icon(size, *, maskable=False):
    if maskable:
        # Maskable: 40% safe-zone radius. Render the visual at 70% scale,
        # centered, so Android can crop edges without clipping the brand.
        full = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        # Background fills the entire canvas (no rounded corners, since
        # Android applies its own mask)
        bg = Image.new("RGBA", (size, size))
        bgpix = bg.load()
        for y in range(size):
            for x in range(size):
                t = (x + y) / (2 * (size - 1))
                r = int(COLOR_A[0] * (1 - t) + COLOR_B[0] * t)
                g = int(COLOR_A[1] * (1 - t) + COLOR_B[1] * t)
                b = int(COLOR_A[2] * (1 - t) + COLOR_B[2] * t)
                bgpix[x, y] = (r, g, b, 255)
        full.paste(bg, (0, 0))
        # Stethoscope in the inner safe zone (60% of canvas)
        inner = int(size * 0.6)
        emoji_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        stamp_emoji(emoji_layer, "\U0001FA7A", size_ratio=0.55 * 0.6, y_ratio=0.56)
        full.alpha_composite(emoji_layer)
        return full
    else:
        img = gradient_square(size)
        stamp_emoji(img, "\U0001FA7A")
        return img


def main():
    targets = [
        ("favicon-16.png", 16, False),
        ("favicon-32.png", 32, False),
        ("apple-touch-icon.png", 180, False),
        ("icon-192.png", 192, False),
        ("icon-512.png", 512, False),
        ("icon-maskable.png", 512, True),
    ]
    for name, size, maskable in targets:
        img = make_icon(size, maskable=maskable)
        path = os.path.join(OUT, name)
        img.save(path, "PNG", optimize=True)
        print(f"  wrote {name} ({size}x{size}, maskable={maskable}, {os.path.getsize(path)} bytes)")

    # Multi-res favicon.ico (16 + 32 + 48)
    sizes = [16, 32, 48]
    ico_layers = [make_icon(s) for s in sizes]
    ico_path = os.path.join(OUT, "favicon.ico")
    ico_layers[0].save(ico_path, format="ICO", sizes=[(s, s) for s in sizes])
    print(f"  wrote favicon.ico (16+32+48, {os.path.getsize(ico_path)} bytes)")


if __name__ == "__main__":
    main()
