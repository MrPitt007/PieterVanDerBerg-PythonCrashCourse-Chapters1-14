 Chapter 7/page117_even_or_odd_modulo_and_intro_to_while_loops.py


 Even or odd? Using modulo (%) to test parity


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


 Introduction to while loops
 Counts from 1 to 5

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
