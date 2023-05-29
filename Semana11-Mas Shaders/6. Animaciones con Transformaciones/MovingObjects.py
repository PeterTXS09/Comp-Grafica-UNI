from glApp.PyOGApp import *
from glApp.Utils import *
from glApp.Square import *
from glApp.Triangle import *
from glApp.Axes import *
from glApp.Cube import *
from glApp.LoadMesh import *
from glApp.MovingCube import *


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


class MovingObjects(PyOGApp):

    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.axes = None
        self.moving_cube = None


    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.axes = Axes(self.program_id, pygame.Vector3(0, 0, 0))
        self.moving_cube = MovingCube(self.program_id, location = pygame.Vector3(2, 1, 2),
                                      move_rotation=Rotation(1, pygame.Vector3(0, 1, 0)))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        self.axes.draw()
        self.moving_cube.draw()



MovingObjects().mainloop()
