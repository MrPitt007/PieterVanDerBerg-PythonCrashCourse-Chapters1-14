Chapter 6/page102 looping keys with conditions and membership.py

Dictionary of favorite programming languages.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

 List of friends.
friends = ['phil', 'sarah']


Looping through keys and printing a special message for friends


for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"  {name.title()}, I see you love {language}!")


Checking whether a specific person took the poll

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")
