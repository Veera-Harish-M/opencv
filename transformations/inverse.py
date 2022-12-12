import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
f, axes = plt.subplots(1, 5)

img =cv.resize( cv.imread('cat.jpg',0), (256, 256))

N = 256
f = img
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
axes[1].imshow(np.abs(g), cmap='gray')


# fft of blured image
G = np.fft.fft2(g)

n = 0.2
B[np.abs(B) < n] = n
H = np.divide(np.ones((N, N)), B)

axes[2].imshow(np.abs(H), cmap='gray')

I = np.multiply(G, H)
im = np.abs(np.fft.ifft2(I))
axes[2].imshow(im, cmap='gray')

plt.show()