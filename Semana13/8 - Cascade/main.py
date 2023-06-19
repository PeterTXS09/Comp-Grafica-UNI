import cv2

cam = cv2.VideoCapture(0)
clasificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

while True:
    check, img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    objetos = clasificador.detectMultiScale(imgGray, minSize=(50,50), scaleFactor=1.5)
    # print(objetos)
    for x, y, l, a in objetos:
        cv2.rectangle(img, (x,y), (x+l, y+a), (255,0,0), 2)
    cv2.imshow('Imagen', img)
    cv2.waitKey(1)