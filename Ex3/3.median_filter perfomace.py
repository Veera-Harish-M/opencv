'''3.Consider an input image cameraman.tif and add Salt and Pepper Noise using imnoise inbuilt function.
Perform median filtering on the noisy image of varying mask size 
(3 × 3, 5 × 5, 7 × 7, and 9×9) and observe the filtering performance.'''


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


        
median3 = cv.medianBlur(newsp, 3)
median5 = cv.medianBlur(newsp, 5)
median7 = cv.medianBlur(newsp, 7)
median9 = cv.medianBlur(newsp, 9)
cv.imshow("Median Filter 3x3",np.array(median3,dtype=np.uint8))

cv.imshow("Median Filter 5x5",np.array(median5,dtype=np.uint8))
cv.imshow("Median Filter 7x7",np.array(median7,dtype=np.uint8))
cv.imshow("Median Filter 9x9",np.array(median9,dtype=np.uint8))
cv.waitKey(0)
cv.destroyAllWindows()