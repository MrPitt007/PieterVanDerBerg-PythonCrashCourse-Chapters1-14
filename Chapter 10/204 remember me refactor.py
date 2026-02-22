

USER_PATH = Path("username.json")


def get_stored_username(path: Path) -> str | None:
    """Get stored username if available; return None if the file is missing."""
    if path.exists():
        contents = path.read_text(encoding="utf-8")
        try:
            username = json.loads(contents)
        except json.JSONDecodeError:
            # Corrupted or unexpected file content; treat as not found
            return None
        return username
    return None


def get_new_username(path: Path) -> str:
    """Prompt for a new username, save it to JSON, and return it."""
    username = input("What is your name? ")
    path.write_text(json.dumps(username), encoding="utf-8")
    return username


def greet_user():
    """Greet the user by name. Load if remembered; otherwise ask and store."""
    username = get_stored_username(USER_PATH)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(USER_PATH)
        print(f"We'll remember you when you come back, {username}!")


if __name__ == "__main__":
    greet_user()

  
