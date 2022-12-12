import numpy as np
import cv2 as cv
image=cv.imread("cat.jpg",0)

from skimage.util import random_noise

noisy = random_noise(image, mode="gaussian")
cv.imshow("noise",noisy)

# noisy = image + np.random.poisson(image) 

# cv.imshow("noised",np.array(noisy,dtype=np.uint8))

cv.waitKey(0)

cv.destroyAllWindows()


# ‘gaussian’ (default)
# Gaussian-distributed additive noise.

# ‘localvar’
# Gaussian-distributed additive noise, with specified local variance at each point of image.

# ‘poisson’
# Poisson-distributed noise generated from the data.

# ‘salt’
# Replaces random pixels with 1.

# ‘pepper’
# Replaces random pixels with 0 (for unsigned images) or -1 (for signed images).

# ‘s&p’
# Replaces random pixels with either 1 or low_val, where low_val is 0 for unsigned images or -1 for signed images.

# ‘speckle’
