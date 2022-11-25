import pygame

class Rocket:
    """A class to manage rocket."""


    def __init__(self, r_game):
        """Initialize the rocket and set its starting position."""
        self.screen = r_game.screen
        self.screen_rect = r_game.screen.get_rect()
        self.settings = r_game.settings


        # Load the rocket image and get its rect.

        self.image = pygame.image.load(r'C:\Users\sserg\1PythonPractice\alien_invasion\once_again_same_story\try_it_yourself_by_Eric\solution_12_4\images\cohete_off.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the rocket's horizontal
        # and vertical positions.

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags.

        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def update(self):
        """Update the rocket's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update rect object from position attributes.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
