'''7. Implement the following two dimensional DFT equation on moon.tif image 
F(k,l) = M−1 m=0 N−1 n=0 f(m,n)e−j2π Mmke−j2π N nl 
You can realize the same using fft2 function of MATLAB.'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('cat.jpg',0)
f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')



plt.title('Original'), plt.axis("off")
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.axis("off")
plt.show()