import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    return texture_id

def load_obj(filename):
    vertices = []
    textures = []
    normals = []
    faces = []

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertices.append(list(map(float, line[2:].split())))
            elif line.startswith('vt '):
                textures.append(list(map(float, line[3:].split())))
            elif line.startswith('vn '):
                normals.append(list(map(float, line[3:].split())))
            elif line.startswith('f '):
                faces.append([list(map(int, vertex.split('/'))) for vertex in line[2:].split()])

    return vertices, textures, normals, faces

def init(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    # link: https://stackoverflow.com/questions/9262351/opengl-cube-not-rendering-properly
    # faceculling: https://learnopengl.com/Advanced-OpenGL/Face-culling
    glEnable(GL_CULL_FACE)

def draw(vertices, textures, normals, faces):
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_data in face:
            vertex_index, texture_index, normal_index = vertex_data
            vertex = vertices[vertex_index - 1]
            texture = textures[texture_index - 1]
            normal = normals[normal_index - 1]

            glTexCoord2fv(texture)
            glNormal3fv(normal)
            glVertex3fv(vertex)
    glEnd()

def main():
    width, height = 800, 600
    obj_file = 'cube.obj'
    texture_file = 'crate.png'

    init(width, height)
    vertices, textures, normals, faces = load_obj(obj_file)
    texture_id = load_texture(texture_file)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        draw(vertices, textures, normals, faces)
        glDisable(GL_TEXTURE_2D)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
