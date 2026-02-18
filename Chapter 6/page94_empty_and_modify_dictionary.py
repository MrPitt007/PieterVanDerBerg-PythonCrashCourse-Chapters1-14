alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_color_before = alien_0['color']
alien_0['color'] = 'yellow'

print(f"The alien was {alien_color_before}, now is {alien_0['color']}.")
