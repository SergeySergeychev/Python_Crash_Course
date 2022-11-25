import sys
import pygame
import game_functions as gf

from settings import Settings
from raindrop import Raindrop
from pygame.sprite import Group

def run_game():
    # Initialize pygame, screen object, settings.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raindrop FaLL")
    # Make a group of raindrops.
    raindrops = Group()
    # Create_rain.
    gf.create_rain(ai_settings, screen, raindrops)

    # Start the main loop fro the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        # Update raindrop position
        gf.update_raindrop(ai_settings, screen, raindrops)
        # Redraw the screen during each pass through the loop.
        # make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, raindrops)
        print(raindrops)
run_game()
