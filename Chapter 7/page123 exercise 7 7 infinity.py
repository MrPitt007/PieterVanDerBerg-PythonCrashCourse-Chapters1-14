
Intentionally demonstrates an infinite loop.
KEEP THIS COMMENTED OUT to avoid locking your session.
To stop an accidental infinite loop in a terminal: press CTRL+C.
"""

 x = 1
 while x <= 5:
    print(x)
     # Missing: x += 1  # Without this, the loop never ends.
