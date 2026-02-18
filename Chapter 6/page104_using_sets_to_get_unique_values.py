Chapter 6/page104_using_sets_to_get_unique_values.py

Dictionary of favorite programming languages.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


 Using a set to show each language only once (no duplicates)

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())
