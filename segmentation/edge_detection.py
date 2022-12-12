import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread("hello.jpg",0)
cv.imshow("original",img)

kernelx = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv.filter2D(img, -1, kernelx)
img_prewitty = cv.filter2D(img, -1, kernely)
prewitt=img_prewittx+img_prewitty
plt.subplot(1,4,1).set_title("Prewitt")
plt.subplot(1,4,1).imshow(prewitt, cmap='gray')



#sobel
img_sobelx = cv.Sobel(img,cv.CV_8U,1,0,ksize=5)
img_sobely = cv.Sobel(img,cv.CV_8U,0,1,ksize=5)
sobel = img_sobelx + img_sobely
plt.subplot(1,4,2).set_title("Sobel")
plt.subplot(1,4,2).imshow(sobel, cmap='gray')


# Setting parameter values
t_lower = 50 # Lower Threshold
t_upper = 150 # Upper threshold

# Applying the Canny Edge filter
edge = cv.Canny(img, t_lower, t_upper)
plt.subplot(1,4,3).set_title("Canny")
plt.subplot(1,4,3).imshow(edge, cmap='gray')




# Apply Gaussian Blur
blur = cv.GaussianBlur(img,(3,3),0)

# Apply Laplacian operator in some higher datatype
laplacian = cv.Laplacian(blur,cv.CV_64F)
filtered_image = cv.convertScaleAbs(laplacian)

plt.subplot(1,4,4).set_title("LoG")
plt.subplot(1,4,4).imshow(filtered_image, cmap='gray')

plt.show()