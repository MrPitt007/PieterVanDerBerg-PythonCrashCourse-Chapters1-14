
 Single-file word count (matches the top of the page)

path = Path("alice.txt")  # move alice.txt next to this script to see the count

try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Approximate the number of words by splitting on whitespace
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")



 Working with Multiple Files — reusable helper

def count_words(path: Path):
    """Count the approximate number of words in a file and print a message."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


 Demo: analyze several titles (if present)
 Place any of these files next to this script to see their counts.
books = [
    Path("alice.txt"),
    Path("siddhartha.txt"),
    Path("moby_dick.txt"),
    Path("little_women.txt"),
]

print("\n--- Multiple files (if present) ---")
for book in books:
    count_words(book)


