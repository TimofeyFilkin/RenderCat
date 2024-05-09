import sys
import moderngl as mgl
import pygame as pg
import win32api
import win32con
import win32gui
from RenderCat.camera import Camera
from RenderCat.light import Light
from RenderCat.mesh import Mesh
from RenderCat.scene import Scene
from RenderCat.scene_renderer import SceneRenderer


class Engine:
    def __init__(self, win_size=None):
        pg.init()
        if win_size != None:
            self.WIN_SIZE = win_size
        else:
            self.WIN_SIZE = pg.display.get_desktop_sizes()[0]
        self.window = pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF | pg.NOFRAME)
        pg.event.set_grab(False)
        pg.mouse.set_visible(False)
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        self.light = Light(position=(15, 15, -3))
        self.camera = Camera(self, position=(0, 5, 15))
        self.mesh = Mesh(self)
        self.scene = Scene(self)
        self.scene_renderer = SceneRenderer(self)
        self.overlay = pg.Surface(self.WIN_SIZE)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_F11:
                pg.display.toggle_fullscreen()

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        dx, dy = pg.mouse.get_rel()
        pg.mouse.set_pos((self.WIN_SIZE[0] / 2, self.WIN_SIZE[1] / 2))
        self.camera.rotate(dx, dy)
        self.camera.move()
        self.scene_renderer.render()
        self.window.blit(self.overlay, (0, 0))
        pg.draw.circle(self.overlay, (255, 255, 255), (self.WIN_SIZE[0]//2, self.WIN_SIZE[1]//2), 50)
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.tick()
            self.render()
            self.delta_time = self.clock.tick(60)

    def tick(self):
        ...


print("RenderCat v.1")
