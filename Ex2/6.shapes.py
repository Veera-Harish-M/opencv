'''6. Draw the following geometrical shapes — (a) Line (b) Circle (c) Rectangle'''

import cv2 as cv
import numpy as np

Imgblack = np.zeros((200, 200, 3), dtype='uint8')
line=cv.line(Imgblack, (100,100), (150,150), (255,255,255), 3)
cv.imshow("line",line)
circle = cv.circle(Imgblack, (125,125), 10, (255,0,0), 3)
cv.imshow("circle",circle)
rect=cv.rectangle(Imgblack, (40,40), (130,180), (0,0,255), 5)
cv.imshow("rect",rect)
cv.waitKey(0)

cv.destroyAllWindows()