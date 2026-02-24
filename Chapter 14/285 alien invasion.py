# NEW PAGE 285 — increase game speed after last alien is destroyed

def _update_bullets(self):
    self.bullets.update()

    for bullet in list(self.bullets):
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True
    )

    if not self.aliens:
        # Destroy existing bullets
        self.bullets.empty()

        # Create a new fleet
        self._create_fleet()

        # NEW PAGE 285 — increase game speed
        self.settings.increase_speed()
