import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

mano = mp.solutions.hands
Mano = mano.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    if not check:
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Mano.process(imgRGB)
    handPoints = results.multi_hand_landmarks
    h,w, _ = img.shape
    puntos = []
    if handPoints:
        for points in handPoints:
            mpDraw.draw_landmarks(img, points, mano.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x*w), int(cord.y*w)
                #cv2.putText(img, str(id), (cx, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
                puntos.append((cx, cy))

        dedos = [8, 12, 16, 20]
        contador = 0
        if points:
            if puntos[4][0] < puntos[2][0]:
                contador += 1
            for x in dedos:
                if puntos[x][1] < puntos[x-2][1]:
                    contador +=1

        cv2.rectangle(img, (80, 10), (200, 100), (255,0,0), -1)
        cv2.putText(img, str(contador), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 5)



    cv2.imshow('Imagen', img)
    cv2.waitKey(1)