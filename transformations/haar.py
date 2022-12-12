# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os


# loading image
img = mahotas.imread('hello.jpg')

# filtering image
img = img[:, :, 0]
# showing image
print("Image")

imshow(img)
show()

# haar transform
h = mahotas.haar(img)

# showing image
print("Image with haar transform")
imshow(h)
show()
