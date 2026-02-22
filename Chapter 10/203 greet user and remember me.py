

# Try to load an existing username.
# If file exists → greet returning user.
# If not → ask for name and store it.

def greet_user():
    path = Path("username.json")

    if path.exists():
        # File exists: load the stored username
        contents = path.read_text(encoding="utf-8")
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        # File does not exist: ask for a new username
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents, encoding="utf-8")
        print(f"We'll remember you when you come back, {username}!")


# Run the program

greet_user()

