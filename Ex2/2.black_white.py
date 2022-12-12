#2. Read a color image and convert it into grayscale.

import cv2 as cv

img=cv.imread("apple.jpg")
cv.imshow("apple",img)

img1=cv.imread("test.jfif")
gray=cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
#img1=cv.imread("test.jfif",0)
cv.imshow("Black",gray)

cv.waitKey(0)

cv.destroyAllWindows()