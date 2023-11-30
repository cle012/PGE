# core/asset_manager.py

class PixelArtManager:
    def __init__(self):
        self.pixel_art_assets = {}

    def load_pixel_art(self, asset_name, path):
        # Load pixel art from file
        self.pixel_art_assets[asset_name] = pygame.image.load(path)

    def get_pixel_art(self, asset_name):
        return self.pixel_art_assets.get(asset_name)
