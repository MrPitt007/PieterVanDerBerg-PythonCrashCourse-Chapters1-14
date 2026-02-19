
 Using continue in a while loop
Prints only odd numbers from 1 to 9


current_number = 0
while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue  # skip even numbers

    print(current_number)


 Avoiding infinite loops
 Correct counting loop (prints 1 to 5)


x = 1
while x <= 5:
    print(x)
    x += 1


 Example of an infinite loop (DO NOT RUN)

 x = 1
 while x <= 5:
    print(x)   # Missing x += 1 → loop runs forever
