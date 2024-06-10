# noinspection PyUnresolvedReferences
import glm
# noinspection PyUnresolvedReferences
import math
import RenderCat
import pygame as pg
import sys

pg.font.init()
my_font = pg.font.SysFont('Arial', 50)

class Engine(RenderCat.Engine):
    def __init__(self):
        res = (1920, 1080)
        shadow_res = res
        fullbright = False
        for i in range(len(sys.argv)):
            if sys.argv[i] == "-resolution":
                res = (int(sys.argv[i+1]), int(sys.argv[i+2]))
            if sys.argv[i] == "-shadow_resolution":
                shadow_res = (int(sys.argv[i+1]), int(sys.argv[i+2]))
            if sys.argv[i] == "-fullbright":
                fullbright = True
                print("FULLBRIGHT ON")
        super().__init__(res, shadow_res, fullbright)

    def tick(self):
        pg.draw.circle(self.screen, (0, 0, 0), (self.WIN_SIZE[0] // 2, self.WIN_SIZE[1] // 2), 2)
        dx, dy = pg.mouse.get_rel()
        pg.mouse.set_pos((self.WIN_SIZE[0] / 2, self.WIN_SIZE[1] / 2))
        self.camera.rotate(dx, dy)
        self.camera.move()
        text_surface = my_font.render(str(int(self.clock.get_fps())), False, (0, 0, 0))
        self.screen.blit(text_surface, (0, 0))
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            exit()

if __name__ == '__main__':
    app = Engine()
    app.run()
