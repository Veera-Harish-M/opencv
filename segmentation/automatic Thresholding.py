import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

# Load the image in greyscale
img = cv2.imread('charlie.jpg',0)
hist=cv2.calcHist(img, [0], None, [256], [0, 256])

lowThreshold =random.randint(0,255)

def automaticThreshold(lowThreshold,img):
    g1=[]
    g2=[]
    for i in img:
        for j in i:
            if j<lowThreshold:
                g1.append(j)
            else:
                g2.append(j)
    mean1=sum(g1)/len(g1)
    mean2=sum(g2)/len(g2)
    newThreshold=(mean1+mean2)/2

    if abs(newThreshold-lowThreshold)<10:
        print(f"Threshold = {int(newThreshold)}")
        return newThreshold
    else:
        lowThreshold=newThreshold
        newThreshold=0
        return automaticThreshold(lowThreshold,img)
finalThreshold=automaticThreshold(lowThreshold,img)
plt.plot(hist)


new_img=[]
for i in img:
    temp=[]
    for j in i:
        if j<finalThreshold:
            temp.append(0)
        else:
            temp.append(255)
    new_img.append(temp)

cv2.imshow("original",img)
cv2.imshow("segmentation",np.array(new_img,dtype=np.uint8))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()