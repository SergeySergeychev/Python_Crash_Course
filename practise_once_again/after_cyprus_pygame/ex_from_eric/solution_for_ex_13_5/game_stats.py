class GameStats():
    """Track statistic for Catch the fireball."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Catch the fireball in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.balls_left = self.ai_settings.ball_limit
