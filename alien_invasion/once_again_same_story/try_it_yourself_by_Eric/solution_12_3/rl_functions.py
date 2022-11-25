# Add to method check_keydow_events two more buttons up and down.
# Add to check_keyup_events two more buttons up and down.


import sys

import pygame

def check_events(rocket):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,rocket)
            return event
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def check_keydown_events(event, rocket):
    """Respond to keypresses and mouse events."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    """"Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down= False



def update_screen(rl_settings, screen, rocket):
    """Update image on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(rl_settings.bg_color)
    rocket.blitme()

    # Make the most recently drawn scren visible.
    pygame.display.flip()
