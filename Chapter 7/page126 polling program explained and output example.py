
Polling program (same logic as page 125, but shown with example output)


responses = {}          # Dictionary to store name → mountain
polling_active = True   # Flag to keep the loop running

while polling_active:
    # Ask for the person's name
    name = input("\nWhat is your name? ")

     Ask for the mountain they want to climb
    response = input("Which mountain would you like to climb someday? ")

     Store the response
    responses[name] = response

     Ask if anyone else should respond
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

 Polling is complete — show results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
