# Chapter 12/239 alien_invasion.py

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # Clock for frame rate
        self.clock = pygame.time.Clock()

        # Settings
        self.settings = Settings()

        # Screen setup
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Game objects
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            # Update game elements
            self.ship.update()

            # Draw everything
            self._update_screen()
            self.clock.tick(60)

    # --- Helper / internal methods (page 239 additions) ---

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # New on page 239: respond to RIGHT arrow key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Start moving to the right
                    self.ship.moving_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Stop moving to the right
                    self.ship.moving_right = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
