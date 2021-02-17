import cv2
import sys

img = cv2.imread('039.png', cv2. IMREAD_UNCHANGED)

if img is None :
    print('Image load failed!')
    sys.exit()

#print(type(img))
#print(img.shape)
#print(img.dtype)


cv2.namedWindow('banana image')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
