# Chapter 6/page98_get_method_and_missing_keys.py

# A dictionary that does not include a 'points' key.
alien_0 = {'color': 'green', 'speed': 'slow'}

# Accessing a missing key with [] would raise a KeyError:
# print(alien_0['points'])  # Uncomment to test the error.

# Using get() prevents the crash by returning a default value.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
