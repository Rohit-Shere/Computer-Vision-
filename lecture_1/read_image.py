import cv2

img1 = cv2.imread('img1.jpg')
print(img1.shape)


img1 = cv2.resize(img1 , (500, 650))

cv2.imwrite("new_img.jpg", img1)

cv2.imshow('Image 1', img1)
cv2.waitKey(0)