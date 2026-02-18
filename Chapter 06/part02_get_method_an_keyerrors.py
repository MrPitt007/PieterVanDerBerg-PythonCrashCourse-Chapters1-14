# chapter_06/part02_get_method_and_keyerrors.py

# A dictionary without a 'points' key.
alien_0 = {'color': 'green', 'speed': 'slow'}

# Accessing a missing key with [] would cause a KeyError:
# print(alien_0['points'])  # Uncomment to see the error

# Using get() avoids the KeyError by returning a default value.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
