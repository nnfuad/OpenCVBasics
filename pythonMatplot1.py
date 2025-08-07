import cv2
import matplotlib.pyplot as plt

img = cv2.imread("assets/centerdiv.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis('off')
plt.show()