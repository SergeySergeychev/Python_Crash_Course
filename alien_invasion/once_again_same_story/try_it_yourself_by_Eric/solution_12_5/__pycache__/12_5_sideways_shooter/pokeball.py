# Creating the pokeball class.
# Import pygame before class.
# From pygame.sprite module import class Sprite.
# Create class Pokeball.It should inherit Sprite class.
# Write docstring """A class to manage pokeballs fired from the pokemaster."""
# Make a constructor with parameters as ss_settings, screen, pokeball_master
# Write inheritance sentence. super().__init__()
# Create attribute of screen parameter.
"""Create a pokeball and set it under the pokemaster layer."""
# Load a pokeball picture.
# Create a rect of the pokeball picture.
# Set rect of pokeball picture to the middle of pokeball_master rect.
# Store the pokeball position as a decimal value.
# Add an atribute speed_factor from settings class.

# Write a method update. Method will take the self parameter only.
# Write a function, to move pokeball to the right of the screen.
# Update the pokeballs rect position , which stored in decimals.
# Write a method blitme for pokeball.
# Draw poekbal at it's current location.

import pygame

from pygame.sprite import Sprite

class Pokeball(Sprite):
    """A class to manage pokeballs fired from the pokemaster."""

    def __init__(self, ss_settings, screen, pokeball_master):
        super().__init__()

        self.screen = screen
        # Create a pokeball and set it under the pokemaster layer."
        # load pokeball picture.C:\Users\sserg\1PythonPractice\alien_invasion\once_again_same_story\try_it_yourself_by_Eric\solution_12_5\__pycache__\12_5_sideways_shooter\image\pokemon.bmp
        self.image = pygame.image.load(r'C:\Users\sserg\1PythonPractice\alien_invasion\once_again_same_story\try_it_yourself_by_Eric\solution_12_5\__pycache__\12_5_sideways_shooter\image\pokeball.bmp')
        # Make rect of the pokeball's image.
        self.rect = self.image.get_rect()
        # Set pokeball position in the middle, right edge of the pokeball_master.
        self.rect.centery = pokeball_master.rect.centery
        self.rect.right = pokeball_master.rect.right

        # Store the pokeball's position as s decimal value
        self.x = float(self.rect.x)

        # Set pokeballs speed.
        self.speed_factor = ss_settings.pokeball_speed_factor

    def update(self):
        """Throw the pokeball to the right side of the screen."""
        self.x +=self.speed_factor
        # Update the pokeballs rect position.
        self.rect.x = self.x

    def blitme(self):
        """Draw an image of the pokeball."""
        self.screen.blit(self.image, self.rect)
