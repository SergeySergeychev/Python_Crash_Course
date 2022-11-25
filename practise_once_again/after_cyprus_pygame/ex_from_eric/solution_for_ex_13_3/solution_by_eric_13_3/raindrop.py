import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop"""

    def __init__(self, rd_game):
        """Initialize the raindrop and set it starting position"""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/erics_raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position.
        self.y = float(self.rect.y)
    def check_disappeared(self):
        """Check if drop has disappeared off bottom of screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False
    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y