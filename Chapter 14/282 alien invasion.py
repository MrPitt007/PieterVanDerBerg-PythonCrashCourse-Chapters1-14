# Chapter 14/282 alien_invasion.py

import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


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

        # Page 278+: start inactive; Play button will activate
        self.game_active = False

        # Game objects
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create the initial fleet
        self._create_fleet()

        # Page 280: Play button
        self.play_button = Button(self, "Play")

  
     MAIN LOOP
    
    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    
     EVENT HANDLING
    
    def _check_events(self):
        """Respond to keypresses, releases, and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

  PAGE 282: START GAME FROM PLAY BUTTON 
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset game statistics (gives fresh ships_left, etc.)
            self.stats.reset_stats()

            # Hide the mouse cursor during active play (new on page 282)
            pygame.mouse.set_visible(False)

            # Reactivate the game
            self.game_active = True

            # Clear old aliens and bullets and set up a fresh state
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

   
    BULLETS
  
    def _fire_bullet(self):
        """Create a bullet if limit not reached."""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _update_bullets(self):
        """Update bullet positions and handle collisions/cleanup."""
        self.bullets.update()

        # Remove bullets that leave the screen
        for bullet in list(self.bullets):
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Bullet–alien collisions (remove both on hit)
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # If fleet is gone, create a new one
        if not self.aliens:
            self._create_fleet()

    
     ALIENS
  
    def _update_aliens(self):
        """Move aliens and handle collisions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Bottom-of-screen collision
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """If any alien reaches the bottom, treat as a ship hit."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

  
    SHIP HIT HANDLING
   
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Lose a ship
            self.stats.ships_left -= 1

            # Reset field
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

            # Brief pause
            sleep(0.5)
        else:
            # Game over: deactivate game (mouse visibility re-enabled later)
            self.game_active = False

 
     DRAW EVERYTHING
    
    def _update_screen(self):
        """Redraw the screen and, when inactive, draw the Play button."""
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the Play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

   
     FLEET CREATION
  
    def _create_fleet(self):
        """Create a full fleet of aliens (rows and columns)."""
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


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
