# Write class raindrop.
    # First of all use instruments  as pygame and Sprite.
    # Raindrop class inherits from Sprite class.
    # Class Raindrop presents a single raindrop.
    # Initialize the raindrop and set it starting position.
        # Load raindrops image and set its rectangle attribute.
        # Start each new raindrop near the top left of the screen.
        # Store raindrops exact position.
    # Write function blitme.
        # Draw the raindrop at its current location

import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to present a single raindrop"""

    def __init__(self, ai_settings, screen):
        """Initialize the raindrop and set it starting position"""
        super(Raindrop, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load raindrop image and set its rectangle attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store raindrop exact position
        self.x = float(self.rect.x)
        self.moving_down = True
    def blitme(self):
        """Draw raindrop at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Make raindrop fall."""
        self.y += (self.ai_settings.raindrop_speed_factor)
        self.rect.y = self.y

    def check_edges(self):
        """Return True if raindrops row is at the bottom."""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom :
            return True
