# procedural_generation/pixel_art_gui.py

import pygame
# procedural_generation/pixel_art_gui.py

import pygame
import pygame_gui

class PixelArtGUI:
    def __init__(self, screen, pixel_art_generator):
        self.screen = screen
        self.pixel_art_generator = pixel_art_generator
        self.ui_manager = pygame_gui.UIManager((screen.get_width(), screen.get_height()))
        self.initialize_gui_elements()

    def initialize_gui_elements(self):
        # Create color palette picker
        color_palette_picker = pygame_gui.elements.UIDropDownMenu(
            ["Palette 1", "Palette 2", "Custom Palette"],  # Palette options
            "Choose Palette",  # Initial text
            pygame.Rect((10, 10), (200, 30)),  # Position and size
            self.ui_manager
        )

        # Create pixel size slider
        pixel_size_slider = pygame_gui.elements.UIHorizontalSlider(
            pygame.Rect((10, 50), (200, 30)),  # Position and size
            1, 10,  # Minimum and maximum values
            self.ui_manager
        )

        # Create resolution input field
        resolution_input = pygame_gui.elements.UITextEntryLine(
            pygame.Rect((10, 90), (200, 30)),  # Position and size
            self.ui_manager
        )

        # Create a Generate button
        generate_button = pygame_gui.elements.UIButton(
            pygame.Rect((10, 130), (200, 30)),  # Position and size
            "Generate Pixel Art",  # Button label
            self.ui_manager
        )

        # Define event handlers for the GUI elements
        color_palette_picker.subscribe(self.on_palette_selected)
        pixel_size_slider.subscribe(self.on_pixel_size_changed)
        resolution_input.subscribe(self.on_resolution_updated)
        generate_button.subscribe(self.on_generate_button_click)

    def on_palette_selected(self):
        # Handle color palette selection
        selected_palette = color_palette_picker.get_single_selection()
        if selected_palette == "Custom Palette":
            # Allow users to customize the palette
            # You may open another GUI window for this.
            pass
        else:
            # Use a predefined palette

    def on_pixel_size_changed(self):
        # Handle pixel size adjustment
        selected_size = pixel_size_slider.get_current_value()

    def on_resolution_updated(self):
        # Handle resolution input
        resolution = resolution_input.get_text()

    def on_generate_button_click(self):
        # Trigger pixel art generation
        # Use the selected options to generate pixel art
