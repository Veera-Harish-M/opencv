# loading library
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import restoration
import random

from scipy.signal import convolve2d 


img = cv2.imread('cat.jpg',0)
plt.subplot(1,4,1).imshow(img, cmap='gray')

psf = np.ones((5, 5)) / 25
img = convolve2d(img, psf, 'same')

plt.subplot(1,4,2).imshow(img, cmap='gray')



def noise(img):
    print(img.shape)
    row , col = img.shape
     
    n = random.randint(10,(row*col)//16)
    for i in range(n):
        y=random.randint(0, row - 1)
        x=random.randint(0, col - 1)
        noise_inf=[0,255] 
        img[y][x] = noise_inf[random.randint(0,1)]
    return img
    
noisy=noise(img)
plt.subplot(1,4,3).imshow(noisy, cmap='gray')


psf = np.ones((5, 5)) / 25
img += 0.1 * noisy.std() * np.random.standard_normal(noisy.shape)

denoised= restoration.wiener(img, psf, 1, clip=False)
plt.subplot(1,4,4).imshow(denoised, cmap='gray')
plt.show()
cv2.waitKey(0)