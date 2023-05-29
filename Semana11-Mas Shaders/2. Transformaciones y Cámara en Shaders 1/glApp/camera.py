import numpy as np
import pygame
from OpenGL.GLU import *
from math import *
from .Transformation import *
from .Uniform import *

class Camera:
    def __init__(self, program_id, w, h):
        # self.eye = pygame.math.Vector3(0, 0, 0)
        # self.up = pygame.math.Vector3(0, 1, 0)
        # self.right = pygame.math.Vector3(1, 0, 0)
        # self.forward = pygame.math.Vector3(0, 0, 1)
        # self.look = self.eye + self.forward
        self.transformation = identity_matrix()
        # self.yaw = -90
        # self.pitch = 0
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivityX = 0.1
        self.mouse_sensitivityY = 0.1
        self.key_sensitivity = 0.008
        self.projection_mat = self.perspective_mat(60, w / h, 0.01, 10000)
        self.projection = Uniform("mat4", self.projection_mat)
        self.projection.find_variable(program_id, "projection_mat")
        self.screen_width = w
        self.screen_height = h
        self.program_id = program_id

    def perspective_mat(self, angle_of_view, aspect_ratio, near_plane, far_plane):
        a = radians(angle_of_view)
        d = 1.0 / tan(a / 2.0)
        r = aspect_ratio
        b = (far_plane + near_plane) / ( near_plane - far_plane)
        c = far_plane * near_plane / ( near_plane - far_plane)
        return np.array([[d/r, 0,  0, 0],
                         [0  , d,  0, 0],
                         [0  , 0,  b, c],
                         [0  , 0, -1, 0]], np.float32)

    def rotate(self, yaw, pitch):
        self.transformation = rotate(self.transformation, yaw, "y")
        self.transformation = rotate(self.transformation, pitch, "x")
        # self.yaw += yaw
        # self.pitch += pitch
        #
        # if self.pitch > 89.0:
        #     self.pitch = 89.0
        #
        # if self.pitch < -89.0:
        #     self.pitch = 89.0
        #
        # self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        # self.forward.y = sin(radians(self.pitch))
        # self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))
        # self.forward = self.forward.normalize()
        # self.right = self.forward.cross(pygame.math.Vector3(0, 1, 0)).normalize()
        # self.up = self.right.cross(self.forward).normalize()

    def update(self):
        if pygame.mouse.get_visible():
            return

        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        # print("Mouse Change: " + str(mouse_change[0]) + ", " + str(mouse_change[1]))
        pygame.mouse.set_pos(self.screen_width / 2, self.screen_height / 2)
        self.last_mouse = pygame.mouse.get_pos()
        self.rotate(mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.transformation = translate(self.transformation, 0, 0, self.key_sensitivity)
        if keys[pygame.K_UP]:
            self.transformation = translate(self.transformation, 0, 0, -self.key_sensitivity)
        if keys[pygame.K_RIGHT]:
            self.transformation = translate(self.transformation, self.key_sensitivity, 0, 0)
        if keys[pygame.K_LEFT]:
            self.transformation = translate(self.transformation, -self.key_sensitivity, 0, 0)

        # self.look = self.eye + self.forward
        # gluLookAt(self.eye.x, self.eye.y, self.eye.z,
        #           self.look.x, self.look.y, self.look.z,
        #           self.up.x, self.up.y, self.up.z)

        self.projection.load()
        lookat_mat = self.transformation
        lookat = Uniform("mat4", lookat_mat)
        lookat.find_variable(self.program_id, "view_mat")
        lookat.load()

