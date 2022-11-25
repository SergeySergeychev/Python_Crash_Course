# Create main function luch_rocket
# With this list of functions and variables inside of it:
# 1. Initialize game and create a screen object.
# 2. Write Main loop for the game.
# 3. Make the most recently drawn screen visible.

import sys

from rocket import Rocket

import pygame

from rocket_settings import Settings

import rl_functions as rl_f

def run_game():
    # Initialize game anc create a screen object.
    pygame.init()

    rl_settings = Settings()

    screen = pygame.display.set_mode(
    (rl_settings.screen_width, rl_settings.screen_height))

    pygame.display.set_caption("Rocket Luncher")
    rocket = Rocket(rl_settings, screen)
    # Start the main loop.
    while True:

        # Watch for keyboard and mouse events.
        rl_f.check_events(rocket)
        # Update the rocket's position.
        rocket.update()
        # Make the most recently drawn screen visible.
        # Redraw the screen during each pass trough the loop.
        rl_f.update_screen(rl_settings, screen, rocket)
run_game()
