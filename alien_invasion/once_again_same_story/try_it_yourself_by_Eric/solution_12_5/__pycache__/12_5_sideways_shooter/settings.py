
class Settings():
    """Class to store settings"""
    def __init__(self):
        """Initialize settings of the screen, ship and bullets."""
        # Settings of the screen
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Settings of the ship.
        self.pokeball_master_speed_factor = 1.5

        # Settings of the pokeball.
        self.pokeball_speed_factor = 5
        self.pokeball_allowed = 10
