import cv2

img = cv2.imread('uni.jpeg')
dim = cv2.selectROI('Seleccione area de recorte', img, False)
cv2.destroyWindow('Seleccione area de recorte')

d1, d2, d3, d4 = dim

recorte = img[d2:d2+d4, d1:d1+d3]

directorio = 'Imagenes'
nombre_archivo = input('Ingrese nombre del archivo')
cv2.imwrite(f'{directorio}/{nombre_archivo}.jpg', recorte)
