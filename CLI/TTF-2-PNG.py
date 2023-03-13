import os
from PIL import Image, ImageFont

desired_characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # The characters you want to extract

point_size = 32
font = ImageFont.truetype("font_file_path_here", point_size)
output = "./output/"

if not os.path.exists(output):
    os.makedirs(output, exist_ok=True)

for char in desired_characters:
    im = Image.Image()._new(font.getmask(char))
    file_name = char + ".png"
    im.save(output + file_name)
