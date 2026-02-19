

 Improved version of the parrot program:
 Do NOT print the word "quit" when the user enters it.


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':   # Only print non-quit messages
        print(message)
