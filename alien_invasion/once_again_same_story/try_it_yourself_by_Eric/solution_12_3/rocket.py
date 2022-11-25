# Create attributes moving_up
# Create attribute moving_down
# Update rocket's position bas on the movement and don't allow to fly over
# the edge

import pygame

class Rocket():

    def __init__(self, rl_settings, screen):
        """Initialize the rocket and set its position."""
        self.screen = screen
        self.rl_settings = rl_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load(r'C:\Users\sserg\1PythonPractice\alien_invasion\once_again_same_story\try_it_yourself_by_Eric\solution_12_3\rocket_images\rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the center of the screen.
        self.rect.center = self.screen_rect.center
        # Store a decimal value for the ship's vertical and horizontal position.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's postion based on the movement flags."""
        # Update the rocket's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.rl_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.rl_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.rl_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.rl_settings.rocket_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y
    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
