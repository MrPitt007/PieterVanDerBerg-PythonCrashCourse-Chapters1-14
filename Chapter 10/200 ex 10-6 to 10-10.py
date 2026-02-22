"""
Chapter 10 – Page 200
Exercises 10-6 to 10-10
Python Crash Course – Solutions (compact, runnable)

This script includes small demo files so it runs out-of-the-box.
"""

from pathlib import Path

# ==================================================
# Helpers: ensure small demo text files exist
# ==================================================
cats_path = Path("cats.txt")
dogs_path = Path("dogs.txt")
if not cats_path.exists():
    cats_path.write_text("Misty\nShadow\nLuna\n", encoding="utf-8")
if not dogs_path.exists():
    dogs_path.write_text("Rex\nBuddy\nMax\n", encoding="utf-8")

# Optional demo books (place big texts next to this script if you have them)
books = [
    Path("alice.txt"),
    Path("moby_dick.txt"),
    Path("little_women.txt"),
]

# ==================================================
# 10-6 — ADDITION (handle ValueError)
# ==================================================

def add_two_numbers(a_str: str, b_str: str):
    """Return the sum of two numbers given as strings; handle ValueError."""
    try:
        return float(a_str) + float(b_str)
    except ValueError:
        print("Please enter numeric values only.")
        return None

print("=== 10-6 Addition (one-off demo) ===")
print("5 + 7 =", add_two_numbers("5", "7"))
print("5 + 'x' =", add_two_numbers("5", "x"))

# ==================================================
# 10-7 — ADDITION CALCULATOR (loop with quit)
# ==================================================

def addition_calculator():
    """Prompt repeatedly for two numbers and print the sum. Enter 'q' to quit."""
    print("\n=== 10-7 Addition Calculator ===")
    print("Enter two numbers to add. Type 'q' at any prompt to quit.")
    while True:
        a = input("First number: ")
        if a.lower() == "q":
            break
        b = input("Second number: ")
        if b.lower() == "q":
            break
        result = add_two_numbers(a, b)
        if result is not None:
            print("Sum =", result)

# Uncomment to interact:
# addition_calculator()

# ==================================================
# 10-8 — CATS AND DOGS (report missing file)
# ==================================================

def print_file(path: Path):
    """Print the contents of a file, or a friendly message if missing."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} is missing.")
    else:
        print(f"\n--- {path} ---")
        print(text, end="")

print("\n=== 10-8 Cats and Dogs (with message) ===")
print_file(cats_path)
print_file(dogs_path)
print_file(Path("missing_pets.txt"))  # demonstrates the message

# ==================================================
# 10-9 — SILENT CATS AND DOGS (fail silently)
# ==================================================

def print_file_silent(path: Path):
    """Print file if present; otherwise do nothing (fail silently)."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # fail silently
        pass
    else:
        print(f"\n--- {path} (silent mode) ---")
        print(text, end="")

print("\n=== 10-9 Cats and Dogs (silent on missing) ===")
print_file_silent(cats_path)
print_file_silent(dogs_path)
print_file_silent(Path("missing_pets.txt"))  # no output

# ==================================================
# 10-10 — COMMON WORDS
# Count how many times a word appears in each text.
# Case-insensitive; uses str.lower().count(word).
# ==================================================

def count_word_in_file(path: Path, word: str):
    """Approximate count of 'word' in file (case-insensitive); report if missing."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Missing: {path} (skipping)")
        return
    lower_text = contents.lower()
    # naive count: counts substrings (e.g., 'the' in 'there'); acceptable for this exercise
    count = lower_text.count(word.lower())
    print(f"{path}: '{word}' appears about {count} times.")

print("\n=== 10-10 Common Words ===")
target_word = "the"  # change as desired; try ' the ' (with spaces) to reduce false matches
# Create one tiny demo text if big books aren’t present
demo = Path("tiny_demo.txt")
if not any(p.exists() for p in books):
    demo.write_text("Row, row, row your boat.\nThe river flows and the wind blows.\n", encoding="utf-8")
    books = [demo]

for book in books:
    count_word_in_file(book, target_word)
