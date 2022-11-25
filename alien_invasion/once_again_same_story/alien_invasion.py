import sys

import pygame

from ship import Ship

from alien import Alien

from settings import Settings

import game_functions as gf

from pygame.sprite import Group

def run_game():
    """Initialize pygame, settings, and screen object."""
    pygame.init()
    # Creat an instance from class Settings.
    ai_settings = Settings()
    # This function will create a display surface with settings
    # (size=(1200, 80)...)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # If the display has a window title, this funciton will change the
    # name of the window.
    pygame.display.set_caption("Alien Invasion")
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Start the main loop for the game.
    while True:
        # Check for players inpu.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Update the position of the ship.
        ship.update()
        # Update bullet position.
        # Get rid of bullets that have disappeared.
        gf.update_bullets(bullets)
        # Redraw the screen during each pass throught the loop.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
