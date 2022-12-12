'''2.Perform contrast stretching on cameraman.tif image with the help of following transfer function as shown below :'''

import cv2
import numpy as np

img = cv2.imread("cat.jpg")
original = img.copy()
xp = [0,80,120,255]
fp = [0,40, 180, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
img = cv2.LUT(img, table)
cv2.imshow("original", original)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 