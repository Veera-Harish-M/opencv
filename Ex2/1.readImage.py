#1. Read and display an image.

import cv2 as cv

img=cv.imread("apple.jpg")
cv.imshow("apple",img)

cv.waitKey(0)

cv.destroyAllWindows()