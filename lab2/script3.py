from PIL import Image, ImageDraw, ImageFont
from argparse import ArgumentParser

if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument("img_path")
    with Image.open(argumentParser.parse_args().img_path) as img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default(size=15)
        draw.text((0, 0), "watermark", fill=(220, 220, 220), font=font)
        with Image.open("watermark.png") as watermarkImg:
            img.paste(watermarkImg.resize((30, 30)), (20, 20))
        img.save("img_with_watermark.jpg", "jpeg")
        img.show()
