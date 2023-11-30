import pygame
from core import engine

class CutsceneState(engine.GameState):
    def __init__(self):
        super(CutsceneState, self).__init__()


        #initialize cutscene assets and logic here
        self.cutscene_duration = 5000
        self.start_time = pygame.time.get_ticks()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.quit()
            #ALlow skipping or interacting with the cutscene as needed

    def update(self):
        #Update cutscene logic here e.g. animations and events

        #check if the cutscene duration has passed
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.cutscene_duration:
            #Transition to another state after the cutscene
            self.engine.set_state(GamePlayState()) #replace with your desired state

    def render(self):
        #render the cutscene here
        #display dialogue, animations, and event relevant to the story
        pass