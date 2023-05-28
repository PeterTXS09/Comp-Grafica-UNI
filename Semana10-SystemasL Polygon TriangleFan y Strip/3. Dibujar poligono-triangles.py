import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

ancho = 1000
alto = 800
ort_ancho = 640
ort_alto = 800

pantalla = pygame.display.set_mode((ancho, alto), DOUBLEBUF | OPENGL)
#colocar titulo:
pygame.display.set_caption('Graficos en OpenGL')

def inicializar_Ortografica():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ort_ancho, 0, ort_alto)

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

def plot_linea():
    for l in puntos:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()


def map_value(current_min, current_max, new_min, new_max, value):
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min)/current_range)


def plot_poligono():
    glColor(0.2,0.2,0.2,1)
    glBegin(GL_POLYGON) #GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP
    for p in puntos:
        glVertex2f(p[0], p[1])
    glEnd()
    glColor(0.5,0.5,0.5,1)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    for p in puntos:
        glVertex2f(p[0], p[1])
    glEnd()


puntos = []
mouse_down = False
Fin = False
inicializar_Ortografica()

while not Fin:
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fin = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                puntos = []
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            puntos.append((map_value(0, ancho, 0, ort_ancho, pos[0]),
                        map_value(0, alto, ort_alto, 0, pos[1])))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #plot_linea()
    plot_poligono()
    pygame.display.flip()
    pygame.time.wait(1)

pygame.quit()

