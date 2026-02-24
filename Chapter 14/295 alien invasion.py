# Chapter 14 / Page 295 — alien_invasion.py (inside _check_bullet_alien_collisions)

def _check_bullet_alien_collisions(self):
    # --snip--
    if not self.aliens:
        # Destroy existing bullets and create a new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()
