import moderngl_window as mglw
import moderngl as mgl
from scene_renderer import SceneRenderer
from mesh import Mesh
from model import *
from camera import Camera
from light import Light
from scene import Scene


class RenderCat(mglw.WindowConfig):
    window_size = 1600, 900
    resource_dir = "Shaders"
    title = "RenderCat Engine"
    cursor = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cam_pos = glm.vec3(0, 15, -5)
        self.test_shader = self.load_program(vertex_shader="default.vert", fragment_shader="default.frag")
        self.red = self.load_program(vertex_shader="default.vert", fragment_shader="RedF.glsl")
        self.light = Light()
        self.camera = Camera(self, position=self.cam_pos)
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        self.time = 0
        self.input_buffer = {"w": False, "a": False, "s": False, "d": False, "q": False, "e": False, "up": False,
                             "down": False, "left": False, "right": False}
        self.mesh = Mesh(self)
        self.scene = Scene(self)
        self.scene_renderer = SceneRenderer
        self.resizable = False
        self.wnd.fullscreen = True
        self.wnd.mouse_exclusivity = True

    def render(self, time: float, frame_time: float):
        self.wnd.fullscreen = False
        self.wnd.mouse_exclusivity = True
        self.camera.process()
        self.camera.move(self.input_buffer)
        self.scene.render()
        self.time += 1

    def mouse_position_event(self, x: int, y: int, dx: int, dy: int):
        self.camera.rotate(dx, dy)

    def key_event(self, key: any, action: any, modifiers):
        if action == self.wnd.keys.ACTION_PRESS:
            match key:
                case (self.wnd.keys.W):
                    self.input_buffer['w'] = True
                case (self.wnd.keys.A):
                    self.input_buffer['a'] = True
                case (self.wnd.keys.S):
                    self.input_buffer['s'] = True
                case (self.wnd.keys.D):
                    self.input_buffer['d'] = True
                case (self.wnd.keys.Q):
                    self.input_buffer['q'] = True
                case (self.wnd.keys.E):
                    self.input_buffer['e'] = True
                case (self.wnd.keys.UP):
                    self.input_buffer['up'] = True
                case (self.wnd.keys.DOWN):
                    self.input_buffer['down'] = True
                case (self.wnd.keys.RIGHT):
                    self.input_buffer['right'] = True
                case (self.wnd.keys.LEFT):
                    self.input_buffer['left'] = True
        else:
            match key:
                case (self.wnd.keys.W):
                    self.input_buffer['w'] = False
                case (self.wnd.keys.A):
                    self.input_buffer['a'] = False
                case (self.wnd.keys.S):
                    self.input_buffer['s'] = False
                case (self.wnd.keys.D):
                    self.input_buffer['d'] = False
                case (self.wnd.keys.Q):
                    self.input_buffer['q'] = False
                case (self.wnd.keys.E):
                    self.input_buffer['e'] = False
                case (self.wnd.keys.UP):
                    self.input_buffer['up'] = False
                case (self.wnd.keys.DOWN):
                    self.input_buffer['down'] = False
                case (self.wnd.keys.RIGHT):
                    self.input_buffer['right'] = False
                case (self.wnd.keys.LEFT):
                    self.input_buffer['left'] = False


# noinspection PyTypeChecker
mglw.run_window_config(RenderCat)
