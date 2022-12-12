'''8. Read an image and apply the Sobel operator to it.'''

import cv2 as cv

img1=cv.imread("test.jfif")
cv.imshow("apple",img1)

sobelx = cv.Sobel(img1,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img1,cv.CV_64F,0,1,ksize=5)

cv.imshow("sobelx",sobelx)
cv.imshow("sobely",sobely)

cv.waitKey(0)

cv.destroyAllWindows()