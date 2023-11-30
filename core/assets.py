import uuid  # For generating unique IDs

class Asset:
    def __init__(self, asset_type, x, y):
        self.asset_type = asset_type
        self.x = x
        self.y = y
        self.unique_id = str(uuid.uuid4())  # Generate a unique ID for each asset
        self.character = self.generate_character()

    def generate_character(self):
        # Logic to generate a character or personality for the asset
        # This could be random or based on the asset's type or location
        # For example, you can assign different characters like "friendly," "mysterious," etc.

# Asset generation logic
def generate_assets(num_assets):
    assets = []
    for _ in range(num_assets):
        asset_type = random.choice(["tree", "rock", "chest"])
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        asset = Asset(asset_type, x, y)
        assets.append(asset)
    return assets

# Inside your game loop
assets = generate_assets(NUM_ASSETS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Handle interactions with assets
            for asset in assets:
                if is_point_within_asset(event.pos, asset):
                    narrative_event = f"You encountered a {asset.asset_type} with ID {asset.unique_id} and character: {asset.character}"
                    display_narrative(narrative_event)
