# Chapter 14 / Page 297 — scoreboard.py (__init__)

def __init__(self, ai_game):
    """Initialize scorekeeping attributes."""
    self.ai_game = ai_game
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ai_game.settings
    self.stats = ai_game.stats

    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont(None, 48)

    # Prepare images.
    self.prep_score()
    self.prep_high_score()
    self.prep_level()
    self.prep_ships()      
