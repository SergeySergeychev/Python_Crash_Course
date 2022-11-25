
import sys

import pygame

from sett import Settings

from picture import Picture

def run_picture():
    # Initialize picture and creeate a screen object.
    pygame.init()
    p_settings = Settings()
    screen = pygame.display.set_mode(
        (p_settings.screen_width, p_settings.screen_height))
    pygame.display.set_caption("Picture in the center")

    # Make a picture.
    picture = Picture(screen)

    # Start the main loop for the picture.

    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw the screen during each pass throught the loop
        screen.fill(p_settings.bg_color)
        picture.blitme

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_picture()
