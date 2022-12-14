import sys

import pygame

from bullet import Bullet

from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
    # Attribute type is telling us which event the object represents.
    #checking if the event object's type is equal to the constant QUIT.
        if event.type == pygame.QUIT:
        # Function sys.exit terminate's the program.
            sys.exit()
        # Check if a key button is pressed.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # Check if a key button is up.
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    # Quit from the game if 'q' is pressed.
    if event.key == pygame.K_q:
        sys.exit()
    # Check if the right key is down.
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Check if the left key is down.
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # Check if space is down.
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Respond to key releases."""
        # Check right key button.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        # Check left key button.
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw all bullets behid ship and aliens.
    # Redraw the screen during each pass throught the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create an alien and find the number of aliens in a row."""
    # Create an aline and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    # Create the fleet of aliens.
    for row_number in range (number_rows):
        for alien_number in range(number_aliens_x):
            #Create an alien and place it in the row.
            create_alien(ai_settings,screen, aliens, alien_number,
                row_number)
def get_number_aliens_x(ai_settings, alien_width):
    """Detetermine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
        (3 *alien_height ) - ship_height)

    number_rows = int(available_space_y/(2*alien_height))
    return number_rows
