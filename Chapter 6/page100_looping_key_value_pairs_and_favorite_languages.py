# Chapter 6/page100_looping_key_value_pairs_and_favorite_languages.py

# Looping through key-value pairs in a dictionary using descriptive variable names.

# Example dictionary storing user information:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Looping through all key-value pairs:
for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

# ---------------------------------------------------------
# Looping through another dictionary: favorite languages.
# ---------------------------------------------------------

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Looping with descriptive names:
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
