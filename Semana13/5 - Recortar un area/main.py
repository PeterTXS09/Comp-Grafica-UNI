import cv2

img = cv2.imread('uni.jpeg')
dim = cv2.selectROI('Seleccione area de recorte', img, False)

d1, d2, d3, d4 = dim

recorte = img[d2:d2+d4, d1:d1+d3]
cv2.imshow('Imagen Original', img)
cv2.imshow('Recorte', recorte)

cv2.waitKey(0)