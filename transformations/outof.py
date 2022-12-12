import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from scipy.signal import convolve2d 

image = cv.imread("cat.jpg",0)
plt.subplot(1,2,1).imshow(image, cmap='gray')
psf = np.ones((5, 5)) / 25
img = convolve2d(image, psf, 'same')
plt.subplot(1,2,2).imshow(img, cmap='gray')
plt.show()