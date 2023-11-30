# ui/code_editor_gui.py

import pygame
from pygame_textinput import TextInputManager
class CodeEditorGUI:
    def __init__(self, screen, code_text):
        self.screen = screen
        self.text_input = TextInput(initial_string=code_text)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Process the entered code, e.g., compile and execute
                    entered_code = self.text_input.get_text()
                    print("Entered code:", entered_code)
                else:
                    self.text_input.update(event)

    def render(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        # Render the code editor
        self.text_input.draw(self.screen)

        # Update the display
        pygame.display.flip()
