# Chapter 14/291 scoreboard.py

import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image (rounded, with commas) and position it."""
        # Round to nearest 10, then format with commas (e.g., 1,530)
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"

        # Render against the screen background color
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Position at top-right, 20 px from right/top edges
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
