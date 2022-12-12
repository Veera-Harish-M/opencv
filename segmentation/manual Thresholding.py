import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in greyscale
img = cv2.imread('charlie.jpg',0)

hist=cv2.calcHist(img, [0], None, [256], [0, 256])

lowThreshold =45
lowThreshold2 =30
highTreshold=95
new_img=[]
new_img2=[]
new_img3=[]
for i in img:
    temp=[]
    temp1=[]
    temp2=[]
    for j in i:
        if j<lowThreshold2 or j>highTreshold:
            temp2.append(255)
        else:
            temp2.append(0)
        if j<lowThreshold:
            temp1.append(0)
            temp.append(255)
        else:
            temp.append(0)
            temp1.append(255)
    new_img.append(temp)
    new_img2.append(temp1)
    new_img3.append(temp2)




plt.plot(hist)

cv2.imshow("original",img)
cv2.imshow("segmentation",np.array(new_img,dtype=np.uint8))
cv2.imshow("segmentation1",np.array(new_img2,dtype=np.uint8))
cv2.imshow("segmentation2",np.array(new_img3,dtype=np.uint8))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()