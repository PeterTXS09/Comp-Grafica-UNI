import cv2

video = cv2.VideoCapture()
# https://play.google.com/store/apps/details?id=com.pas.webcam&hl=es&gl=US
# Descargar IP Webcam
# debe estar en la misma red

ip = "https://192.168.18.5:4747/video"
video.open(ip)

while True:
    check, img = video.read()
    cv2.imshow("Video", img)
    cv2.waitKey(1)