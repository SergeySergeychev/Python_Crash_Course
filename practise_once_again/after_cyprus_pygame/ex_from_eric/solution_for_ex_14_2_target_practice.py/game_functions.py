import sys
import pygame

from time import sleep

from bullet import Bullet
from rectangle import Rectangle

def check_keydown_events(event, ai_setting, screen, stats, ship,bullets):
    """Respond to keypress."""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_setting, screem, stats, ship, bullets,)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, play_button, ship, bullets,
                rectnagle):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship,
                bullets)
        elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship,
                bullets, mouse_x, mouse_y, rectnagle)

def check_play_button(ai_settings, screen, stats, play_button, ship,
                bullets, mouse_x, mouse_y, rectangles):
    """Start a new game when the player clicks on play button."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings, screen, stats, ship, bullets, rectangles)

def start_game(ai_settings, screen, stats, ship, bullets, rectangles):
    """Start a new game."""
    # Hide the mouse cursor.
    pygame.mouse.set_visible(False)
    # Reset the game statistic.
    stats.reset_stats()
    stats.game_active = True
    # Empty the list of bullets.
    bullets.empty()
    rectangles.empty()
    # Center rectangle.
    create_rectangle(ai_settings, screen, rectangles)
    # Center ship.
    ship.center_ship()

def update_bullets(ai_settings, screen, stats, ship, bullets,
                    rectangles):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get screen rect.
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.right >= screen_rect.right:
            miss_hit(ai_settings, stats, screen, ship, bullets, rectangles)
    # Get rid of missed bullet.
    # Check for bullet that hit the rectangle.
    # IF so get rid of the bullet and the rectangle.
    # Destroy existing bullets and create new fleet.
    check_bullet_rectangle_collisions(ai_settings, screen, ship, bullets,
                                         rectangles)

def check_bullet_rectangle_collisions(ai_settings, screen, ship, bullets,
                                         rectangles):
    """Respond to bullet-rectangle collision."""

    if pygame.sprite.groupcollide(rectangles, bullets, True, True):
        ai_settings.increase_speed()
        create_rectangle(ai_settings, screen, rectangles)

def create_rectangle(ai_settings, screen, rectangles):
    """Create an rectangle and add it to the group."""
    rectangle = Rectangle(ai_settings, screen)
    screen_rect = screen.get_rect()

    rectangle.rect.centery = screen_rect.centery
    rectangle.rect.right = screen_rect.right
    rectangles.add(rectangle)

def check_rectangle_edges(ai_settings, rectangles):
    """Respond appropriately if any rectangle have reached an edge."""
    for rectangle in rectangles.sprites():
        if rectangle.check_edges():
            change_rectangle_direction(ai_settings)
            break

def change_rectangle_direction(ai_settings):
    """Change direction of rectangle on opposite."""
    ai_settings.rectangle_direction *= -1


def miss_hit(ai_settings, stats, screen, ship, bullets, rectangles):
    # Get rid of missed bullet.
    if stats.ships_left > 0:
        bullets.empty()
        # Decrement ship_left.
        stats.ships_left -= 1
        # Center ship
        ship.center_ship()
        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_rectangle(ai_settings,  rectangles):
    """
    Check if the rectangle is at an edge of the screen.
    And then update position of the rectangle.
    """
    check_rectangle_edges(ai_settings, rectangles)
    rectangles.update()


def update_screen(ai_settings, stats, screen, bullets, rectangles, ship,
                    play_button):
    """Update  images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behid ship and rectangle.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for rectangle in rectangles.sprites():
        rectangle.draw_rectangle()
    ship.blitme()


    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    # make the most recently drawn screen visible.
    pygame.display.flip()
