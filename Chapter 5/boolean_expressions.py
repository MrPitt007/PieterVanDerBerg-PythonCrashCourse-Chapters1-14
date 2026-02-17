"""
Chapter 5 — Page 77: Boolean Expressions & State Tracking
Run:
  python page77_boolean_expressions.py
"""

print("=== Boolean Expressions ===")
game_active = True
can_edit = False
print("game_active =>", game_active)
print("can_edit =>", can_edit)
print()

# Demonstrate how booleans can control program flow
if game_active:
    print("The game is running...")
else:
    print("The game is paused.")

if can_edit:
    print("User can edit this content.")
else:
    print("User cannot edit this content.")

