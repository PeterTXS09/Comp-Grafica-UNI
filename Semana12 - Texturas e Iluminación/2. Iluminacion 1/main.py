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
in vec3 vertex_normal;
uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;
out vec3 color;
out vec3 normal;
out vec3 fragpos;
out vec3 light_pos;
void main()
{
    light_pos = vec3(inverse(model_mat) * 
                    vec4(view_mat[3][0], view_mat[3][1], view_mat[3][2],1));
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position,1);
    normal = vertex_normal;
    fragpos = vec3(model_mat * vec4(position,1));
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core
in vec3 color;
in vec3 normal;
in vec3 fragpos;
in vec3 light_pos;
out vec4 frag_color;
void main()
{
    vec3 light_color = vec3(1, 0, 0);
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - fragpos);
    float diff = max(dot(norm, light_dir), 0);
    vec3 diffuse = diff * light_color;
    frag_color = vec4(color * diffuse, 1);
}
'''


class ShaderObjects(PyOGApp):

    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.axes = None
        self.moving_cube = None
        self.teapot1 = None
        self.teapot2 = None


    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        #self.axes = Axes(self.program_id, pygame.Vector3(0, 0, 0))
        #self.moving_cube = Cube(self.program_id, location=pygame.Vector3(2, 1, 2),
         #                       move_rotation=Rotation(1, pygame.Vector3(0, 1, 0)))
        #self.teapot1 = LoadMesh("models/teapot.obj", self.program_id,
         #                       move_translate=pygame.Vector3(0.1, 0, 0),
          #                      move_rotation=Rotation(2, pygame.Vector3(1, 1, 0)))
        self.teapot2 = LoadMesh("models/teapot.obj", self.program_id,
                                location=pygame.Vector3(0, 0, 0),
                                scale=pygame.Vector3(0.5, 0.5, 0.5),
                                move_rotation=Rotation(1, pygame.Vector3(0, 1, 0)))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        #self.axes.draw()
        #self.moving_cube.draw()
        #self.teapot1.draw()
        self.teapot2.draw()



ShaderObjects().mainloop()
