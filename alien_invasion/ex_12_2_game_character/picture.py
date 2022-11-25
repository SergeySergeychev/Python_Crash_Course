import pygame

class Picture():

    def __init__(self,screen):
        """Initialize the picture and set it in the center of screen"""
        self.screen = screen

        #Load the picture image and get its rect.
        self.image = pygame.image.load('ex_12_2_game_character/square.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Show picture at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery


    def blitme(self):
        """Draw the picture at its current location"""
        self.screen.blit(self.image, self.rect)
