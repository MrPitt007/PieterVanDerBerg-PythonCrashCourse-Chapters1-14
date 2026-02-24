# Chapter 13/271 game_stats.py

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # In Chapter 13 we keep stats always active; a 'game_active' flag comes later.
        # self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Ships left (decrement when the ship is hit).
        self.ships_left = self.settings.ship_limit
