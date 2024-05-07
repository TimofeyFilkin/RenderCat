from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    # noinspection PyDictCreation
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}
        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.shaders['default'],
            vbo=self.vbo.vbos['cube'])
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.shaders['shadow_map'],
            vbo=self.vbo.vbos['cube'])
        self.vaos['cat'] = self.get_vao(
            program=self.program.shaders['default'],
            vbo=self.vbo.vbos['cat'])
        self.vaos['cactus'] = self.get_vao(
            program=self.program.shaders['default'],
            vbo=self.vbo.vbos['cactus'])
        self.vaos['shadow_cat'] = self.get_vao(
            program=self.program.shaders['shadow_map'],
            vbo=self.vbo.vbos['cat'])
        self.vaos['shadow_cactus'] = self.get_vao(
            program=self.program.shaders['shadow_map'],
            vbo=self.vbo.vbos['cactus'])
        self.vaos['skybox'] = self.get_vao(
            program=self.program.shaders['skybox'],
            vbo=self.vbo.vbos['skybox'])
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.shaders['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
