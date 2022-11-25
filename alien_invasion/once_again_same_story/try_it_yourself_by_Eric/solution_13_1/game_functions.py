# Write all functionality for star game.
# Write check events method to respond for key and mouse.
# Write update_screen method to draw image at it current location and redraw
# the screen.

# Write  a method create_stars. It has to draw stars in the sky.
# Create star and find out the number of stars in a row.
# Spacing between each star is equal to one star width.
# Create first row of stars.
# Add stars and calculate position of the first star. Update star position
# add to group of stars.

# Refactor create stars method.
# Split create_stars method for get_number_stars_x and create_single_star
# Method get_number_stars_x will determine the number of stars that fit
# in a row.
# Method create_single_star will create star and put it in the row.

# Write method and call it get_number_rows. It should determine the number of
# rows of stars that fit on the screen.
# Add star_y position to create_single_star.
# Add number_rows to create_stars.
# Create grid of stars.
import sys

import pygame

from star import Star

from random import randint
def check_events():
    """Check events to quit the game."""
    # Check mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Check keyboard events.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(s_settings, screen, stars):
    # Draw a background of the screen.
    screen.fill(s_settings.bg_color)
    # Draw the single star at its current location.
    # Draw stars in the sky.
    stars.draw(screen)
    #Make a most recetly object visibile.
    pygame.display.flip()

def get_number_stars_x(star_width, screen_width):
    """Detemine the number of stars that fit in a row."""
    available_space_x = screen_width - 2 * star_width
    number_stars_x = int(available_space_x /(2 * star_width))
    return number_stars_x

def get_number_rows(star_height, screen_height):
    """Determine the number of rows of stars that fit on the screen."""
    available_space_y = screen_height - 2 * star_height
    number_rows = int(available_space_y / (2 * star_height ))
    return number_rows
def create_single_star(s_settings, screen, star_number, stars, row_number):
    """Create a single star and put it in the row."""
    star = Star(screen)
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = star_width + (2 * star_width * star_number)
    star.y = star_height + (2 * star_height * row_number)
    star.rect.x = star.x
    star.rect.y = star.y
    stars.add(star)


def create_stars(s_settings, screen, stars):
    star = Star(screen)
    number_stars_x = get_number_stars_x(star.rect.width,
                                        s_settings.screen_width)
    number_rows = get_number_rows (star.rect.height,
                                   s_settings.screen_height)
    for row_number  in range(number_rows):
       for star_number in range(number_stars_x):
        create_single_star(s_settings, screen, star_number, stars, row_number)
