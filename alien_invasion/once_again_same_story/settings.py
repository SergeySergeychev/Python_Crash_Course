import pygame

class Settings():
    """A class to store all setting s for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings.
        self.screen_width = 848
        self.screen_height = 600
        self.bg_color =(255, 255, 255)
        self.ship_speed_factor = 1.5
        #Bullet Settings
        self.bullet_speed_fact = 2
        self.bullet_widht = 5
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 5
