import sys
import pygame

from pygame.sprite import Group

from player import Player
from ball import Ball
from settings import Settings
from game_stats import GameStats

import game_functions as gf

def run_game():
    # Initialize pygame, screen object, settings.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch The Fireball")
    # Make a player, a group of ball and players.
    player = Player(ai_settings, screen)
    ball = Ball(ai_settings, screen)
    balls = Group()
    players = Group()
    stats = GameStats(ai_settings)
    # Start the main loop for the game.

    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(player)

        if stats.game_active:
            # Update the player's position.
            player.update()
            # Update position of ball and get rid of old one.
            gf.update_ball(ai_settings,screen, player, players, balls, stats)

        # Update screen.
        gf.update_screen(ai_settings, screen, balls, player, players)
        print(balls)

run_game()
