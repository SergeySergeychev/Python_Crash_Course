# Import sys and pygame.
# Create method check_event.
# Method should respond to keypresses and mouse events.
# import game_functions to sideways_shooter.
# Rewrite While loop in sideways_shooter.

# Create method update_screen.Method should take three parameters.
# Parameters - ss_settings, screen, pokeball_master
# Method functionality is to update image on the screen and flip to new scr.
# Delete screen.fill, pokeball_master.blitme and display.flip from while loop.
# Add to while loop method update_screen.
# In while loop method update_screen will take three arguments.

# Add the pokeball_master parameter to check_event.
# Check_event method should to respond for down arrow if it pressed.
# And move picture to the bottom of the screen.
# Update while loop and add attribute pokeball_master to check_event method.

# Add conditional to check_events If key down is pressed.
# Flag pokeball_master.moving_down is True.
# Add new conditional block elif which responds to key up.
# Add if statement to elif block. If key down is not pressed.
# Flag pokeball_master.moving_down is False.

# Add conditional elif to check_events in elif KEYDOWN block.
# Conditional controls moving_up flag and sets it to True.
# Add conditional elif to check_events in elif KEYUP block
# Conditional controls moving_up flag and sets it to False.

# Refactoring check_events. Create def check_keydown_evnts and check_keyup_events.
# Provide methods with functionality to respond for key buttons.
# Refactor check_events , delete all keys and add new functions.

# Add Pokeball class.
# Add Three parameters to check_keydown_events: ss_settings, screen, pokeballs
# Add elif block to check_keyup_events.
# Elif block have to create a new pokeball and add it to the pokeballs Group
# When K_SPACE is pressed.
# Add to check_events three parameters ss_settings, screen, pokeballs.
# In KEYDOWN elif block , for check_keydown_evnts add parametrs of method.
# For update_screen add pokeballs.
# Write for loop inside update_screen to redraw all pokeballs.
import sys

import pygame

from pokeball import Pokeball

def check_events(ss_settings, screen, pokeball_master, pokeballs):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ss_settings, screen, pokeball_master, pokeballs)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pokeball_master)

def check_keydown_events(event, ss_settings, screen, pokeball_master, pokeballs):
    """Respond to keypresses."""
    if event.key == pygame.K_DOWN:
        pokeball_master.moving_down = True
    elif event.key == pygame.K_UP:
        pokeball_master.moving_up = True
    elif event.key ==pygame.K_SPACE:
        # Create new pokeball and add it to the pokeballs group.
        fire_pokeball(ss_settings, screen, pokeball_master, pokeballs)

def check_keyup_events(event, pokeball_master):
    """Respond to key releases."""
    if event.key == pygame.K_DOWN:
        pokeball_master.moving_down = False
    elif event.key == pygame.K_UP:
        pokeball_master.moving_up = False


def update_screen(ss_settings, screen, pokeball_master, pokeballs):
    """Update image on the screen and flip to new screen."""
    # Fill the background with color.
    screen.fill(ss_settings.bg_color)
    # Redraw all pokeballs.
    for pokeball in pokeballs.sprites():
        pokeball.blitme()

    # Copy picture to screen.
    pokeball_master.blitme()
    # Redraw the screen and make last picture visible.
    pygame.display.flip()

def update_pokeballs(pokeball_master, pokeballs):
    """Update position of pokeballs and get rid of old pokeballs."""
    # Update pokeballs position
    pokeballs.update()
    # Get rid of pokeballs that have disappeared.
    for pokeball in pokeballs.copy():
        if pokeball.rect.right >= pokeball_master.screen_rect.right:
            pokeballs.remove(pokeball)
    print(len(pokeballs))

def fire_pokeball(ss_settings, screen, pokeball_master, pokeballs):
    """Fire a pokeball if limit not reached yet."""
    # Create new pokeballs and ADD it to pokeballs Group.
    if len(pokeballs) < ss_settings.pokeball_allowed:
        new_pokeball = Pokeball(ss_settings, screen, pokeball_master)
        pokeballs.add(new_pokeball)
