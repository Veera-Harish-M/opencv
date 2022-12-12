
import cv2 as cv
import numpy as np
img=cv.imread("point_attributebasedpoint.png",0)
cv.imshow("original",img)

height, width = img.shape
mask =np.array([[-1,-1 ,-1],[-1, 8, -1],[-1, -1 ,-1]])
print(mask)
new=np.zeros((height,width))
for i in range(1, height-1):
    for j in range(1, width-1):
        new[i, j]= np.sum(img[i-1:i+2,j-1:j+2]*mask)
        
cv.imshow("Point detection",np.array(new,dtype=np.uint8))


cv.waitKey(0)
cv.destroyAllWindows()