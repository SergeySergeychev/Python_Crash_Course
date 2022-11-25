import sys
import pygame
import game_functions as gf

from settings import Settings
from rectangle import Rectangle
from game_stats import GameStats
from button import Button
from ship import Ship
from pygame.sprite import Group

def run_game():
    # Initialize pygame, screen, object , settings.]
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("TryToHit")
    # Make a play button.
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Let's GO")
    # Make a ship, a group of bullets and group of rectangles.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    rectangles = Group()
    # Add rectangle to the group.
    gf.create_rectangle(ai_settings, screen, rectangles)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        bullets, rectangles)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, ship, bullets,
                                 rectangles)
            gf.update_rectangle(ai_settings, rectangles)
            print(bullets)
        gf.update_screen(ai_settings, stats, screen, bullets,  rectangles ,
                        ship, play_button)
run_game()
