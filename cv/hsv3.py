import sys
import numpy as np
import cv2

#frame = cv2.imread('032.png')
frame = cv2.imread('039.png')

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Yellow color
low_yellow = np.array([15, 80, 70])
#low_yellow = np.array([0, 80, 70])
high_yellow = np.array([255, 255, 255]) #gbr
yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

# Every color except white
low = np.array([0, 42, 0])
high = np.array([179, 255, 255])
mask = cv2.inRange(hsv_frame, low, high)
result = cv2.bitwise_and(frame, frame, mask=mask)

# Every color except white & Green
low2 = np.array([195,159,28])
high2 = np.array([244,231,94])
mask2 = cv2.inRange(hsv_frame, low2, high2)
result2 = cv2.bitwise_and(frame, frame, mask=mask)

cv2.imshow('Image', frame)
cv2.imshow('Yellow mask', yellow)
cv2.imshow('Result', result2)
cv2.waitKey(0)
cv2.destroyAllWindows()