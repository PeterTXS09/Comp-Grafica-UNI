import cv2
import mediapipe as mp
import math
import time

video = cv2.VideoCapture(0)
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
mpDraw = mp.solutions.drawing_utils
estado = 'X'
inicio = 0
estado_actual = ''

while True:
    check, img = video.read()
    img = cv2.resize(img, (1000, 720))
    if not check:
        break
    results = faceMesh.process(img)
    h, w, _ = img.shape

    if results:
        if not results.multi_face_landmarks:
            continue
        for face in results.multi_face_landmarks:
            #print(face)
            # mpDraw.draw_landmarks(img, face, mpFaceMesh.FACEMESH_FACE_OVAL)
            d1x, d1y = int((face.landmark[159].x)*w), int((face.landmark[159].y)*h)
            d2x, d2y = int((face.landmark[145].x) * w), int((face.landmark[145].y) * h)
            i1x, i1y = int((face.landmark[386].x) * w), int((face.landmark[386].y) * h)
            i2x, i2y = int((face.landmark[374].x) * w), int((face.landmark[374].y) * h)

            distD = math.hypot(d1x - d2x, d1y - d2y)
            distI = math.hypot(i1x - i2x, i1y - i2y)


            # print(f'distD: {distD}, distI: {distI}')
            if distI <= 15 and distD <= 15:
                print('ojos cerrados')
                cv2.rectangle(img, (100, 30), (390, 80), (0,0,255), -1)
                cv2.putText(img, 'OJOS CERRADOS', (105,65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255, 255), 3)
                estado = 'Dormido'
                if estado != estado_actual:
                    inicio = time.time()
            else:
                print('ojos abiertos')
                cv2.rectangle(img, (100, 30), (390, 80), (255, 0, 0), -1)
                cv2.putText(img, 'OJOS ABIERTOS', (105, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
                estado = 'Despierto'
                inicio = time.time()
                tiempo = int(time.time() - inicio)

            if estado == 'Dormido':
                tiempo = int(time.time() - inicio)

            if tiempo >= 2:
                cv2.rectangle(img, (300, 150), (850, 220), (0,0,255), -1)
                cv2.putText(img, f'DORMIDO: {tiempo} SEG', (310, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255, 255, 255), 5)
            estado_actual = estado
    cv2.imshow('Detector', img)
    cv2.waitKey(10)