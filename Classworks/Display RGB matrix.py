#display R G B matrix of an image 

import cv2 as cv


img=cv.imread("he.jpg")
cv.imshow("color",img)

height, width, channels = img.shape
print(height,width,channels)
R=[]
G=[]
B=[]

for i in range(height):
    for j in range(width):
          R1,G1,B1=img[i,j]
          R.append(R1)
          G.append(G1)
          B.append(B1)
print(f"Red:{R}\n\nGreen:{G}\n\nBlue:{B}")