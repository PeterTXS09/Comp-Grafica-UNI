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

def GuardarDibujo():
    f = open("mi_dibujo.txt", "w")
    f.write(str(len(puntos)) + "\n") #longitud de lineas
    for l in puntos:
        f.write(str(len(l)) + "\n") #cuantas coordenadas tiene una linea
        for coordenadas in l:
            f.write(str(coordenadas[0]) + " " + str(coordenadas[1]) + "\n") # las coordenadas de puntos que conforman la linea
    f.close()
    print("Dibujo guardado")

def CargarDibujo():
    f = open("mi_dibujo.txt", "r")
    total_lineas = int(f.readline())
    global puntos
    global line
    puntos = []
    for l in range(total_lineas):
        line = []
        puntos.append(line)
        total_coordenadas = int(f.readline())
        for coordenada in range(total_coordenadas):
            px, py = [float(value) for value in next(f).split()]
            line.append((px,py))
            print(str(px) + "," + str(py))


def map_value(current_min, current_max, new_min, new_max, value):
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min)/current_range)

puntos = []
line = []
mouse_down = False

Fin = False
inicializar_Ortografica()
glPointSize(10)
while not Fin:
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fin = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                GuardarDibujo()
            elif event.key == pygame.K_c:
                CargarDibujo()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            line = []
            puntos.append(line)
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down:
            pos = pygame.mouse.get_pos()
            line.append((map_value(0, ancho, 0, ort_ancho, pos[0]),
                        map_value(0, alto, ort_alto, 0, pos[1])))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_linea()
    pygame.display.flip()
    pygame.time.wait(1)

pygame.quit()

