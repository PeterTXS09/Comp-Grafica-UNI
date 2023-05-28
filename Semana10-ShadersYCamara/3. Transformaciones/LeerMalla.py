from OpenGL.GL import *
from Mallas import *
import pygame

class LeerMalla(Malla):

    def __init__(self, nombre, tipo_dibujo):
        self.vertices = []
        self.triangulos = []
        self.nombre = nombre
        self.tipo_dibujo = tipo_dibujo
        self.cargar_dibujo()

    def cargar_dibujo(self):
        with open(self.nombre) as f:
            linea = f.readline()
            while linea:
                if linea[:2] == "v ":
                    vx, vy, vz = [float(value) for value in linea[2:].split()]
                    self.vertices.append((vx, vy, vz))
                if linea[:2] == "f ":
                    t1, t2, t3, *r = [value for value in linea[2:].split()]
                    self.triangulos.append([int(value) for value in t1.split('/')][0] - 1)
                    self.triangulos.append([int(value) for value in t2.split('/')][0] - 1)
                    self.triangulos.append([int(value) for value in t3.split('/')][0] - 1)
                linea = f.readline()
