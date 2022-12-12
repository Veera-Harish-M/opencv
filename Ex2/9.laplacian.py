# 9. Find out the Laplacian of an image

import cv2 as cv

img1=cv.imread("test.jfif")
cv.imshow("apple",img1)

laplacian = cv.Laplacian(img1,cv.CV_64F)
cv.imshow("laplacian",laplacian)

cv.waitKey(0)

cv.destroyAllWindows()