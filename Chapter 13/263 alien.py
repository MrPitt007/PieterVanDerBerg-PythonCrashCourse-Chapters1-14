# Chapter 13/263 alien.py

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings    # NEW on page 263

        # Load image and rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Default starting position near top-left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store precise float for the x position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right (page 263)."""
        🧠 What page 263 teaches you

### ✔ Aliens need their own speed setting  
Stored in `settings.py` so you can change difficulty later.

### ✔ Aliens move using floats, like the ship  
Using `self.x` prevents jittering and keeps motion smooth.

### ✔ Aliens now move right continuously  
…but they don’t change direction or drop down yet.  
That comes on the next several pages.

### ✔ You now must call `aliens.update()` in alien_invasion.py  
Page 264 will add:

```python
self.aliens.update()
