from PIL import Image, ImageDraw, ImageFont


def add_watermark(image, wm_text):

    opened_image = Image.open(image)
    image_width, image_height = opened_image.size
    font_size = int(image_width / 10)
    font = ImageFont.truetype('Arial.ttf', font_size)
    draw = ImageDraw.Draw(opened_image)

    # Plot watermark location
    x, y = int(image_width / 2), int(image_height / 2)

    # Add the watermark
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=0, anchor='ms')
    opened_image.show()