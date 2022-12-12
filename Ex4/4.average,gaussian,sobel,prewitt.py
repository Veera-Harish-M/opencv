import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d 
from skimage import restoration
import random


def noise(img):
    print(img.shape)
    row , col = img.shape
     
    n = 1000
    for i in range(n):
        y=random.randint(0, row - 1)
        x=random.randint(0, col - 1)
        noise_inf=[0,255] 
        img[y][x] = noise_inf[random.randint(0,1)]
    return img


img=cv.imread("cat1.jpg",0)
plt.subplot(3,5,1).set_title("Original")
plt.subplot(3,5,1).imshow(img, cmap='gray')

average = cv.blur(img,(5, 5))
plt.subplot(3,5,2).set_title("Average")
plt.subplot(3,5,2).imshow(average, cmap='gray')
average=noise(average)
plt.subplot(3,5,7).set_title("adding noise")
plt.subplot(3,5,7).imshow(average, cmap='gray')

Gaussian =cv.GaussianBlur(img,(7,7),0)
plt.subplot(3,5,3).set_title("Gaussian")
plt.subplot(3,5,3).imshow(Gaussian, cmap='gray')
Gaussian=noise(Gaussian) 
plt.subplot(3,5,8).imshow(Gaussian, cmap='gray')

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv.filter2D(img, -1, kernelx)
img_prewitty = cv.filter2D(img, -1, kernely)
prewitt=img_prewittx+img_prewitty
plt.subplot(3,5,4).set_title("Prewitt")
plt.subplot(3,5,4).imshow(prewitt, cmap='gray')



#sobel
img_sobelx = cv.Sobel(img,cv.CV_8U,1,0,ksize=5)
img_sobely = cv.Sobel(img,cv.CV_8U,0,1,ksize=5)
sobel = img_sobelx + img_sobely
plt.subplot(3,5,5).set_title("Sobel")
plt.subplot(3,5,5).imshow(sobel, cmap='gray')



#restoring average
psf = np.ones((5, 5)) / 25
averageimg =average+ 0.01 * average.std() * np.random.standard_normal(average.shape)
average_deconvolved = restoration.wiener(averageimg, psf, 1, clip=False)
plt.subplot(3,5,7).set_title("removing noise")
plt.subplot(3,5,12).imshow(average_deconvolved, cmap='gray')


#restoring gaussian 
psf = np.ones((7, 7)) / 49
Gaussianimg =Gaussian+ 0.01 * Gaussian.std() * np.random.standard_normal(Gaussian.shape)
average_deconvolved = restoration.wiener(Gaussianimg, psf,1, clip=False)
plt.subplot(3,5,13).imshow(average_deconvolved, cmap='gray')





plt.show()

