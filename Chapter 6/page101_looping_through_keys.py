 Chapter 6/page101_looping_through_keys.py

 Dictionary of favorite programming languages.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


 Looping through all keys using the keys() method

print("Names of everyone who took the poll:")
for name in favorite_languages.keys():
    print(name.title())


 Looping through keys WITHOUT .keys()  (default dictionary loop)
 This produces the same output as the loop above.


print("\nSame list, looping without keys():")
for name in favorite_languages:
    print(name.title())

 Looping through selected friends and printing personalized messages
(Based on the upcoming example on the page)


friends = ['phil', 'sarah']

print("\nMessages to friends:")
for name in favorite_languages:
    print(f"Hi {name.title()}!")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"  I see you love {language}!")
