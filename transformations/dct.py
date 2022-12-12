import cv2
import numpy as np
from matplotlib import pyplot as plt


img1 = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)    
dct = cv2.dct(np.float32(img1))         
 

idct = cv2.idct(dct)

plt.subplot(2,2,1),plt.imshow(img1,cmap = 'gray')
plt.title('Original'), plt.axis("off")
plt.subplot(2,2,2),plt.imshow(dct,cmap = 'gray',vmin = 0, vmax = 255)
plt.title('DCT image'), plt.axis("off")
plt.subplot(2,2,3),plt.imshow(idct,cmap = 'gray')
plt.title('IDCT image'), plt.axis("off")
plt.show()