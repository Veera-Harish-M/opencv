
import cv2 as cv
from sympy import fwht
import numpy as np

img=cv.imread("cat.jpg",0)
cv.imshow("original",img)
print(img)
height, width = img.shape

n = int(input("Enter N:"))
H= np.ones((n, n), dtype=int)

i1 = 1
while i1 < n:
    for i2 in range(i1):
        for i3 in range(i1):
            H[i2+i1][i3]    = H[i2][i3]
            H[i2][i3+i1]    = H[i2][i3]
            H[i2+i1][i3+i1] = -1 if H[i2][i3]==1 else 1
    i1 += i1
print(H)
ch={}
for i in H:
    c=0
    for j in range(0,n-1):
        if(i[j-1]!=i[j-2]):
            c+=1
    ch[c]=i
print(ch)

for i in range(n):
    H[i]=ch[i]
print(H)
img_new = np.zeros([height, width])
 
for i in range(0, height-n,n-1):
    for j in range(0, width-n,n-1):
        img_new[i:i+n,j:j+n]=img[i:i+n,j:j+n]*H*H
print(img_new)
        


cv.imshow("transform",np.array(img_new,dtype=np.uint8))
cv.imwrite('final_test.jpg', img_new)

cv.waitKey(0)

cv.destroyAllWindows()