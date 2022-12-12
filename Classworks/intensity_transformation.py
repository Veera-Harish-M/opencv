# to perform intensity transformations (log,inverse log, negative, power functions)
 
import cv2 as cv
import numpy as np
import math

import matplotlib.pyplot as plt

img=cv.imread("i.jpg",0)

height, width = img.shape

img_log=[]
img_negative=[]
img_inverse_log=[]
img_pow=[]
for i in range(height):
    temp_img_log=[]
    temp_img_negative=[]
    temp_img_inverse_log=[]
    temp_img_pow=[]
    for j in range(width):
        px=img[i,j]
        temp_img_inverse_log.append(math.exp(px)** (1/35)-1)
        temp_img_log.append(round(math.log(1+px)*50))
        temp_img_negative.append(255-px)
        temp_img_pow.append(30*pow(px,1/3.6))
    img_log.append(temp_img_log)
    img_negative.append(temp_img_negative)
    img_inverse_log.append(temp_img_inverse_log)
    img_pow.append(temp_img_pow)
cv.imshow("ORIGINAL",img)
cv.imshow("LOG",np.array(img_log,dtype=np.uint8))
cv.imshow("INVERSE LOG",np.array(img_inverse_log,dtype=np.uint8))
cv.imshow("POW",np.array(img_pow,dtype=np.uint8))
cv.imshow("NEGATIVE",np.array(img_negative,dtype=np.uint8))



cv.waitKey(0)

cv.destroyAllWindows()