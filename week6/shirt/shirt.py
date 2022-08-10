import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

a = os.path.splitext(sys.argv[1])
b = os.path.splitext(sys.argv[2])

if not (b[1] == ".jpg" or b[1] == ".jpeg" or b[1] == ".png"):
    sys.exit("Invalid output")

if a[1] != b[1]:       #not same extension
    sys.exit("Input and output have different extensions")


try:
    shirt = Image.open("shirt.png")
    photo = Image.open(sys.argv[1])
    size = shirt.size
    photo = ImageOps.fit(photo,size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
