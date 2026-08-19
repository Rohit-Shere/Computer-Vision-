import cv2

img = cv2.imread('new_img.jpg')

resizing = cv2.resize(img, (400,600))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurring = cv2.GaussianBlur(img, (5,5),0)
edges = cv2.Canny(img, 220, 220)

cv2.imshow('Resized Image', resizing)
cv2.imshow('Grey Image', grey)
cv2.imshow('Blurring Image', blurring)
cv2.imshow("Edges Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()