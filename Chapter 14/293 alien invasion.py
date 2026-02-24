# Chapter 14 / Page 293 — alien_invasion.py (inside _check_bullet_alien_collisions)

def _check_bullet_alien_collisions(self):
    # if collisions occur:
    if collisions := pygame.sprite.groupcollide(self.bullets, self.aliens, True, True):
        for aliens in collisions.values():
            self.stats.score += self.settings.alien_points * len(aliens)
        self.sb.prep_score()
        self.sb.check_high_score()
