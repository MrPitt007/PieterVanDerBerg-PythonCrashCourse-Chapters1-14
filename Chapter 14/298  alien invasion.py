# Chapter 14 / Page 298 — alien_invasion.py (inside _check_play_button)

def _check_play_button(self, mouse_pos):
    # --snip--
    if button_clicked and not self.game_active:
        # --snip--
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()      # ⬅ NEW ON PAGE 298
