import pygame
from glApp.PyOGApp import *
import numpy as np
from glApp.Utils import *
from OpenGL.arrays.vbo import VBO
from glApp.Graphics_Data import *
from glApp.Square import *
from glApp.Triangle import *
from glApp.Axes import *

vertex_shader = r'''
#version 330 core

in vec3 position;
in vec3 vertex_color;
uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;
out vec3 color;

void main() {

    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position, 1.0);
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core

in vec3 color;
out vec4 FragColor;
void main() {

    FragColor = vec4(color, 1.0f);
}
'''

class Projections(PyOGApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        # self.vao_ref = None
        # self.vertex_count = 0
        self.square = None
        self.triangle = None
        self.axes = None



    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id, pygame.Vector3(-0.5, 0.5, 0.0))
        self.triangle = Triangle(self.program_id, pygame.Vector3(0.5, -0.5, 0.0))
        self.axes = Axes(self.program_id, pygame.Vector3(0.0, 0.0, 0.0))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)

        # self.vao_ref = glGenVertexArrays(1)
        # glBindVertexArray(self.vao_ref)
        # glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        # glPointSize(10)
        # position_data = [[ 0.0, -0.9, 0.0],
        #                  [-0.6,  0.8, 0.0],
        #                  [ 0.9, -0.2, 0.0],
        #                  [-0.9, -0.2, 0.0],
        #                  [ 0.6,  0.8, 0.0]]
        # self.vertex_count = len(position_data)
        # position_variable = Graphics_Data("vec3", position_data)
        # position_variable.create_variable(self.program_id, "position")
        #
        # color_data = [[1.0, 0.0, 0.0],
        #               [0.0, 1.0, 0.0],
        #               [0.0, 0.0, 1.0],
        #               [1.0, 1.0, 0.0],
        #               [1.0, 0.0, 1.0]]
        # color_variable = Graphics_Data("vec3", color_data)
        # color_variable.create_variable(self.program_id, "vertex_color")


    def camera_init(self):
        pass

    def display(self):
        # glLineWidth(10)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        self.square.draw()
        self.triangle.draw()
        self.axes.draw()
        # glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count)

Projections().mainloop()