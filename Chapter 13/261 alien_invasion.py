# Chapter 13/261 alien_invasion.py

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
        self.aliens = pygame.sprite.Group()

         Build the full fleet (multiple rows)
        self._create_fleet()

  
      CREATE FULL FLEET (ROWS + COLUMNS)
 
    def _create_fleet(self):
        """Create the fleet of aliens — multiple rows (page 261)."""
        # Make an alien to get size.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

         Start x and y positions.
        current_x = alien_width
        current_y = alien_height

         OUTER LOOP — add rows until screen-height limit is reached.
        while current_y < (self.settings.screen_height - 3 * alien_height):

             INNER LOOP — fill one row left to right.
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width  # spacing

             Reset for next row.
            current_x = alien_width
            current_y += 2 * alien_height  # move down

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it at the given row/column."""
        alien = Alien(self)
        alien.rect.x = x_position
        alien.rect.y = y_position
        self.aliens.add(alien)

   
       MAIN GAME LOOP
   
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

  
      BULLET UPDATING
  
  def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

   

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


       FIRING BULLETS
  
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


       DRAW EVERYTHING
   
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

         Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

         Draw ship
        self.ship.blitme()

       Draw aliens (full fleet)
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
