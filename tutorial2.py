import cv2
import random

img = cv2.imread('assets/centerdiv.jpg', 1)
print(img)

for i in range(100):
    for j in range(img.shape[0]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imwrite('new_img2.jpg', img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

	# •	Loads an image (centerdiv.jpg) in color mode (1).
	# •	Prints the image matrix and its shape.
	# •	Alters the first 100 rows of every column by filling each pixel with random RGB values.
	# •	Saves the new image as new_img2.jpg.
	# •	Displays the modified image in a window.
 
import cv2
import random

img = cv2.imread('assets/centerdiv.jpg', 1)
print(img)
height, width, _ = img.shape

for i in range(height-100, height):
    for j in range(width):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imwrite('new_img2.jpg', img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

	# •	height - 100 to height: selects the bottom 100 rows.
	# •	j in range(width): loops through all pixels in each row.
	# •	img[i][j] = [B, G, R]: assigns random color to each pixel.