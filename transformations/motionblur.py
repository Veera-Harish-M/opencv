# loading library
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg')
cv2.imshow('Original', img)

# Specify the kernel size.
# The greater the size, the more the motion.
kernel_size = 15

# Create the vertical kernel.
kernel_v = np.zeros((kernel_size, kernel_size))
# plt.subplot(131).plot(np.abs(kernel_v),cmap="gray")
kernel_h = np.zeros((30, 30))

# Fill the middle row with ones.
kernel_v[:, int((kernel_size - 1)/2)] = np.ones(kernel_size)*1
print(kernel_v)

#plt.subplot(132).plot(np.abs(kernel_v),cmap="gray")

kernel_h[:, int((30 - 1)/2)] = np.ones(30)

  
# Normalize.
kernel_v /= kernel_size
print(kernel_v)
#plt.subplot(133).plot(np.abs(kernel_v),cmap="gray")
kernel_h /= 30

# Apply the vertical kernel.
vertical_mb = cv2.filter2D(img, -1, kernel_v)

# Apply the horizontal kernel.
horizonal_mb = cv2.filter2D(img, -1, kernel_h)

cv2.imshow('vertical', vertical_mb)
cv2.imshow('horizontal', horizonal_mb)
plt.show()
cv2.waitKey(0)