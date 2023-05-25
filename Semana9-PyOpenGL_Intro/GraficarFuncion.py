import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init()

ancho = 1000
alto = 800

pantalla = pygame.display.set_mode((ancho, alto), DOUBLEBUF | OPENGL)
#colocar titulo:
pygame.display.set_caption('Graficos en OpenGL')

def inicializar_Ortografica():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 5, -1, 1)

def plotearGrafico():
    glBegin(GL_POINTS)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 5, 0.00005):
        py = math.exp(-px) * math.cos(2*math.pi * px)
        glVertex2f(px, py)
    glEnd()

def DibujarEstrella(x, y, tamanio):
    glPointSize(tamanio)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


Fin = False
inicializar_Ortografica()
glPointSize(4)
while not Fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fin = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plotearGrafico()
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()

