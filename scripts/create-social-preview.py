from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parent.parent
out = root / 'public'
out.mkdir(exist_ok=True)
im = Image.new('RGB', (1200, 630), '#fff200')
d = ImageDraw.Draw(im)
font_path = 'C:/Windows/Fonts/arialbd.ttf'
def font(size):
    return ImageFont.truetype(font_path, size)
d.ellipse((-120, -140, 220, 200), fill='#98c9ad')
for i in range(6):
    d.rectangle((940+i*35, 0, 1200, 40+i*35), fill='#3d52ef')
d.ellipse((965, 340, 1305, 680), fill='#27104f')
for i in range(8):
    d.ellipse((975+i*9, 350+i*9, 1295-i*9, 670-i*9), outline='#514362', width=2)
d.ellipse((1080, 455, 1190, 565), fill='#16d264')
d.text((60, 35), 'INDEPENDENT SPIRIT. SHARED SOUNDTRACK.', font=font(16), fill='#27104f')
d.text((52, 105), 'WRAPPED', font=font(176), fill='#df104c', stroke_width=2)
d.text((60, 270), '2026', font=font(228), fill='#df104c', stroke_width=2)
d.text((65, 555), 'YOUR YEAR. YOUR MUSIC. OUR CULTURE.', font=font(27), fill='#27104f')
d.text((65, 600), 'An independent community celebration on Solana. Not affiliated with Spotify.', font=font(13), fill='#27104f')
im.save(out / 'social-preview.png', optimize=True)
