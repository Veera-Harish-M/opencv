'''3. Read an image and find out its following details(a) Height (b) Width (c) Channels (d) Depth'''

import cv2 as cv

img=cv.imread("apple.jpg")
cv.imshow("apple",img)

height, width, channels = img.shape
print(height,width,channels)


cv.waitKey(0)

cv.destroyAllWindows()