
 Helper function reused from page 197


def count_words(path: Path):
    """Count the approximate number of words in a file and print a report."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")



 List of filenames (as STRINGS, as shown in the book)

filenames = [
    "alice.txt",
    "siddhartha.txt",    # intentionally missing for demonstration
    "moby_dick.txt",
    "little_women.txt",
]

 Loop through each file and count words.
 Missing files DO NOT stop the program.


print("=== Word count for multiple text files ===")

for file in filenames:
    path = Path(file)     # convert string to Path object
    count_words(path)


