# Make group of Stars.
# Create stars visible on the black sky.
# Refactor functionality in while loop.


import sys

import pygame

from settings import Settings

from star import Star

from pygame.sprite import Group

import game_functions as gf

def run_game():
    """Initialize game and create a screen object visible."""
    pygame.init()
    s_settings = Settings()
    stars = Group()
    screen = pygame.display.set_mode(
                    (s_settings.screen_width, s_settings.screen_height))
    pygame.display.set_caption('Super Star')
    # Make a Star
    star = Star(screen)
    gf.create_stars(s_settings, screen, stars)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        gf.update_screen(s_settings, screen, stars)
run_game()
