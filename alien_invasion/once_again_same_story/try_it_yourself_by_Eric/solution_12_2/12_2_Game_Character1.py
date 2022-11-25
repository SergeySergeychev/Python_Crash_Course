import sys

import pygame

from centercharacter import CenterCharacter

from settings import Settings

import game_functions as gf

def run_game():
    """Initialize pygame, settings, and screen object."""
    pygame.init()

    # Creat variable from class Settings
    ai_settings = Settings()

    # This function will create a display Surface
    # set_mode(size=(1200, 80)...)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    # If the display has a window title, this funciton will change the
    # name of the window.
    pygame.display.set_caption("GO POCEMON")

    # Make a ship.
    image = CenterCharacter(screen)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events()

        # Redraw the screen during each pass throught the loop.
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, image)

run_game()
