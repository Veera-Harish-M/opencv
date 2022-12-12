import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

img=cv.imread("moom.jpg",0)
plt.subplot(331).imshow(img,cmap='gray')
plt.subplot(331).set_title("Original")
plt.subplot(331).axis("off")

# image = cv.blur(img, (3,3)) 
 
height, width = img.shape

img_new = np.zeros([height, width])
 
for i in range(1, height-1):
    for j in range(1, width-1):
        img_new[i, j]= np.sum(img[i-1:i+2,j-1:j+2])//9

plt.subplot(332).imshow(np.array(img_new,dtype=np.uint8),cmap='gray')
plt.subplot(332).set_title("Blured image")
plt.subplot(332).axis("off")

#normalized the image
f = img_new / 255
plt.subplot(333).imshow(f, cmap='gray')
plt.subplot(333).set_title("Normalized")
plt.subplot(333).axis("off")
print(f)
# transform into frequency domain
F = np.fft.fftshift(np.fft.fft2(f))
print(F)
plt.subplot(334).imshow(np.log1p(np.abs(F)), cmap='gray')
plt.subplot(334).set_title("Frequency")
plt.subplot(334).axis("off")

# Laplacian Filter
'''Laplacian transfer filter function:
    H(u,v) = -4 Pi^2(u -P/2)^2 +(v-2/2)^2] 
'''

P,Q = F.shape
H = np.zeros((P,Q), dtype=np.float32)
for u in range(P):
    for v in range(Q):
        H[u,v] = -4*np.pi*np.pi*((u-P/2)**2 + (v-Q/2)**2)
        
plt.subplot(335).imshow(H, cmap='gray')
plt.subplot(335).set_title("Laplacian filter")
plt.subplot(335).axis("off")

# Laplacian image
Lap = H * F
Lap = np.fft.ifftshift(Lap)
Lap = np.real(np.fft.ifft2(Lap))

# convert the Laplacian Image value into range [-1,1]
OldRange = np.max(Lap) - np.min(Lap)
NewRange = 1 - -1
LapScaled = (((Lap - np.min(Lap)) * NewRange) / OldRange) + -1

plt.subplot(336).imshow(LapScaled, cmap='gray')
plt.subplot(336).set_title("Scaled")
plt.subplot(336).axis("off")

# image ehancement
c = -1
g = f + c*LapScaled
g = np.clip(g, 0, 1)

plt.subplot(337).imshow(g, cmap='gray')
plt.subplot(337).set_title("Final")
plt.subplot(337).axis("off")
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()