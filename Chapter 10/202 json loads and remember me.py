
# PART 1 — Load numbers back from JSON
# Mirrors: reading numbers.json and using json.loads()


# Ensure numbers.json exists (so the demo always runs).
# If you already created it on page 201, this will just overwrite with the same data.
numbers_path = Path("numbers.json")
if not numbers_path.exists():
    numbers = [2, 3, 5, 7, 11, 13]
    numbers_path.write_text(json.dumps(numbers), encoding="utf-8")

 Read JSON text from the file and convert back to Python data.
contents = numbers_path.read_text(encoding="utf-8")
numbers_loaded = json.loads(contents)   # JSON string -> Python object (list)

print("Loaded numbers:", numbers_loaded)   # -> [2, 3, 5, 7, 11, 13]



# PART 2 — Saving and reading user-generated data
# Mirrors: prompt for username, store to username.json, confirm message


# In a non-interactive environment, you can swap the input() line
# with a hardcoded value; here we keep input(), as in the book.
username = input("\nWhat is your name? ")

user_path = Path("username.json")
user_json = json.dumps(username)
user_path.write_text(user_json, encoding="utf-8")

print(f"We'll remember you when you come back, {username}!")


