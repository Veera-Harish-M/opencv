'''5. Use a Gaussian Low Pass Filter in frequency domain to remove Salt and Pepper Noise 
from the image coins.png.'''

import cv2 as cv
from skimage.util import random_noise


img=cv.imread("test.jfif",0)
cv.imshow("Original",img)

sp = random_noise(img, mode='s&p')
cv.imshow("sp",sp)


image =cv.GaussianBlur(sp,(5,5),0)
cv.imshow("Gaussian Filter",image)


cv.waitKey(0)
cv.destroyAllWindows()