# noinspection PyUnresolvedReferences
import glm
# noinspection PyUnresolvedReferences
import math
import RenderCat


class Engine(RenderCat.Engine):
    def __init__(self):
        super().__init__((1920, 1080))


if __name__ == '__main__':
    app = Engine()
    app.run()
