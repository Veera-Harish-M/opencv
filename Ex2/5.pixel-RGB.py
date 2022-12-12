'''5. Read an image and display its RGB plane value at a particular pixel location.'''

import cv2 as cv

img1=cv.imread("test.jfif")

height, width, channels = img1.shape
print(height,width,channels)

pixel1=int(input("Enter pixel1:"))
pixel2=int(input("Enter pixel2:"))
if(pixel1<height and pixel2<width):
    R,G,B=img1[pixel1,pixel2]
    print(f"Red:{R},Green:{G},Blue:{B}")
else:
    print("Entered values are out of the range")
    
cv.waitKey(0)

cv.destroyAllWindows()