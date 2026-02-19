 Chapter 7/page116_using_int_in_conditions_and_modulo_operator.py


Converting input to an int before comparisons
 (rollercoaster height check)

 Converting input to an int before comparisons
 (rollercoaster height check)

height = input("How tall are you, in inches? ")
height = int(height)  # convert the string to an integer

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

print("\nModulo operator examples:")
print("4 % 3 =", 4 % 3)   # 1
print("5 % 3 =", 5 % 3)   # 2
print("6 % 3 =", 6 % 3)   # 0  (divides evenly)
print("7 % 3 =", 7 % 3)   # 1

 Practical check: is a number even or odd?
number = int(input("\nEnter a number and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
