# loading library
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import restoration
import random

from scipy.signal import convolve2d 


img = cv2.imread('cat.jpg',0)
img_ori = cv2.imread('cat.jpg',0)
img_ori= cv2.resize(img,(256,256))
img = cv2.resize(img,(256,256))
plt.subplot(1,6,1).set_title("Original")
plt.subplot(1,6,1).imshow(img, cmap='gray')

psf = np.ones((5, 5)) / 25
img = convolve2d(img, psf, 'same')
plt.subplot(1,6,2).set_title("blured")
plt.subplot(1,6,2).imshow(img, cmap='gray')



def noise(img):
    print(img.shape)
    row , col = img.shape
     
    n = random.randint(10,(row*col)//100)
    for i in range(n):
        y=random.randint(0, row - 1)
        x=random.randint(0, col - 1)
        noise_inf=[0,255] 
        img[y][x] = noise_inf[random.randint(0,1)]
    return img
    
noisy=noise(img)
psnr=cv2.PSNR(img,noisy)
print(psnr)
plt.subplot(1,6,3).set_title("noised")
plt.subplot(1,6,3).imshow(noisy, cmap='gray')

height, width = noisy.shape

img_new = np.zeros([height, width])
 
for i in range(1, height-1):
    for j in range(1, width-1):
        img_new[i, j]= np.median(noisy[i-1:i+2,j-1:j+2])
        
plt.subplot(1,6,4).imshow(img_new, cmap='gray')

psf = np.ones((3, 3)) / 9


# fft of blured image
G = np.fft.fft2(img_new)

n = 0.8
#fft of mask
B = np.fft.fft2(psf, s=(256, 256))
B[np.abs(B) < n] = n
H = np.divide(np.ones((256, 256)), B)


I = np.multiply(G, H)
im = np.abs(np.fft.ifft2(I))
plt.subplot(1,6,5).set_title("inverse filter")
plt.subplot(1,6,5).imshow(im, cmap='gray')



plt.show()
cv2.waitKey(0)