import os

from PIL import Image, ImageDraw, ImageFont


def create_image(text, font_name, font_size, width, height, text_color, background_color, output_path):
    font = ImageFont.truetype(font_name, font_size)
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    draw.text((x, y), text, font=font, fill=text_color)
    image.save(output_path)


text = input()
font_name = "simsun.ttc"
font_size = 36
width = 300
height = 100
text_color = (225, 225, 2225)  # 黑色字体
background_color = (0, 0, 0)  # 白色背景
output_path = f"./assets/images/name/{text}.png"
if os.path.exists(output_path):
    print("文件已存在，不需要生成图片。")
else:
    create_image(text, font_name, font_size, width, height, text_color, background_color, output_path)
