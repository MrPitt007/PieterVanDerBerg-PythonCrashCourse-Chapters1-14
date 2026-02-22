
from pathlib import Path


Ensure demo file exists (same 3 lines shown in the book)

path = Path("pi_digits.txt")
if not path.exists():
    path.write_text(
        "3.1415926535\n"
        "8979323846\n"
        "2643383279\n",
        encoding="utf-8",
    )

contents_raw = path.read_text(encoding="utf-8")
print("=== RAW (with trailing newline from read_text) ===")
print(contents_raw)  # shows a blank line at the end


Strip the trailing newline using rstrip() and print again

contents_stripped = contents_raw.rstrip()
print("=== STRIPPED (rstrip removes the extra blank line) ===")
print(contents_stripped)

 Method chaining: call rstrip() immediately on read_text()

contents_chain = path.read_text(encoding="utf-8").rstrip()
print("=== METHOD CHAINING RESULT ===")
print(contents_chain)

