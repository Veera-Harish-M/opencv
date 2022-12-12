#adding noise to image and removing noise with median filter

import cv2 as cv
import numpy as np
# from skimage.util import random_noise
import random

def noise(img):
    row , col = img.shape
     
    n = random.randint(10,(row*col)//4)
    for i in range(n):
        y=random.randint(0, row - 1)
        x=random.randint(0, col - 1)
        noise_inf=[0,255] 
        img[y][x] = noise_inf[random.randint(0,1)]
    return img
    

img=cv.imread("test.jfif",0)
cv.imshow("original",img)
# sp = random_noise(img, mode='s&p')
# cv.imshow("sp",sp)

newsp=noise(img)
cv.imshow("noised",newsp)
height, width = img.shape

img_new = np.zeros([height, width])
 
for i in range(1, height-1):
    for j in range(1, width-1):
        img_new[i, j]= np.median(newsp[i-1:i+2,j-1:j+2])
        
cv.imshow("Median Filter",np.array(img_new,dtype=np.uint8))

cv.waitKey(0)
cv.destroyAllWindows()