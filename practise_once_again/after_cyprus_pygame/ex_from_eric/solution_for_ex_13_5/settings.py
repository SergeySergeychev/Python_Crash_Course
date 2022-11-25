class Settings():
    """A class to store all settings of the Catch the Ball game."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Player settings.
        self.player_speed_factor = 4
        # Ball settings.
        self.ball_falling_speed = 1
        self.ball_limit = 3
