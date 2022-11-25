import sys

import pygame

from settings import Settings

from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

from pygame.sprite import Group

def run_game():
    # Initialize pygame, screen object, settings.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    # Make a Play button.
    play_button = Button(ai_settings, screen, "Play")
    # Create an instance to store game statistic and create scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                aliens, bullets)
        if stats.game_active:
            # Update the ship's position.
            ship.update()
            # Update position of bullets and get rid of old bullets.
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                 aliens,  bullets)
            # Update position of each alien.
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
        # Redraw the screen during each pass through the loop.
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                bullets, play_button)

run_game()
