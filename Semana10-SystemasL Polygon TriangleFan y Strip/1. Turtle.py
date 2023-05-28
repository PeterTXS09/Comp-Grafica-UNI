import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

ancho_pantalla = 800
largo_pantalla = 800
orto_izquierda = -400
orto_derecha = 400
orto_arriba = -400
orto_abajo = 400

pantalla = pygame.display.set_mode( (ancho_pantalla, largo_pantalla), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graficos en Turtle')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(orto_izquierda, orto_derecha, orto_arriba, orto_abajo)

def z_rotation(vector, theta):
    new_vector = np.array([ [np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0,0,1]])
    return np.dot(new_vector, vector)

posicion_actual = (0,0)
direccion = np.array([0,1,0])

def line_to(x,y):
    global posicion_actual
    glBegin(GL_LINE_STRIP)
    glVertex2f(posicion_actual[0], posicion_actual[1])
    glVertex2f(x,y)
    posicion_actual = (x,y)
    glEnd()

def move_to(x,y):
    global posicion_actual
    posicion_actual = (x,y)

def reset_turtle():
    global posicion_actual, direccion
    posicion_actual = (0, 0)
    direccion = np.array([0, 1, 0])

def draw_turtle():
    for i in range(20):
        forward(50)
        rotate(22)

def forward(longitud):
    nuevo_x = posicion_actual[0] + direccion[0] * longitud
    nuevo_y = posicion_actual[1] + direccion[1] * longitud
    line_to(nuevo_x, nuevo_y)

def rotate(angulo):
    global direccion
    direccion = z_rotation(direccion, math.radians(angulo))


init_ortho()
Finalizar = False
glLineWidth(5)
while not Finalizar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Finalizar = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glBegin(GL_POINTS)
    glVertex2f(0,0)
    glEnd()
    reset_turtle()
    draw_turtle()

    pygame.display.flip()
pygame.quit()