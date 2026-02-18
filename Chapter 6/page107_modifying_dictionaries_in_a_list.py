# Chapter 6/page107_modifying_dictionaries_in_a_list.py

# -------------------------------------------------------------
# Start with a list of freshly-created green aliens.
# -------------------------------------------------------------

Create 30 green aliens.
aliens = []
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)


# Modify the first 3 aliens.

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

 Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")


 Expanded version (not run here):
 Turning yellow aliens into fast red aliens worth 15 points.


 for alien in aliens[:3]:
     if alien['color'] == 'green':
         alien['color'] = 'yellow'
         alien['speed'] = 'medium'
         alien['points'] = 10
        elif alien['color'] == 'yellow':
         alien['color'] = 'red'
         alien['speed'] = 'fast'
         alien['points'] = 15
