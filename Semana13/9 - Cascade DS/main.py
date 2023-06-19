import cv2

video = cv2.VideoCapture(0)

index = 1

while True:
    check, img = video.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    if cv2.waitKey(1):
        imgR = cv2.resize(imgGray, (220, 220))
        cv2.imwrite(f'train/p/{index}.jpg', imgR)
        index += 1

    cv2.imshow('Captura', img)
    cv2.waitKey(1)