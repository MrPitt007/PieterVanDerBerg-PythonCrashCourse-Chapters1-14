# Chapter 14 / Page 291  — settings.py

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # --snip--

        # Scoring
        self.alien_points = 50
        self.score_scale = 1.5

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)    # For debugging as shown in the book
