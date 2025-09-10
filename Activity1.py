from PIL import Image, ImageDraw, ImageFont

# Canvas size
w, h = 500, 500
whiteCanvas = Image.new('RGB', (w, h), "White")
draw = ImageDraw.Draw(whiteCanvas)

# Medal sling (rectangles)
draw.rectangle([w/2-55, 50, w/2+55, 300], fill="Purple")
draw.rectangle([w/2-45, 50, w/2+45, 300], fill="Magenta")
draw.rectangle([w/2-35, 50, w/2+35, 300], fill="skyBlue")
draw.rectangle([w/2-25, 50, w/2+25, 300], fill="darkOrange")
draw.rectangle([w/2-15, 50, w/2+15, 300], fill="Gold")

# Medal circle
cx, cy, r = w//2, 300, 100
draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(205,173,0))
cx, cy, r = w//2, 300, 90
draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(255, 215, 0), outline=(205,173,0), width=5)

# Font loader (use Arial from Windows fonts folder)
def get_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size)  # Arial Bold
        else:
            return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)   # Arial Regular
    except:
        return ImageFont.load_default()

# Fonts
topFont = get_font(37, bold=True)
titleFont = get_font(19, bold=True)
subtitleFont = get_font(22)
nameFont = get_font(18, bold=False)

# Helper to measure text
def get_text_size(text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

# Top text
topText = "BISU Balilihan PASUC 2025"
tw, th = get_text_size(topText, topFont)
draw.text((w//2 - tw//2, 10), topText, font=topFont, fill="Purple")

# Medal text
title = "Sportsmanship"
title2 = "Award"


tw, th = get_text_size(title, titleFont)
draw.text((cx - tw//2, cy-15), title, font=titleFont, fill=(139,105,20))

tw, th = get_text_size(title2, titleFont)
draw.text((cx - tw//2, cy--5), title2, font=titleFont, fill=(139,105,20))

#Bottom text
myName = "Marc Arron C. Nepomuceno BSCS-3B"
tw, th = get_text_size(myName, nameFont)
draw.text((w//2 - tw//2, h - th - 10), myName, font=nameFont, fill=(0,0,0))




whiteCanvas.save("CSELEC3_3B_NepomucenoMarcArron_Activity1.png")
