from glApp.PyOGApp import *

class Refactor_Test(PyOGApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)

    def initialise(self):
        background_color = (0, 0, 0, 1)
        drawing_color = (1, 1, 1, 1)

        glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
        glColor(drawing_color)

        # projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, (self.screen_width / self.screen_height), 0.1, 1000.0)

    def camera_init(self):
        # modelview
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0, 0, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)
        self.camera.update(self.screen_width, self.screen_height)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_world_axes()

Refactor_Test().mainloop()