'''4.Consider an input image coins.png. Use an averaging filter of size 
3×3 and 5×5 by convolving with the original image'''

import cv2 as cv
import numpy as np


img=cv.imread("moom.jpg",0)
cv.imshow("Original",img)
 
image3 = cv.blur(img,(3, 3))
image5 = cv.blur(img,(5, 5))

cv.imshow("Mean Filter 3x3",image3)
cv.imshow("Mean Filter 5x5",image5)


cv.waitKey(0)
cv.destroyAllWindows()