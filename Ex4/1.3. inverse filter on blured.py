import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from skimage import restoration
from scipy.signal import convolve2d 

f, axes = plt.subplots(1, 4)

img =cv.resize( cv.imread('cat.jpg',0), (256, 256))

N = 256
f = img
axes[0].set_title("Original")
axes[0].imshow(f, cmap='gray')

# mask
b = np.ones((4, 4)) / (4 * 4)
print(b)
#fft of image 
F = np.fft.fft2(f)
#fft of mask
B = np.fft.fft2(b, s=(N, N))
#multiply fft of image with fft of mask
G = np.multiply(F, B)

#inverse fft of blured image 
g = np.fft.ifft2(G) 
axes[1].set_title("blured")
axes[1].imshow(np.abs(g), cmap='gray')


# fft of blured image
G = np.fft.fft2(g)

n = 0.2
B[np.abs(B) < n] = n
H = np.divide(np.ones((N, N)), B)


I = np.multiply(G, H)
im = np.abs(np.fft.ifft2(I))
axes[2].set_title("inverse filter")
axes[2].imshow(im, cmap='gray')


psf = np.ones((4, 4)) / 16
img = convolve2d(np.abs(g), psf, 'same')

img += 0.1 * img.std() * np.random.standard_normal(img.shape)

deconvolved_img = restoration.wiener(img, psf, 0.1, clip=False)

axes[3].imshow(deconvolved_img, cmap='gray')
plt.show()