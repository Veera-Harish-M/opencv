#resizing an image size reducing it and enlarging the same 

import cv2
 
img = cv2.imread('hello.jpg')
cv2.imshow("1024*1024",img)
  
# resize image
resized512 = cv2.resize(img, (512,512))
cv2.imshow("512*512",resized512)

resized256 = cv2.resize(img, (256,256))
cv2.imshow("256*256",resized256)

resized128 = cv2.resize(img, (128,128))
cv2.imshow("128*128",resized128)

resized64 = cv2.resize(img, (64,64))
cv2.imshow("64*64",resized64)

resized32 = cv2.resize(img, (32,32))
cv2.imshow("32*32",resized32)

#------------


resize64 = cv2.resize(resized32, (64,64))
cv2.imshow("Max:64*64",resize64)

resize128 = cv2.resize(resize64, (128,128))
cv2.imshow("Max:128*128",resize128)

resize256 = cv2.resize(resize128, (256,256))
cv2.imshow("Max:256*256",resize256)

resize512 = cv2.resize(resize256, (512,512))
cv2.imshow("Max:512*512",resize512)

resize1024 = cv2.resize(resize512, (1024,1024))
cv2.imshow("Max:1024*1024",resize1024)


cv2.waitKey(0)
cv2.destroyAllWindows()
