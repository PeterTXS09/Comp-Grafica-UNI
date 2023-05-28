from OpenGL.GL import *
from Mallas import *
import pygame

class LeerMalla(Malla):

    def __init__(self, file_name, draw_type, position=pygame.Vector3(0, 0, 0), rotation=Rotation(0, pygame.Vector3(0, 1, 0)), scale=pygame.Vector3(1, 1, 1) ):
        self.file_name = file_name
        vertices, triangles = self.cargar_dibujo()
        self.tipo_dibujo = draw_type
        super().__init__(vertices, triangles, draw_type, position, rotation, scale)

    def cargar_dibujo(self):
        vertices = []
        triangulos = []
        with open(self.file_name) as f:
            linea = f.readline()
            while linea:
                if linea[:2] == "v ":
                    vx, vy, vz = [float(value) for value in linea[2:].split()]
                    vertices.append((vx, vy, vz))
                if linea[:2] == "f ":
                    t1, t2, t3, *r = [value for value in linea[2:].split()]
                    triangulos.append([int(value) for value in t1.split('/')][0] - 1)
                    triangulos.append([int(value) for value in t2.split('/')][0] - 1)
                    triangulos.append([int(value) for value in t3.split('/')][0] - 1)
                linea = f.readline()
        return vertices, triangulos

