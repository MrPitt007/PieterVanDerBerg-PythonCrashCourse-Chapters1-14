
from pathlib import Path


Write one line to a text file

path.write_text("I love programming.", encoding="utf-8")

(No terminal output is required by the book, but we verify by reading back.)
contents = path.read_text(encoding="utf-8")
print("=== programming.txt ===")
print(contents)

