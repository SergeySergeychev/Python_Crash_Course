# Find bitmap image of a game character.
# Make a class that draws the character at the center of the screen.
# Match background color of the image to the back ground color of the screen.

import pygame

# ceate class ClassName(object):
class CenterCharacter():
    """
    Drawing character in the center of screen.
    Make background color of the screen same as background color of image.
    """
    def __init__(self, screen):
        """Iniitalize attributes of class CharacterCenter"""
        self.screen = screen

        # Load image and get its rect.
        # Create attribute for image and load image from images dir..
        self.image = pygame.image.load('images/pocemon.bmp')

        # Create attribute for rectangular image and make image as rect.
        self.rect = self.image.get_rect()

        # Create attribute for rectangular screen and make surface as rect.
        self.screen_rect = screen.get_rect()

        # Position of image center on surface is the same position as screen
        # center.
        self.rect.center = self.screen_rect.center


        # Copy the image to the screen.
    def blitme(self):
        """Draw image at its current location on the screen."""
        self.screen.blit(self.image, self.rect)
