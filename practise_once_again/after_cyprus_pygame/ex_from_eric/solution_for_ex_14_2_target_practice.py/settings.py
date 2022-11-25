
class Settings():
    """A  class to store all settings for game 'Rectangle Invasion'."""
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Ship settings:
        self.ship_life_limit = 3

        # Rectangle settings:
        self.rectangle_width = 40
        self.rectnagle_height = 60
        self.rectnagle_color = (0, 0, 255)



        # Bullet settings:
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 0 , 0)
        self.bullets_allowed = 3

        # How quick the game speed up
        self.speedup_scale = 1.5

        # Initialize dynamic settings.
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the game's dynamic settings."""
        self.ship_speed_factor = 2
        self.rectangle_speed_factor = 0.1
        self.bullet_speed_factor = 4

        # Direction of the rectangles is down with 1 and up with -1.
        self.rectangle_direction = 1

    def increase_speed(self):
        """Increase speed parameters."""
        self.ship_speed_factor *= self.speedup_scale
        self.rectangle_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
