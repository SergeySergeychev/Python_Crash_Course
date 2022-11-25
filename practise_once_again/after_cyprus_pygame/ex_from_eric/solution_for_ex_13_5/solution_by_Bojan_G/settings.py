
class Settings(object):
    """Game settings."""
    def __init__(self):
        # Game settings.
        self.screen_width = 800
        self.screen_heigth = 600
        self.bg_color = (255, 255, 255)

        # Catcher settings.
        self.catcher_speed_factor = 1.5

        # Ball settings.
        self.ball_speed_factor = 1
        self.ball_limit = 3
