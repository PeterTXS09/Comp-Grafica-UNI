import cv2
import os

caminhos = [os.path.join('ImagesAge/60-98',f) for f in os.listdir('ImagesAge/60-98')]

pasta = 'ImagesAge/60-98 new/'
id = 1

for img in caminhos:
    imagem = cv2.imread(img)
    imagemRedim = cv2.resize(imagem,(224,224))
    # cv2.imshow('img',imagemRedim)

    cv2.imwrite(pasta + str(id) + '.jpg',imagemRedim)
    id = id+1
    # cv2.waitKey(1)



