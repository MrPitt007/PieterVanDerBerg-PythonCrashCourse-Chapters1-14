# Chapter 14 / Page 293  scoreboard.py (prep_high_score)

def prep_high_score(self):
    """Turn the high score into a rendered image."""
    high_score = round(self.stats.high_score, -1)
    high_score_str = f"{high_score:,}"

    self.high_score_image = self.font.render(
        high_score_str, True,
        self.text_color, self.settings.bg_color
    )

    # Center the high score at the top of the screen.
    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.centerx = self.screen_rect.centerx
    self.high_score_rect.top = self.score_rect.top
