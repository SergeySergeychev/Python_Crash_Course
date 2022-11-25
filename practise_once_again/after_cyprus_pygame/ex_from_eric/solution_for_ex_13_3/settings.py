# Write class settings for screen and raindrop.
    # In class setting Initialize the game's setting.
    # Write screen settings such as screen_width, screen_height, bg_color.
    # Write raindrop settings such as raindrops_speed_factor,


class Settings():
    """A class to store all setting for raindrop game."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen setting.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (211, 197, 184)

        # Raindrop settings.
        self.raindrop_speed_factor = 1
        self.ball_allowed = 1
