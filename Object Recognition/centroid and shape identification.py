import cv2 as cv
import numpy as np

# change it with your absolute path for the image
image = cv.imread("shape.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5, 5),
					cv.BORDER_DEFAULT)
ret, thresh = cv.threshold(blur, 127, 255,
						cv.THRESH_BINARY_INV)


cv.imshow("thresh.png",thresh)


contours, hierarchies = cv.findContours(
	thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
blank = np.zeros(thresh.shape[:2],
				dtype='uint8')

cv.drawContours(blank, contours, -1,
				(255, 0, 0), 1)

cv.imshow("Contours.png", blank)



for i in contours:
	approx = cv.approxPolyDP(
        i, 0.01 * cv.arcLength(i, True), True)
	M = cv.moments(i)
	if M['m00'] != 0:
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		cv.drawContours(image, [i], -1, (0, 255, 0), 2)
		cv.circle(image, (cx, cy), 7, (0, 0, 255), -1)
		cv.putText(image, "", (cx - 20, cy - 20),
				cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
		if len(approx) == 3:
			cv.putText(image, 'Triangle', (cx, cy),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		elif len(approx) == 4:
			cv.putText(image, 'Quadrilateral', (cx, cy),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		elif len(approx) == 5:
			cv.putText(image, 'Pentagon', (cx, cy),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		elif len(approx) == 6:
			cv.putText(image, 'Hexagon', (cx,cy),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		else:
			cv.putText(image, 'circle', (cx, cy),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  

		
	print(f"x: {cx} y: {cy}")


cv.imshow("image.png", image)
cv.waitKey(0)
cv.destroyAllWindows()