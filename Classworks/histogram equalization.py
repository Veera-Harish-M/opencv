#histogram equalization of an image
 
import cv2 as cv
from matplotlib import pyplot as plt

axis = plt.subplots(1, 2)[1]

img=cv.imread("test.jfif",0)
cv.imshow("original",img)
hist=cv.calcHist(img, [0], None, [256], [0, 256])
axis[0].plot(hist)



equ = cv.equalizeHist(img)
hist1=cv.calcHist(equ, [0], None, [256], [0, 256])
axis[1].plot(hist1)
cv.imshow("equalizer",equ)
plt.show()