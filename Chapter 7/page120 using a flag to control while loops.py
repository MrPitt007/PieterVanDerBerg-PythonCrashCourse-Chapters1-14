
 Using a flag to control a while loop


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True  # this is our flag variable

while active:
    message = input(prompt)

    if message == 'quit':
        active = False   # turn the flag off
    else:
        print(message)
