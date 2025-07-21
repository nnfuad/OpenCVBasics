import cv2

import cv2
print(cv2.__version__)

img = cv2.imread('assets/centerdiv.jpg', -1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


cv2.imshow('Image', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

	# Read the image
	# Resize it to 50%
	# Rotate it 90° counter-clockwise
	# Show it in a window for 10 seconds