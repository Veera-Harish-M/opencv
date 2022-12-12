'''7. Read an image and extract your region of interest (ROI) using cvSetImageROI.'''

import cv2 as cv

img1=cv.imread("test.jfif")
r = cv.selectROI("select the area", img1)
print(r)
cropped_image = img1[int(r[1]):int(r[1]+r[3]),
                      int(r[0]):int(r[0]+r[2])]

cv.imshow("Cropped image", cropped_image)
cv.waitKey(0)

cv.destroyAllWindows()