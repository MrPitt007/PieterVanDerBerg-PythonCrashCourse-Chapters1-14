
USER_PATH = Path("username.json")


def get_stored_username(path: Path) -> str | None:
    """Get stored username if available; return None otherwise."""
    if path.exists():
        contents = path.read_text(encoding="utf-8")
        try:
            return json.loads(contents)
        except json.JSONDecodeError:
            # File exists but isn't valid JSON; act as if not found.
            return None
    return None


def get_new_username(path: Path) -> str:
    """Prompt for a new username, store it, and return it."""
    username = input("What is your name? ")
    path.write_text(json.dumps(username), encoding="utf-8")
    return username


def greet_user():
    """Greet the user by name—load if remembered, else ask and remember."""
    username = get_stored_username(USER_PATH)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(USER_PATH)
        print(f"We'll remember you when you come back, {username}!")


if __name__ == "__main__":
    greet_user()
