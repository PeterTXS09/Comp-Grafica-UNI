import cv2

# id de la cámara
cam = cv2.VideoCapture(0)

# configuraciones adicionales
# link de referencia: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a8c6d8c2d37505b5ca61ffd4bb54e9a7c
cam.set(3, 30) # largo
cam.set(2, 20) # alto
cam.set(10, 500) # brillo / luminosidad

while True:
    check, img = cam.read()
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('Q'):
        break