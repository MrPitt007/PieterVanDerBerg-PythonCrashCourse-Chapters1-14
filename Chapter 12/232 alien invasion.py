 Chapter 12/232 alien_invasion.py

import sys
import pygame
from settings import Settings

class AlienInvasion:
    Overall class to manage game assets and behavior.

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()

         NEW (page 232): create a Settings instance
        self.settings = Settings()

         Use screen settings from Settings instance
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

             Fill screen using settings background color
            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
