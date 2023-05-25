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
    gluOrtho2D(-320, 320, -400, 400)

def plotearGrafico():
    glBegin(GL_POINTS)
    glVertex2f(100,200)
    glEnd()

def DibujarEstrella(x, y, tamanio):
    glPointSize(tamanio)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


Fin = False
inicializar_Ortografica()
glPointSize(5)
while not Fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fin = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    DibujarEstrella(50, 50, 10)
    DibujarEstrella(100, 50, 5)
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()

