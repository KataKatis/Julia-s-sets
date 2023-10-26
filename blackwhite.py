from PIL import Image
from math import sqrt

photoname = input("Photo name : ")
re = float(input("Real part : "))
im = float(input("Imagine part : "))
width = 4001
height = 4001
origin = (width//2, height//2)

img = Image.new(mode="1", size=(width, height), color=1)

c = complex(re, im)

for i in range(-2000, 2000):
    print(i)
    for j in range(-2000, 2000):
        z = complex(i/1000, j/1000)
        counter = 0

        while sqrt(z.imag**2 + z.real**2) <= 2 and counter < 30:
            counter += 1
            z = z**2 + c

        if counter == 30:
            img.putpixel((origin[0] + i, origin[1] + j), 0)

# img.putpixel((origin[0],origin[1]), 1)
img.save(f"{photoname}.png")
