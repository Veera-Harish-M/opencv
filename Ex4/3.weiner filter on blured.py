import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from skimage import restoration
from scipy.signal import convolve2d 

image = cv.imread("cat.jpg",0)

psf = np.ones((5, 5)) / 25
img = convolve2d(image, psf, 'same')
plt.subplot(1,2,1).set_title("Original")
plt.subplot(1,2,1).imshow(img, cmap='gray')
img += 0.1 * img.std() * np.random.standard_normal(img.shape)

deconvolved_img = restoration.wiener(img, psf, 0.1, clip=False)

plt.subplot(1,2,2).set_title("Weiner filter")
plt.subplot(1,2,2).imshow(deconvolved_img, cmap='gray')
plt.show()