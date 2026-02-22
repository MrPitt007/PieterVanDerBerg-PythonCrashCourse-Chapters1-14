
 Basic try/except demonstration (ZeroDivisionError)


print("=== Basic try/except ZeroDivisionError ===")

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")


Division calculator (matches page 193 example)


print("\nGive me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        # Convert both inputs to ints and divide
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Please enter valid numbers (or 'q' to quit).")
    else:
        print("Result:", answer)


