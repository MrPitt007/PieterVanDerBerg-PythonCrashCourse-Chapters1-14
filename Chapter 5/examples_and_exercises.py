"""
Python Crash Course — Chapter 5: If Statements
Page 72 start — Examples + Exercises (5-1 to 5-7)

How to run:
    python examples_and_exercises.py
"""

# -----------------------------
# Section: Examples
# -----------------------------

def examples_basic_if():
    print("=== Example: Basic if vs else ===")
    cars = ['audi', 'bmw', 'subaru', 'toyota']
    for car in cars:
        if car == 'bmw':
            print(car.upper())  # BMW printed in uppercase
        else:
            print(car.title())  # Others in Title Case
    print()


def examples_if_elif_else():
    print("=== Example: if-elif-else chain ===")
    age = 4
    if age < 4:
        price = 0
    elif age < 18:
        price = 5
    else:
        price = 10
    print(f"Your admission cost is ${price}.")
    print()


def examples_boolean_and_or_not_in():
    print("=== Example: comparisons, and/or, in/not in ===")
    age_1 = 22
    age_2 = 18

    # and
    if age_1 >= 21 and age_2 >= 21:
        print("Both can drink.")
    else:
        print("At least one cannot.")

    # or
    requested_toppings = ['mushrooms', 'onions']
    if 'pepperoni' in requested_toppings or 'mushrooms' in requested_toppings:
        print("At least one desired topping is available.")

    # not
    is_open = False
    if not is_open:
        print("The store is closed.")

    # membership tests
    available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    if 'bacon' not in available_toppings:
        print("Sorry, we don't have bacon.")
    print()


# -----------------------------
# Exercises
# -----------------------------

def ex_5_1_conditional_tests():
    """
    5-1 Conditional Tests:
    Write a series of conditional tests. Print a statement describing each test and your prediction
    for the result. Create at least 10 tests and include both True and False results.
    """
    print("=== 5-1 Conditional Tests ===")
    tests = [
        ("apple" == "apple", True),
        ("Apple".lower() == "apple", True),
        (42 > 21, True),
        (3.14 < 3, False),
        (10 >= 10, True),
        (9 <= 8, False),
        ("a" != "b", True),
        ("python" in "i love python", True),
        ("java" in "i love python", False),
        (("x" not in ["a", "b", "c"]), True),
    ]
    for idx, (expr, expected) in enumerate(tests, 1):
        result = expr
        print(f"Test {idx}: expected={expected}, got={result} -> {'PASS' if result == expected else 'FAIL'}")
    print()


def ex_5_2_more_conditional_tests():
    """
    5-2 More Conditional Tests:
    Tests that cover string comparisons, lower(), numerical tests, and/or, and list membership.
    """
    print("=== 5-2 More Conditional Tests ===")
    # String comparisons
    print("String equality:", "hello" == "hello")
    print("String inequality:", "hello" != "world")

    # .lower()
    msg = "Hello"
    print("Lower equal:", msg.lower() == "hello")

    # Numerical tests
    a, b = 10, 20
    print("a < b:", a < b)
    print("a <= 10:", a <= 10)
    print("b > a:", b > a)
    print("b >= 21:", b >= 21)

    # and / or
    print("a < b and b < 30:", (a < b) and (b < 30))
    print("a > b or a == 10:", (a > b) or (a == 10))

    # in / not in
    items = ["python", "rust", "go"]
    print("'python' in items:", "python" in items)
    print("'java' not in items:", "java" not in items)
    print()


def ex_5_3_alien_colors_1():
    """
    5-3 Alien Colors #1:
    Imagine an alien was just shot down in a game. Create a variable called alien_color
    and assign it a value of 'green', 'yellow', or 'red'. Write an if statement to test
    whether the alien’s color is green. If it is, print a message that the player just
    earned 5 points.
    """
    print("=== 5-3 Alien Colors #1 ===")
    alien_color = 'green'
    if alien_color == 'green':
        print("You just earned 5 points!")
    print()


def ex_5_4_alien_colors_2():
    """
    5-4 Alien Colors #2:
    Choose a color and write an if-else chain. If the alien is green, print a message that
    the player earned 5 points. If the alien is not green, print 10 points.
    """
    print("=== 5-4 Alien Colors #2 ===")
    for alien_color in ['green', 'yellow']:
        if alien_color == 'green':
            print(f"Alien color: {alien_color} -> You earned 5 points.")
        else:
            print(f"Alien color: {alien_color} -> You earned 10 points.")
    print()


def ex_5_5_alien_colors_3():
    """
    5-5 Alien Colors #3:
    Turn your if-else chain from Exercise 5-4 into an if-elif-else chain:
    - If the alien is green, print 5 points
    - If yellow, print 10 points
    - If red, print 15 points
    """
    print("=== 5-5 Alien Colors #3 ===")
    for alien_color in ['green', 'yellow', 'red']:
        if alien_color == 'green':
            points = 5
        elif alien_color == 'yellow':
            points = 10
        else:
            points = 15
        print(f"Alien color: {alien_color} -> You earned {points} points.")
    print()


def ex_5_6_stages_of_life():
    """
    5-6 Stages of Life:
    Write an if-elif-else chain that determines a person’s stage of life:
    - < 2: baby
    - 2–3: toddler
    - 4–12: kid
    - 13–19: teenager
    - 20–64: adult
    - >= 65: elder
    """
    print("=== 5-6 Stages of Life ===")

    def life_stage(age: int) -> str:
        if age < 2:
            return "baby"
        elif age < 4:
            return "toddler"
        elif age < 13:
            return "kid"
        elif age < 20:
            return "teenager"
        elif age < 65:
            return "adult"
        else:
            return "elder"

    sample_ages = [0, 2, 3, 10, 16, 30, 70]
    for a in sample_ages:
        print(f"Age {a}: {life_stage(a)}")
    print()


def ex_5_7_favorite_fruit():
    """
    5-7 Favorite Fruit:
    Make a list of your favorite fruits, and then write a series of independent if statements
    that check for certain fruits in your list.
    """
    print("=== 5-7 Favorite Fruit ===")
    favorite_fruits = ['mango', 'banana', 'blueberry']

    if 'banana' in favorite_fruits:
        print("You really like bananas!")
    if 'mango' in favorite_fruits:
        print("You really like mangoes!")
    if 'apple' in favorite_fruits:
        print("You really like apples!")  # Won't print unless 'apple' is added
    if 'blueberry' in favorite_fruits:
        print("You really like blueberries!")
    print()


# -----------------------------
# Main
# -----------------------------

def main():
    # Examples
    examples_basic_if()
    examples_if_elif_else()
    examples_boolean_and_or_not_in()

    # Exercises
    ex_5_1_conditional_tests()
    ex_5_2_more_conditional_tests()
    ex_5_3_alien_colors_1()
    ex_5_4_alien_colors_2()
    ex_5_5_alien_colors_3()
    ex_5_6_stages_of_life()
    ex_5_7_favorite_fruit()


if __name__ == "__main__":
    main()
