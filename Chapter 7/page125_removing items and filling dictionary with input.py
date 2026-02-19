
Removing all instances of a specific value from a list


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("Original list of pets:")
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print("\nList after removing all 'cat' entries:")
print(pets)


 Filling a dictionary with user input (polling program)


responses = {}

 A flag to indicate that polling is active
polling_active = True

while polling_active:
    # Ask for the participant's name and response
    name = input("\nWhat is your name? ")
    mountain = input("Which mountain would you like to climb someday? ")

     Store the response in the dictionary
    responses[name] = mountain

     Ask if another person should be polled
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

 Polling complete; show results
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain.title()}.")
