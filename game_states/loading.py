import pygame
from core import engine


class LoadingState(engine.GameState):
    def __init__(self):
        super(LoadingState, self).__init__()

        #initialize loading screen assetsand logic here
        self.loading_progress = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.quit()
            #loading screen may not require event handling

    def update(self):
        #Simulate loading process here (e.g., loading assets)
        self.loading_progress += 1

        if self.loading_progress >= 100:
            #Transition to another state( e.g., gameplay) once loading is complete
            self.engine.set_state(GamePlayState()) #replace with your desired state

    def render(self):
        #Render the loading screen, indicating loading progress
        loading_font = pygame.font.Font(None,36)
        loading_text = loading_font.render(f'LOading... {self.loading_progress}%', True,(255,255,255))
        self.engine.screen.blit(loading_text,(200,200)) #Example display loading progress
