import cv2

img = cv2.imread('cat.jpg')
cv2.imshow('Original', img)

image_blurred = cv2.blur(src=img, ksize=(5, 5))
cv2.imshow('blured image', image_blurred)

cv2.waitKey()
cv2.destroyAllWindows()