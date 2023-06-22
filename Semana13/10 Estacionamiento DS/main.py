import cv2
import pickle

img = cv2.imread('estacionamiento.png')

espacios = []

for x in range(69):
    espacio = cv2.selectROI('espacio', img, False)
    cv2.destroyWindow('espacio')
    espacios.append(espacio)

    for x, y, w, h in espacios:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

with open('espacios.pkl','wb') as file:
    pickle.dump(espacios, file)