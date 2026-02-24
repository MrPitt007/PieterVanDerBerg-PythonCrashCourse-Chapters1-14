def _check_play_button(self, mouse_pos):
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.game_active:

        # NEW PAGE 285 — reset dynamic settings
        self.settings.initialize_dynamic_settings()

        # Reset stats
        self.stats.reset_stats()

        pygame.mouse.set_visible(False)
        self.game_active = True

        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()
