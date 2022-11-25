import pygame
import random
import sys
from player import Player
from ball import Ball
from game_stats import GameStats
from time import sleep

def check_keydown_events(event, player):
    """Respond to keypress."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, player):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    if event.key == pygame.K_LEFT:
        player.moving_left = False

def check_events(player):
    """Respond to keypress and mouse releases."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

def get_number_balls_x(ai_settings, ball_width):
    """Determine number of balls that fit in a row."""
    available_space_x = ai_settings.screen_width - ball_width
    number_balls_x = int(available_space_x /(ball_width))
    return number_balls_x

def get_random_number(ai_settings, ball_width):
    """Get randoom number in range of 0 to number_ball_x."""
    n = random.randint(0, get_number_balls_x(ai_settings, ball_width))
    return n


def create_ball(ai_settings, screen, balls):
    """Create a ball and place it in random place."""
    ball = Ball(ai_settings, screen)
    ball_width = ball.rect.width
    ball_height = ball.rect.height
    ball.x = ball_width * get_random_number(ai_settings, ball_width)
    ball.y = ball_height
    ball.rect.x = ball.x
    ball.rect.y = ball.y
    balls.add(ball)

def update_ball(ai_settings,screen, player, players, balls, stats):
    """Update position of ball and get rid of old balls."""
    # Update ball position.
    balls.update()

    # Get rid of balls that have disappeared
    ball_hit_the_floor(ai_settings, screen, balls, player, stats)
    # If player catched the ball create new one.
    check_ball_player_collisions(ai_settings, screen, players, balls,)

def check_ball_player_collisions(ai_settings, screen, players, balls,):
    """Respond to ball-player collisions."""
    # Remove any balls that have collided and create new ball.
    collisions = pygame.sprite.groupcollide(balls, players, True, False)
    if len(balls) == 0:
        # Create new ball.
        create_ball(ai_settings, screen, balls)

def update_screen(ai_settings, screen, balls, player, players):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Draw the player and add it to Group.
    players.add(player)
    players.draw(screen)
    # Draw the player and ball at its current position.
    balls.draw(screen)


    # Make the most recently drawn screen visible.
    pygame.display.flip()

def miss_ball(ai_settings, screen, balls, player, stats):
    """Respond if ball hit the floor."""
    if stats.balls_left > 0:
        # Decrement balls_left.
        stats.balls_left -=1
        #Empty the list of the balls.
        balls.empty()

        # Create a new ball and center the player.
        create_ball(ai_settings, screen, balls)
        player.take_center()

        sleep(0.5)
    else:
        stats.game_active = False

def ball_hit_the_floor(ai_settings, screen, balls, player, stats):
    """Check if ball hit bottom edge of the floor."""
    screen_rect = screen.get_rect()
    for ball in balls.sprites():
        if ball.rect.bottom >= screen_rect.bottom:
            miss_ball(ai_settings, screen, balls, player, stats)
            break
