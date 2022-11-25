import pygame

class Ship():
    """A class to represent a ship."""

    def __init__(self, ai_settings, screen):
        """Initialize a ship and set its starting position."""
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the ship and get its rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the left center side of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the ship center.
        self.center = float(self.rect.centery)

        # Set movement flags.
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update ship's position based on the movement flags."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update ship center rect position.
        self.rect.centery = self.center

    def center_ship(self):
        """Center the ship on the left side of the screen."""
        self.center = self.screen_rect.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
