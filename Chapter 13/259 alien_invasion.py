# Chapter 13/259 alien_invasion.py

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Group for all aliens
        self.aliens = pygame.sprite.Group()

        # Build the initial fleet (now a whole row)
        self._create_fleet()

   CREATE FLEET (ROW) 
    def _create_fleet(self):
        """Create a full row of aliens across the screen (page 259)."""
        # Make an alien so we can get its size.
        alien = Alien(self)
        alien_width = alien.rect.width

        # Start placing aliens one alien width from the left edge.
        current_x = alien_width

        # Keep adding aliens until there's no room left for another alien + margin.
        while current_x < (self.settings.screen_width - 2 * alien_width):
            new_alien = Alien(self)
            new_alien.rect.x = current_x
            # Top row: y is one alien height down from the top.
            new_alien.rect.y = alien.rect.height
            self.aliens.add(new_alien)

            # Advance by alien width + one alien width spacing.
            current_x += 2 * alien_width

  MAIN LOOP 
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

  BULLET UPDATING 
    def _update_bullets(self):
        """Update bullets and remove those that have left the screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

 EVENT HANDLING 
ents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    FIRE BULLETS 
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

 DRAW EVERYTHING 
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        # Draw bullets behind ship
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw ship
        self.ship.blitme()

        # Draw the aliens row (page 259)
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
