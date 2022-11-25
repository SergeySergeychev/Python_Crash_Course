
import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """Class to present a player."""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set it starting position."""
        super(Player, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the player image and set its rect.
        self.image = pygame.image.load('images/player_super_sonic.bmp')
        self.rect =self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start player position at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for a player's rect.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Update player position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ball_falling_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ball_falling_speed

        # Update rect object from self center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)

    def take_center(self):
        """Player take center position."""
        self.center = self.screen_rect.centerx
