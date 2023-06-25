import numpy as np
import cv2
from keras.models import load_model
import mediapipe as mp
import cvzone

#tf 2.9.1
#keras 2.6.0

face = mp.solutions.face_detection
Face = face.FaceDetection()
mpDwaw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('Videos/vd06.mp4')

modelGender = load_model("model_gender.h5", compile=False)

modelAge = load_model("model_age.h5", compile=False)

classesGender=['Hombre','Mujer']
classesAge=['6-20','25-30','42-48','60-98']

while True:
    success, imgOrignal = cap.read()
    # imgOrignal = cv2.resize(imgOrignal,(1200,720))
    imgRGB = cv2.cvtColor(imgOrignal, cv2.COLOR_BGR2RGB)
    results = Face.process(imgRGB)
    facesPoints = results.detections
    hO, wO, _ = imgRGB.shape
    if facesPoints:
        for id, detection in enumerate(facesPoints):
            #mpDwaw.draw_detection(img, detection)
            bbox = detection.location_data.relative_bounding_box
            x,y,w,h = int(bbox.xmin*wO),int(bbox.ymin*hO),int(bbox.width*wO),int(bbox.height*hO)
            imgFace = imgOrignal[y:y + h, x:x + w]
            imgFace = cv2.resize(imgFace, (224, 224))
            face = np.asarray(imgFace, dtype=np.float32).reshape(1, 224, 224, 3)
            face = (face / 127.5) - 1

            predictions = modelGender.predict(face)
            indexGender = np.argmax(predictions)
            confGender = np.amax(predictions)

            predictions = modelAge.predict(face)
            indexAge = np.argmax(predictions)
            confAge = np.amax(predictions)

            # print(indexVal,probabilityValue)
            if confGender >0.30:
                cv2.rectangle(imgOrignal, (x, y), (x + w, y + h), (0,255,0), 3)
                cvzone.putTextRect(imgOrignal, str(classesGender[indexGender]), (x, y-15), 2, 3)
                cvzone.putTextRect(imgOrignal, str(round(confGender * 100, 2)) + "%", (x+130, y-15), 1.5, 2)

            if confAge > 0.40:
                cvzone.putTextRect(imgOrignal,f'Edad: {classesAge[indexAge]}',(x, y-50),2,3)


    cv2.imshow("Result", imgOrignal)
    cv2.waitKey(15)

