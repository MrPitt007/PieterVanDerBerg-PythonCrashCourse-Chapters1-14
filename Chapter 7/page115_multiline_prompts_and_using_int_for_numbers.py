
 Building a multi-line prompt using string concatenation

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name}!")


 Demonstrating input() returning strings


 age = input("How old are you? ")
 print(age)          # -> e.g., "21"  (always a string)


 Converting input to an integer using int()

 age = input("How old are you? ")
 age = int(age)      # Convert string "21" -> number 21
 print(age >= 18)    # Now comparisons work correctly
