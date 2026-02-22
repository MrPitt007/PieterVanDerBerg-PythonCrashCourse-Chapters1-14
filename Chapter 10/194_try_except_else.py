 Demonstration: what happens WITHOUT try/except (crashes)
 (This is shown on the page but commented to avoid a real crash.)

print("First number: 5") print("Second number: 0")
print(5 / 0)   # -> ZeroDivisionError traceback (not user-friendly)



 Using try/except/else to prevent crashes


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        # This runs ONLY if the try-block succeeds (i.e., no ZeroDivisionError)
        print("Result:", answer)


