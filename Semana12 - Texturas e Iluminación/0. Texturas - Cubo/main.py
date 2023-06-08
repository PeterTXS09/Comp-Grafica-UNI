import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def load_texture(file_name):
    texture_surface = pygame.image.load(file_name)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    glEnable(GL_TEXTURE_2D)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    return texture_id

def draw_cube(texture_id):
    glBegin(GL_QUADS)
    # Front Face
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    """# Back Face
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Top Face
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)

    # Bottom Face
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # Right face
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Left Face
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)"""

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    cube_texture = load_texture("cube_texture.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube(cube_texture)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
