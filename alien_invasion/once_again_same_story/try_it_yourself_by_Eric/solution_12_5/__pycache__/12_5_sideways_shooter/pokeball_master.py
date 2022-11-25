# Create class.
# Initialize pokeball_masters attributes.
# Download an image and create folder for it.
# load the pokeball_master image.
# Get pokeball_master rect.
# Get screen rect.
# Start each pokeball_master at the left center of the screen.
# Write method blitme.
# Draw pokeball_master at its current location.

# Create movement flag self.moving_down and put it on false.
# Write method update. Update pictures position based on the movement flag.
# Add update method to sideways_shooter while loop.

# Create movement flag self.moving_up and put it on false.
# Add to method update function moving_up

# Constructor have to store one more parameter ss_settings.
# Make ss_settings as atribute of pokeball_master class.
# Store a decimal value for the pokeball_master's center.
# In method update add functionality for movement. Update pokeball_masters center
# value , not the rect.
# Update rect object from self.y

# In update method limits pocemasters moving border.
# Image should not go out of screen's edges.


import pygame

class Pokeball_master():
    """Initialize a pokeball_master and its attributes."""
    def __init__(self, ss_settings, screen):
        self.screen = screen
        self.ss_settings = ss_settings
        # Load an image.
        self.image = pygame.image.load(r'C:\Users\sserg\1PythonPractice\alien_invasion\once_again_same_story\try_it_yourself_by_Eric\solution_12_5\__pycache__\12_5_sideways_shooter\image\pokemon.bmp')
        # Crate a pokeball_master rect.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Movement flag.
        self.moving_down = False
        self.moving_up = False
        # Store a decimal value for the pictures center.
        self.center_y = float(self.rect.centery)
        # Start each picture at the left center of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        # Draw pokeball_master at its current location.
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update pictures position if movement flag is True."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ss_settings.pokeball_master_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ss_settings.pokeball_master_speed_factor

        # Update rect object of the image.
        self.rect.centery = self.center_y
