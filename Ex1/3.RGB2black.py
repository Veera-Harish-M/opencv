'''Take input lena.png, display its red, green component and 
blue component separately; 
Binarize these component using threshold 0.3,0.2,0.4 respectively.'''

import cv2 as cv
import numpy as np

img=cv.imread("hello.jpg")
cv.imshow("color",img)

height, width, channels = img.shape
print(height,width,channels)

black_img=[]
for i in range(height):
    temp=[]
    for j in range(width):
        R1,G1,B1=img[i,j]
        black_img.append(sum([0 if R1/255 <0.3 else 255,0 if G1/255 <0.2 else 255,0 if B1/255 <0.4 else 255])/3)


cv.imshow("black",np.reshape(np.array(black_img),(height,width)))
      

cv.waitKey(0)

cv.destroyAllWindows()