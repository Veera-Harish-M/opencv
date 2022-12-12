
import cv2 as cv
import numpy as np

img=cv.imread("line.png",0)
cv.imshow("original",img)

height, width = img.shape
#horizontal
hor_mask =np.array([[-1,-1 ,-1],[2, 2, 2],[-1, -1 ,-1]])
#vertical
ver_mask =np.array([[-1,2 ,-1],[-1, 2, -1],[-1, 2 ,-1]])
#45 deg
deg45_mask =np.array([[2,-1 ,-1],[-1, 2, -1],[-1, -1 ,2]])
#-45 deg
degNeg45_mask =np.array([[-1,-1 ,2],[-1, 2, -1],[2, -1 ,-1]])
new_hor=np.zeros((height,width))
new_ver=np.zeros((height,width))
new_45=np.zeros((height,width))
new_neg45=np.zeros((height,width))

def convol(img,mask):
    newI=np.zeros((len(img),len(img[0])))
    for i in range(len(img)):
        for j in range(len(img[0])):
            newI[i][j]=img[i][j]*mask[i][j]
    return newI
for i in range(1, height-1):
    for j in range(1, width-1):

        new_hor[i, j]= np.sum(convol(img[i-1:i+2,j-1:j+2],hor_mask))/9
        new_ver[i, j]= np.sum(convol(img[i-1:i+2,j-1:j+2],ver_mask))/9
        new_45[i, j]= np.sum(convol(img[i-1:i+2,j-1:j+2],deg45_mask))/9
        new_neg45[i, j]= np.sum(convol(img[i-1:i+2,j-1:j+2],degNeg45_mask))/9
        
cv.imshow("Horizontal",np.array(new_hor,dtype=np.uint8))
cv.imshow("Vertical",np.array(new_ver,dtype=np.uint8))
cv.imshow("45",np.array(new_45,dtype=np.uint8))
cv.imshow("Neg 45",np.array(new_neg45,dtype=np.uint8))



cv.waitKey(0)
cv.destroyAllWindows()