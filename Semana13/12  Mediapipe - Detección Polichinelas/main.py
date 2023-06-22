import math

import cv2
import mediapipe as mp

video = cv2.VideoCapture('polichinelas.mp4')
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils
contador = 0
check = True

while True:
    success, img = video.read()
    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRGB)
    points = results.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    # https://developers.google.com/mediapipe/solutions/vision/pose_landmarker

    h, w, _ = img.shape

    if points:
        pieDY = (points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y)
        pieDX = (points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x)
        pieIY = (points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y)
        pieIX = (points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x)
        manoDY = (points.landmark[pose.PoseLandmark.RIGHT_INDEX].y)
        manoDX = (points.landmark[pose.PoseLandmark.RIGHT_INDEX].x)
        manoIY = (points.landmark[pose.PoseLandmark.LEFT_INDEX].y)
        manoIX = (points.landmark[pose.PoseLandmark.LEFT_INDEX].x)

        dist_manos = math.hypot(manoDX - manoIX, manoDY - manoIY)
        dist_pies = math.hypot(pieDX - pieIX, pieDY - pieIY)
        print(f'manos:{dist_manos} pies:{dist_pies}')

        if check == True and dist_manos <= 0.07 and dist_pies >= 0.14:
            check = False
            contador += 1
        if dist_manos > 0.07 and dist_pies < 0.14:
            check = True
        #print(contador)

    cv2.imshow('Resultado', img)
    cv2.waitKey(40)