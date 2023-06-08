from glApp.PyOGApp import *
from glApp.Utils import *
from glApp.Square import *
from glApp.Triangle import *
from glApp.Axes import *
from glApp.Cube import *
from glApp.LoadMesh import *


vertex_shader = r'''
#version 330 core
in vec3 position;
in vec3 vertex_color;
uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;
out vec3 color;
void main()
{
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position,1);
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core
in vec3 color;
out vec4 frag_color;
void main()
{
    frag_color = vec4(color, 1);
}
'''


class Projections(PyOGLApp):

    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.square = None
        self.triangle = None
        self.axes = None
        self.cube = None
        self.teapot = None

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id, pygame.Vector3(-1, 1, 0))
        self.triangle = Triangle(self.program_id, pygame.Vector3(0.5, -0.5, 0))
        self.axes = Axes(self.program_id, pygame.Vector3(0, 0, 0))
        self.cube = Cube(self.program_id)
        self.teapot = LoadMesh("models/teapot.obj", self.program_id,
                               scale=pygame.Vector3(5, 10, 5),
                               rotation=Rotation(45, pygame.Vector3(1, 0, 1)))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        #self.square.draw()
        #self.triangle.draw()
        self.axes.draw()
        #self.cube.draw()
        self.teapot.draw()


Projections().mainloop()
