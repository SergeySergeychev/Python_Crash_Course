
# Import Group from pygame.sprite
# Make a Group to store pokeballs in it.
# In while loop to check_events add three parameters ss_settings,
# screen, pokeballs Group.
# To while loop add update function with Group argument
# To update_screen add group parameter.

# Get rid of pokeballs that have disappeared.
#
import sys

import pygame

from settings import Settings

import game_functions as gf

from pokeball_master import Pokeball_master

from pygame.sprite import Group

def run_game():
    """Initialize pygame,settings, and screen object."""
    pygame.init()
    # Make a group to store pokeballs in it.
    pokeballs = Group()
    ss_settings = Settings()
    screen = pygame.display.set_mode(
        (ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("GO-GO Pokemon Master!!!")
    # Make an image object.
    pokeball_master = Pokeball_master(ss_settings, screen)
    # Start main loop for the game.
    while True:

        #Watch for keyboard and mouse events.
        gf.check_events(ss_settings, screen, pokeball_master, pokeballs)
        pokeball_master.update()
        #  Update position of pokeballs and get rid of old pokeballs.
        gf.update_pokeballs(pokeball_master, pokeballs)
        gf.update_screen(ss_settings, screen, pokeball_master, pokeballs)

run_game()
