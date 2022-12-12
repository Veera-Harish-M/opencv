'''6. Take two images an.jpg & tu.jpg from the folder Face and calculate their phase using FFT and 
exchange the phase between them. 
See the impact of phase exchange between two images. Hint: • z =rcosφ+isinφ • z =reiφ'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
img0 = cv2.imread('hello.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img0, (300, 225))
cv2.imshow("original1",img1)
cv2.imshow("original2",img2)

dft1 = cv2.dft(np.float32(img1), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift1 = np.fft.fftshift(dft1)
mag1, phase1 = cv2.cartToPolar(dft_shift1[:,:,0], dft_shift1[:,:,1])
# get spectrum for viewing only
spec1 = np.log(mag1) / 30
#raise mag to some power near 1
# values larger than 1 increase contrast; values smaller than 1 decrease contrast
mag1 = cv2.pow(mag1, 1.1)

dft2 = cv2.dft(np.float32(img2), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift2 = np.fft.fftshift(dft2)
mag2, phase2 = cv2.cartToPolar(dft_shift2[:,:,0], dft_shift2[:,:,1])
spec2 = np.log(mag2) / 30
mag2 = cv2.pow(mag2, 1.1)
# convert magnitude and phase into cartesian real and imaginary components
real1, imag1 = cv2.polarToCart(mag1, phase2)
real2, imag2 = cv2.polarToCart(mag2, phase1)

# combine cartesian components into one complex image
back1 = cv2.merge([real1, imag1])
back2 = cv2.merge([real2, imag2])

# shift origin from center to upper left corner
back_ishift1 = np.fft.ifftshift(back1)
back_ishift2 = np.fft.ifftshift(back2)

# do idft saving as complex output
img_back1 = cv2.idft(back_ishift1)
img_back2 = cv2.idft(back_ishift2)


# combine complex components into original image again
img_back1 = cv2.magnitude(img_back1[:,:,0], img_back1[:,:,1])
img_back2 = cv2.magnitude(img_back2[:,:,0], img_back2[:,:,1])

# re-normalize to 8-bits
min1, max1 = np.amin(img_back1, (0,1)), np.amax(img_back1, (0,1))
img_back1 = cv2.normalize(img_back1, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
min2, max2 = np.amin(img_back2, (0,1)), np.amax(img_back2, (0,1))
img_back2 = cv2.normalize(img_back2, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow("Swapped1",img_back1)
cv2.imshow("swapped2",img_back2)

cv2.waitKey(0)
cv2.destroyAllWindows()