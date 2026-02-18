alien_0 = {'color': 'green', 'points': 5}
print("Original:", alien_0)

del alien_0['points']
print("After deleting 'points':", alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
