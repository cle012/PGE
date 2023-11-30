import numpy as np
import noise
import pygame

class TerrainGenerator:
    def __init__(self):
        self.colors = {
            "water":(0,0,255),
            "sand":(255,255,102),
            "grass":(34,139,34),
            "rock":(139,137,137),
        }

    def generate_terrain(self, width, height, scale, octaves, persistence, lacurity, seed):
        terrain = np.zeros((width,height), dtype=float)

        for x in range(width):
            for y in range(height):
                nx = x / width-0.5
                ny = y / height-0.5
                value = noise.snoise2(
                    scale * nx,
                    scale * ny,
                    octaves = octaves,
                    persistence = persistence,
                    lacunarity = lacunarity,
                    base = seed
                )
                terrain[x][y] = value
        return terrain

    def render_terrain(self, screen, terrain):
        for x in range(len(terrain)):
            for y in range(len(terrain[0])):
                color = self.get_terrain_color(terrain[x][y])
                pygame.draw.rect(screen, color, (x,y,1,1))

    def terrain_color(self, value):
        if -1 <= -0.2:
            return self.colors["water"]
        elif -0.2 <= value < 0:
            return self.colors["sand"]
        elif 0 <= value < 0.3:
            return self.colors["rock"]
