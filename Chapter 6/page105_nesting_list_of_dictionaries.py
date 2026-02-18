Chapter 6/page105_nesting_list_of_dictionaries.py

Demonstrating a list of dictionaries (nesting)

Each alien is represented as its own dictionary.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

A list that contains all three alien dictionaries.
aliens = [alien_0, alien_1, alien_2]

Looping through the list and printing each dictionary.
for alien in aliens:
    print(alien)
