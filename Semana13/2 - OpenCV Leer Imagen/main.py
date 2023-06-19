import cv2

img = cv2.imread('uni.jpeg')

# blanco y negro:
img_bn = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('UNI', img)
# mostrar la imagen:
cv2.imshow('UNI Blanco y Negro',img_bn)
cv2.waitKey(0)
