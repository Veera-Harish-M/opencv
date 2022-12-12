'''4. Read an image and find a clone of it'''
import cv2 as cv

img1=cv.imread("test.jfif")

cv.imshow("original",img1)

img2=img1.copy()
cv.imshow("clone",img2)

cv.waitKey(0)

cv.destroyAllWindows()