 Chapter 6/page109_nested_loops_list_values_in_dictionary.py


 A dictionary where each value is a list of favorite languages


favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

 Loop through the dictionary:
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")

     Loop through the list associated with each person:
    for language in languages:
        print(f"\t{language.title()}")
