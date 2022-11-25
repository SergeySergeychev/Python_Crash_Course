import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """A class to present a single ball."""

    def __init__(self, ai_settings, screen):
        """"Initialize the ball and set it starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ball image and set its rect attribute
        self.image = pygame.image.load(r'C:\Users\sserg\after_cyprus_pygame\images\fire_ball.bmp')
        self.rect = self.image.get_rect()

        # Start each new ball at the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the ball exact position
        self.y = float(self.rect.y)

    def blitme(self):
        # Draw the ball at its current location.
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the ball steady down of the screen."""
        self.y += self.ai_settings.ball_falling_speed
        self.rect.y = self.y
