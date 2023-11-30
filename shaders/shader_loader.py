import pygame
from OpenGL.GL import *
import os

def load_shader(shader_filename, shader_type):
    """"Load and compile a shader from a file"""
    shader_id = glCreateShader(shader_type)
    with open(shader_filename, "r") as shader_file:
        shader_source = shader_file.read()
    glShaderSource(shader_id, shader_source)
    glCompileShader(shader_id)

    #check for shader compilation errors (and error handling here)
    if glGetShaderiv(shader_id, GL_COMPILE_STATUS) != GL_TRUE:
        print(f'Shader compilation errors in {shader_filename}:')
        print(glGetShaderInfoLog(shader_id))
        return None

    return shader_id

def create_shader_program(vertex_shader, fragment_shader):
    """Create a shader program from vertex and fragment shaders"""
    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader, fragment_shader)
    glLinkProgram(shader_program)

    #check for program linking errors (and error handling here )
    if glGetProgramiv(shader_program, GL_LINK_STATUS) != GL_TRUE:
        print("shader program linking error:" )
        print(glGetProgramInfoLog(shader_program))
        return None
    return shader_program
