import glm

FOV = 50
ZNEAR = 0.1
ZFAR = 200
SPEED = 0.2
sensivity = 0.2


class Camera:
    def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0):
        self.app = app
        self.ASPECT = 1600 / 900
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        self.m_view = self.get_view_matrix()
        self.m_proj = self.get_matrix()

    def rotate(self, x, y):
        rel_x, rel_y = x, y
        self.yaw += rel_x * sensivity
        self.pitch -= rel_y * sensivity
        self.pitch = max(-89, min(89, self.pitch))
        self.update_vectors()
        self.m_view = self.get_view_matrix()

    def update_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)
        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def process(self):
        pass

    def move(self, input_buffer: dict):
        if input_buffer["w"]:
            self.position += self.forward * SPEED
        if input_buffer["s"]:
            self.position -= self.forward * SPEED
        if input_buffer["a"]:
            self.position -= self.right * SPEED
        if input_buffer["d"]:
            self.position += self.right * SPEED
        if input_buffer["q"]:
            self.position += self.up * SPEED
        if input_buffer["e"]:
            self.position -= self.up * SPEED
        if input_buffer["up"]:
            self.rotate(0, -1)
        if input_buffer["down"]:
            self.rotate(0, 1)
        if input_buffer["left"]:
            self.rotate(-1, 0)
        if input_buffer["right"]:
            self.rotate(1, 0)
        self.m_view = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_matrix(self):
        return glm.perspective(glm.radians(FOV), self.ASPECT, ZNEAR, ZFAR)
