# Chapter 13/273 alien_invasion.py

import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Screen setup
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Game statistics
        self.stats = GameStats(self)

        # Game objects
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

FLEET CREATION 
    def _create_fleet(self):
        probe = Alien(self)
        alien_width, alien_height = probe.rect.size

        current_x = alien_width
        current_y = alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x, y):
        alien = Alien(self)
        alien.rect.x = x
        alien.rect.y = y
        alien.x = float(alien.rect.x)
        self.aliens.add(alien)
      
 MAIN LOOP 
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

   BULLETS
    def _update_bullets(self):
        self.bullets.update()

         Remove bullets that leave top of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

         Check for bullet–alien collisions
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # If no aliens remain, create a new fleet
        if not self.aliens:
            self._create_fleet()

 ALIENS 
    def _update_aliens(self):
        """Check edges, update positions, detect ship hits."""
        self._check_fleet_edges()
        self.aliens.update()

        # PAGE 273: replace print with actual ship-hit method
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # (Bottom-of-screen collisions added next page)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
      
 SHIP HIT HANDLING 
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""

        # Decrement ships left
        self.stats.ships_left -= 1

        # Clear aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Respawn fleet and recenter ship
        self._create_fleet()
        self.ship.center_ship()

        # Pause
        sleep(0.5)

 BOTTOM-OF-SCREEN CHECK (added next page) 
    def _check_aliens_bottom(self):
        """Check if any aliens reach the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._ship_hit()
                break

     EVENT HANDLING 
    def _check_events(self):
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

    FIRING 
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    DRAW EVERYTHING 
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
