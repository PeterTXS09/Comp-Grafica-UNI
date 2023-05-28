from OpenGL.GL import *
import pygame

class Malla:

    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (-0.5, -0.5, -0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (-0.5, -0.5, -0.5),
                         (-0.5, -0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (-0.5, 0.5, -0.5),
                         (-0.5, -0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (0.5, 0.5, -0.5),
                         (0.5, 0.5, 0.5),
                         (0.5, -0.5, 0.5)]

        self.triangulos = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
                           13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]

        self.tipo_dibujo = GL_LINE_LOOP

    def Dibujar(self):
        for t in range(0, len(self.triangulos), 3):
            glBegin(self.tipo_dibujo)
            glVertex3fv(self.vertices[self.triangulos[t]])
            glVertex3fv(self.vertices[self.triangulos[t+1]])
            glVertex3fv(self.vertices[self.triangulos[t+2]])
            glEnd()
