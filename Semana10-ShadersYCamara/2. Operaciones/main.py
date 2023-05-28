import pygame, os
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cubo import *
from LeerMalla import *
from Camara import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
# x= 850
# y = 200
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (x, y)

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')
cube = Cubo(GL_LINE_LOOP, position=pygame.Vector3(2, 0, 0), rotation=Rotation(45, pygame.Vector3(0, 1, 0)), scale=pygame.Vector3(0.5, 0.5, 0.5))
cube2 = Cubo(GL_LINE_LOOP, position=pygame.Vector3(2, 0, 0), rotation=Rotation(45, pygame.Vector3(0, 1, 0)), scale=pygame.Vector3(2, 2, 2))
# mesh = LoadMesh("../objects/teapot.obj", GL_LINE_LOOP, rotation=Rotation(45, pygame.Vector3(1, 1, 0)), scale=pygame.Vector3(0.1, 0.1, 0.1))
camera = Camara()


def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 1000.0)

def camera_init():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    camera.update(screen.get_width(), screen.get_height())

def draw_world_axes():
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex3d(-1000, 0, 0)
    glVertex3d(1000, 0, 0)
    glColor(0, 1, 0)
    glVertex3d(0, -1000, 0)
    glVertex3d(0, 1000, 0)
    glColor(0, 0, 1)
    glVertex3d(0, 0,-1000)
    glVertex3d(0, 0, 1000)
    glEnd()


    sphere = gluNewQuadric()

    # x pos sphere
    glColor(1, 0, 0)
    glPushMatrix()
    glTranslated(1, 0, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # y pos sphere
    glColor(0, 1, 0)
    glPushMatrix()
    glTranslated(0, 1, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # z pos sphere
    glColor(0, 0, 1)
    glPushMatrix()
    glTranslated(0, 0, 1)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    glLineWidth(1)
    glColor(1, 1, 1)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera_init()
    draw_world_axes()
    #mesh.draw()
    glRotatef(45, 0, 0, 1)
    cube.draw()
    cube2.draw()


done = False
initialise()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)
            if event.key == K_SPACE:
                pygame.mouse.set_visible(False)
                pygame.event.set_grab(True)
    display()
    pygame.display.flip()
    #pygame.time.wait(60);
pygame.quit()