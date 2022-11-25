import pygame
from pygame.sprite import Sprite

class Rectangle(Sprite):
    """A class to represent rectangle."""

    def __init__(self, ai_settings, screen):
        """Create a rectangle object.
        Place it at the right side of the screen center.
        """
        super(Rectangle, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings

        # Create a rectangle rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.rectangle_width,
            ai_settings.rectnagle_height)

        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        # Store rectangle's position as a decimal value.
        self.y = float(self.rect.y)

        # Store rectangle's color, speed factor, direction
        self.color = self.ai_settings.rectnagle_color
    def update(self):
        """Move rectangle up and down on a screen."""
        # Update position of the rectangle.
        self.y += (self.ai_settings.rectangle_speed_factor *
                    self.ai_settings.rectangle_direction)
        self.rect.y = self.y

    def check_edges(self):
        """Return True if rectangle is at edge of a screen."""
        screen_rect  = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def draw_rectangle(self):
        """Draw the rectangle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_rectangle(self):
        """Center the rectangle on the left side of the screen."""
        self.y = self.screen_rect.centery
