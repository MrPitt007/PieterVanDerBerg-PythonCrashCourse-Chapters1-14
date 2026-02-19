

Counting from 1 to 5 with a while loop


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

 Letting the user decide when to quit (sentinel value)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""  initialize to something that is not 'quit'

while message != 'quit':
    message = input(prompt)
    print(message)
