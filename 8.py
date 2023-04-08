# Bonus: Assignment 11
from PIL import Image, ImageDraw


image = Image.new('RGB', (400, 400), color = 'white')
draw = ImageDraw.Draw(image)

draw.rectangle([50, 50, 200, 200], fill='red')
draw.text((100, 100), "Hello, World!", fill='white')
image.save("output.png")