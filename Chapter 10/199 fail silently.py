
 Helper: count words without printing any error if the file is missing
         (Fail silently using `pass` in the except block.)

def count_words(path: Path):
    """Count the approximate number of words in a file (fails silently if missing)."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # FAIL SILENTLY: choose to do nothing here
        # (Optionally, you could log missing filenames to a separate file.)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")



# Demo: some files exist, one intentionally missing

filenames = [
    "alice.txt",
    "siddhartha.txt",   # intentionally absent → will be ignored silently
    "moby_dick.txt",
    "little_women.txt",
]

for fname in filenames:
    count_words(Path(fname))

# • You will only see counts for files that exist.
# • Missing files produce no output and no traceback.


