

import sys
import pygame

from raindrop import Raindrop

def check_events():
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(ai_settings, screen, raindrops):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass trough the screen.
    screen.fill(ai_settings.bg_color)
    # Draw raindrop rectangle

    raindrops.draw(screen) # !!! CHECKING IT !!!

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_raindrops_x(ai_settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    available_space_x = ai_settings.screen_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x

def get_number_rows(ai_settings, raindrop_height):
    """Determine number of rows of raindrops that fit on the screen"""
    available_space_y =  raindrop_height
    number_rows = int(available_space_y / (raindrop_height))
    return number_rows

def create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number):
    """Create a raindrop and place it in a row."""
    # Create a single raindrop.
    raindrop = Raindrop(ai_settings, screen)
    # Measure the raindrops width and height.
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    # Place raindrops by x,y axis.
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.y = raindrop_height + 2 * raindrop_height * row_number
    # Update raindrops rect position.
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop.y
    # Add raindrop to Group.
    raindrops.add(raindrop)


def create_rain(ai_settings, screen, raindrops):
    """Create beautiful raindrop fall."""
    # Create a raindrop and find the number of raindrops in a row.
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop.rect.width)
    number_rows = get_number_rows(ai_settings, raindrop.rect.height)
    # Create the first row of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            # Create a raindrop and place it in the row.
            create_raindrop(ai_settings, screen, raindrops, raindrop_number,
                            row_number)
def start_the_rain(ai_settings, screen, raindrops):
    """Start the rain if it is ended."""
    heavy_rain = False
    for raindrop in raindrops.copy():
        if raindrop.check_edges():
            raindrops.remove(raindrop)
            heavy_rain = True
    if heavy_rain:
        create_rain(ai_settings, screen, raindrops)

def update_raindrop(ai_settings, screen, raindrops):
    """
    Update posiiton of raindrop.
    Get rid of old raindrops.
    Start the rain.
    """
    raindrops.update()
    start_the_rain(ai_settings, screen, raindrops)
