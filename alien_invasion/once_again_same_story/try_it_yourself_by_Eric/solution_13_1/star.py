# import pygame
# Make a class Star
# Initialize class attributes.
# Load image.
# Make rect from image.
# Make rect from screen.
# First start position will be in left upper-corner of the screen.
# Write method to draw the stars image.

# import addition tool as pygame.sprit.
# Class Start need to inerit class Sprite.


import pygame

from pygame.sprite import Sprite

class Star(Sprite):
    """Class reprsents single star."""
    def __init__(self, screen):
        super().__init__()
        """Initialize star and contains first star position."""
        self.screen = screen
        # Load image from folder images.
        self.image = pygame.image.load(r'C:\Users\sserg\1PythonPractice\alien_invasion\once_again_same_story\images\star.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set start position of the first star rect.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
