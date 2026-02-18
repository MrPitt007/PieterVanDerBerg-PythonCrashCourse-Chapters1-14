# Chapter 6/page99_looping_through_dictionaries.py

# A dictionary storing user information.
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Looping through all key-value pairs in the dictionary.
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
