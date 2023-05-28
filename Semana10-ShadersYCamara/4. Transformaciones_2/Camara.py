import pygame
from OpenGL.GLU import *
from math import *

class Camara:
    def __init__(self):
        self.eye = pygame.math.Vector3(0, 0, 0)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.look = self.eye + self.forward
        self.yaw = -90
        self.pitch = 0
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivityX = 0.1
        self.mouse_sensitivityY = 0.1

    def rotatate(self, yaw, pitch):
        self.yaw += yaw
        self.pitch += pitch

        if self.pitch > 89.0:
            self.pitch = 89.0

        if self.pitch < -89.0:
            self.pitch = 89.0

        self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward.y = sin(radians(self.pitch))
        self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward = self.forward.normalize()
        self.right = self.forward.cross(pygame.math.Vector3(0, 1, 0)).normalize()
        self.up = self.right.cross(self.forward).normalize()

    def update(self, w, h):
        if pygame.mouse.get_visible():
            return

        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)

        pygame.mouse.set_pos(w / 2, h / 2)

        self.last_mouse = pygame.mouse.get_pos()

        self.rotatate(-mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.eye -= self.forward * self.mouse_sensitivityX
        if keys[pygame.K_UP]:
            self.eye += self.forward * self.mouse_sensitivityX
        if keys[pygame.K_RIGHT]:
            self.eye += self.right * self.mouse_sensitivityX
        if keys[pygame.K_LEFT]:
            self.eye -= self.right * self.mouse_sensitivityX

        self.look = self.eye + self.forward
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.look.x, self.look.y, self.look.z,
                  self.up.x, self.up.y, self.up.z)