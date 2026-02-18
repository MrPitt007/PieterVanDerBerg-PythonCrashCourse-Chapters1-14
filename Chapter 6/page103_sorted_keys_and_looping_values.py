Chapter 6/page103_sorted keys and looping values.py

 Dictionary of favorite programming languages.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


Looping through all keys in sorted order

print("People who took the poll (sorted alphabetically):")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


Looping through all values in a dictionary

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
