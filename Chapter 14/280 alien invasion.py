# Chapter 14/280 alien_invasion.py

import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button     # NEW PAGE 280

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create screen object
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Game statistics
        self.stats = GameStats(self)

        # Game starts inactive (page 278)
        self.game_active = False

        # Create game objects
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create initial fleet
        self._create_fleet()

        # NEW PAGE 280 — create the Play button
        self.play_button = Button(self, "Play")

   
    MAIN LOOP
   
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

  
     BULLET UPDATES
   
    def _update_bullets(self):
        self.bullets.update()

        # Remove bullets that leave the screen
        for bullet in list(self.bullets):
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Handle bullet–alien collisions
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # If fleet destroyed, recreate it
        if not self.aliens:
            self._create_fleet()

   
     ALIEN UPDATES
   
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

  
     SHIP-HIT HANDLING
    
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Reset fleets and bullets
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
       _active = False

  
     EVENT HANDLING
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Next page (281) will handle detecting clicks

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


     FIRING BULLETS
   
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

  
    DRAW THE SCREEN
    
    def _update_screen(self):
        """Draw screen elements and the Play button when inactive."""
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        # NEW PAGE 280 — draw the Play button when game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
