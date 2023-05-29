from OpenGL.GL import *
import pygame
from Graphics_Data import *
import numpy as np


class Mesh02:
    def __init__(self, program_id, vertices, vertex_colors, draw_type):
        self.vertices = vertices
        self.draw_type = draw_type
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        position = Graphics_Data("vec3", self.vertices)
        position.create_variable(program_id, "position")
        colors = Graphics_Data("vec3", vertex_colors)
        colors.create_variable(program_id, "vertex_color")

    def draw(self):
        glBindVertexArray(self.vao_ref)
        glDrawArrays(self.draw_type, 0, len(self.vertices))
