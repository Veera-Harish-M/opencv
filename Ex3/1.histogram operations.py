'''1. Given an input image tire.tif of arbitrary histogram, generate an output image that has a nearly uniform histogram by Histogram Equalization. 
(a) Compute the probability of occurrence of each of the 256 gray levels in the image and display the normalized histogram. P (ri) = Number of pixels of gray level i Total number of pixels , i =0,1,...,255 
(b) From the normalized histogram, compute the cumulative distribution function. i T(i) = k=0 P(rk), i = 0,1,...,255 
(c) Given a gray level r in the input image, map that level to yr = 255×T (r). 
(d) Display the histogram equalized image.'''


import cv2 as cv
from matplotlib import pyplot as plt
import numpy
import math
axis = plt.subplots(1, 2)[1]

img=cv.imread("test.jfif",0)
cv.imshow("original",img)
print(img.size)
for i in numpy.unique(img):
    p=round((numpy.count_nonzero(img == i)/img.size)*100,2)
    print(f"P({i})->{p}")
hist=cv.calcHist(img, [0], None, [256], [0, 256])
t=0
T={}
for i in numpy.unique(img):
    p=round((numpy.count_nonzero(img == i)/img.size)*100,2)
    t+=p
    T[i]=t
    print(f"T({i})->{t}")
axis[0].plot(hist)

g=int(input("Enter The grey level r:"))
if g in T:
    print(f"y({g}) = {math.floor(255* T[g])}")
else:
    print(f"input grey level is not present in the image: y({g})=0")

equ = cv.equalizeHist(img)
hist1=cv.calcHist(equ, [0], None, [256], [0, 256])
axis[1].plot(hist1)
cv.imshow("equalizer",equ)
plt.show()


cv.waitKey(0)

cv.destroyAllWindows()