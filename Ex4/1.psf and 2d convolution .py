import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from scipy.signal import convolve2d 

image = cv.imread("cat.jpg",0)
plt.subplot(1,2,1).imshow(image, cmap='gray')
plt.subplot(1,2,1).set_title("Original")
# Model an out-of-blur PSF 
psf = np.ones((5, 5)) / 25


#circular boundary condition
img2 = convolve2d(image, psf, mode='same',boundary="wrap")
plt.subplot(1,2,2).set_title("blured circular boundary")
plt.subplot(1,2,2).imshow(img2, cmap='gray')
plt.show()