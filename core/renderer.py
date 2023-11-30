from OpenGl.GL import *
from shaders.shader_loader import load_shader,create_shader_program

class Renderer:
    def __init__(self, width, height):
        #Initialize Pygameand OPenGL here

        #load shaders
        self.vertex_shader = load_shader("assets/shaders/vertex_shader.glsl", GL_VERTEX_SHADER)
        self.fragment_shader = load_shader("assets/shaders/fragmentshader.glsl", GL_FRAGMEN_SHADER)

        #create shader program
        self.shader_program = create_shader_program(self.vertex_shader, self.fragment_shader)

        #Initiate other rendering-related settings


    def render(self, game_objects):
        glUseProgram(self.shader_program)

        #set shader uniforms and attributes here

        for game_objects in game_objects:
            #Bind object-specific data to shader uniform/attributes
            pass
            #render object using shaders
        glUseProgram(0)#Disable the shader program when done rendering
