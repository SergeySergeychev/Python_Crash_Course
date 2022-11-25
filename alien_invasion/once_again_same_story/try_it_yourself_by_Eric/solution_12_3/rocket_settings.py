class Settings():
    """A Class to store all sieting for Rocket Luncher"""

    def __init__(self):
        """Initialize the games's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250, 250, 250)
        # Rocket settings.
        self.rocket_speed_factor = 1.7
