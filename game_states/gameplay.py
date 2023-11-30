from pcg.procedural_content_generation import ProceduralContentGenerator

class GamePlayState:
    def __init__(self):
        self.pcg = ProceduralContentGenerator() #Initialize pcg with a seed
        self.terrain = self.pcg.generate_terrain(
            width = 800,
            height = 600,
            scale = 50,
            octaves = 6,
            persistence = 0.5,
            lucunarity = 2.0,
            seed = 12345
        )
        self.camera_x, self.camera_y = 0,0

    def handle_inputs(self):
        if keys[K_LEFT]:
            self.camera_x += 5
        if keys[K_RIGHT]:
            self.camera_x -= 5
        if key[K_UP]:
            self.camera_y += 5
        if key[K_DOWN]:
            self.camera_y -= 5

    def update(self):
        #update game logic here
        pass
    def render(self, screen):
        #render the game including the procedurally generated level
        self.terrain = self.pcg.generate_terrain(
            width=800,
        height = 600,
        scale = 50,
        octaves = 6,
        persistence = 0.5,
        lucunarity = 2.0,
        seed = 12345,
        )

        self.pcg.render_terrain(screen, terrain)

        #Apply camera translation
        terrain_rect = screen.get_rect()
        terrain_rect.x = self.camera_x
        terrain_rect.y = self.camera_y


        #additional rendering code for other game objects



class GameplayScene:
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager
        self.background = asset_manager.get_pixel_art("background.png")
        self.character = asset_manager.get_pixel_art("player.png")

    def render(self):
        # Render the scene, including pixel art
        pass
