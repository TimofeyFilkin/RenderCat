class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        # noinspection PyDictCreation
        self.shaders = {}
        self.shaders['default'] = self.get_prtogram('default')
        self.shaders['skybox'] = self.get_prtogram('skybox')
        self.shaders['advanced_skybox'] = self.get_prtogram('advanced_skybox')
        self.shaders['shadow_map'] = self.get_prtogram('shadow_map')


    def get_prtogram(self, shader_name):
        with open(f'Shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        
        with open(f'Shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        [program.release() for program in self.shaders.values()]
