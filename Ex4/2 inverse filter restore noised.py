# loading library
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import restoration
import random

from scipy.signal import convolve2d 


img = cv2.imread('cat2.jpg',0)
img_ori = cv2.imread('cat2.jpg',0)
img_ori= cv2.resize(img,(256,256))
img = cv2.resize(img,(256,256))
plt.subplot(2,4,1).set_title("Original")
plt.subplot(2,4,1).imshow(img, cmap='gray')

psf = np.ones((5, 5)) / 25
img = convolve2d(img, psf, 'same')
plt.subplot(2,4,2).set_title("blured")
plt.subplot(2,4,2).imshow(img, cmap='gray')



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
plt.subplot(2,4,3).set_title("noised")
plt.subplot(2,4,3).imshow(noisy, cmap='gray')


psf = np.ones((5, 5)) / 25


# fft of blured image
G = np.fft.fft2(noisy)

n = 0.6
#fft of mask
B = np.fft.fft2(psf, s=(256, 256))
B[np.abs(B) < n] = n
H = np.divide(np.ones((256, 256)), B)


I = np.multiply(G, H)
im = np.abs(np.fft.ifft2(I))
plt.subplot(2,4,4).set_title("inverse filter")
plt.subplot(2,4,4).imshow(im, cmap='gray')

img = convolve2d(noisy, psf, 'same')
img =noisy+ 0.1 * noisy.std() * np.random.standard_normal(noisy.shape)

deconvolved_img = restoration.wiener(img, psf, 0.1, clip=False)

plt.subplot(2,4,5).set_title("Weiner filter")
plt.subplot(2,4,5).imshow(deconvolved_img, cmap='gray')

height, width = deconvolved_img.shape

img_new = np.zeros([height, width])
 
for i in range(1, height-1):
    for j in range(1, width-1):
        img_new[i, j]= np.median(deconvolved_img[i-1:i+2,j-1:j+2])
        
plt.subplot(2,4,6).imshow(img_new, cmap='gray')

# plt.subplot(1,2,1).imshow(img_ori, cmap='gray')
# plt.subplot(1,2,2).imshow(img_new, cmap='gray')



dft = cv2.dft(np.float32(img_new), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

rows, cols = img_new.shape
crow, ccol = int(rows / 2), int(cols / 2)

mask = np.ones((rows, cols, 2), np.uint8)
r = 20
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 0

fshift = dft_shift * mask

fshift_mask_mag = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

f_ishift = np.fft.ifftshift(fshift)

img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])



        
plt.subplot(2,4,7).imshow(img_back, cmap='gray')
print(img_back)
sum=np.sum(img_new,img_back)
plt.subplot(2,4,8).imshow(sum, cmap='gray')

plt.show()
cv2.waitKey(0)