from PIL import Image
from math import sqrt, pi, e
from matplotlib import colormaps

photoname = input("Photo name : ")
re = -0.038088 #float(input("Real part : "))
im = 0.9754633#float(input("Imagine part : "))
width = 4001
height = 4001
origin = (width//2, height//2)

mycm = ((255, 255, 255), (255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255))

img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))

c = complex(re, im)

for i in range(-2000, 2001):
    print(i)
    for j in range(-2000, 2001):
        z = complex(i/1000, j/1000)
        counter = 0

        while sqrt(z.imag**2 + z.real**2) <= 2 and counter < 30:
            counter += 1
            z = z**2 + c

        #img.putpixel((origin[0] + i, origin[1] + j), mycm[round(6*counter/30)-1])
        img.putpixel((origin[0] + i, origin[1] + j), (int(255 * counter / 30), 0, 0))

# img.putpixel((origin[0],origin[1]), 1)
img.save(f"{photoname}.png")
