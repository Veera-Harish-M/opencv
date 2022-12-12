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
    if(len(g1)==0):
        mean1=0
    else:
        mean1=sum(g1)//len(g1)
    if(len(g2)==0):
        mean2=0
    else:
        mean2=sum(g2)//len(g2)
    newThreshold=(mean1+mean2)/2

    if abs(newThreshold-lowThreshold)<10:
        print(f"Threshold = {int(newThreshold)}")
        return newThreshold
    else:
        lowThreshold=newThreshold
        newThreshold=0
        return automaticThreshold(lowThreshold,img)



height,width=img.shape
d=2
minX=0
minY=0

thX=height//d
thY=width//d
maxX=thX
maxY=thY
images={}
print(height,width)
a=1
thres=[]

newImgage=np.zeros((height,width))
for k in range(d):
    for m in range(d):
        print(minX,maxX,minY,maxY)
        # print(np.min(img[minX:maxX,minY:maxY]),np.max(img[minX:maxX,minY:maxY]))
        localth=np.median(img[minX:maxX,minY:maxY])
        finalTh=automaticThreshold(localth,img[minX:maxX,minY:maxY])
        thres.append(finalTh)
        new_img=[]
        for i in img[minX:maxX,minY:maxY]:
            temp=[]
            for j in i:
                if j<finalTh:
                    temp.append(0)
                else:
                    temp.append(255)
            new_img.append(temp)
        images[a]=new_img
        newImgage[minX:maxX,minY:maxY]=new_img
        a+=1
        minX=maxX
        
        maxX=maxX+thX
    minY=maxY
    maxY=maxY+thY
    minX=0  
    maxX=thX

for i in range(d*d):   
    plt.subplot(d,d,i+1).imshow(np.array(images[i+1],dtype=np.uint8), cmap='gray')


cv2.imshow("original",img)
cv2.imshow("seg",np.array(newImgage,dtype=np.uint8))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()