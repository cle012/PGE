import pygame
from core import engine

#remember to insert the engine.GameState in the Victory State class below
#class VictoryStates(engine.GameStates):
class VictoryStates():
    def __init__(self):
        super(VictoryStates, self).__init__()

        #initialize the victory screen assets and logic here

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.quit()

            #handle mouse clicks or other events specific to the victory screen

    def update(self):
        #update victory screen logic Here
        pass

    def render(self):
        #render the victory screen here
        pass