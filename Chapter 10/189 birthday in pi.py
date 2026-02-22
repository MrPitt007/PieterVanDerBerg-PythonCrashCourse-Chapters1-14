
 Choose source file: prefer the large file if available

pi_large = Path("pi_million_digits.txt")
pi_small = Path("pi_digits.txt")

if pi_large.exists():
    src = pi_large
else:
    src = pi_small
    # Ensure small demo exists so the script always runs:
    if not pi_small.exists():
        pi_small.write_text(
            "3.1415926535\n"
            " 8979323846\n"
            " 2643383279\n",
            encoding="utf-8",
        )

print(f"Reading digits from: {src.name}")


 Build a single string of digits from the file
(strip left-padding spaces on each line)

contents = src.read_text(encoding="utf-8")
lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.lstrip()

 Optional: preview a small slice when using the big file
if src == pi_large:
    print(f"Preview: {pi_string[:52]}...")  # 3. + 50 decimals


 Get a birthday string to search for.
 Uncomment the input() line for interactive runs.


 birthday = input("Enter your birthday (e.g., mmddyy or mmddyyyy): ").strip()
birthday = "120327"  # demo value; change as you like (e.g., "12031992")


 Search for the birthday within pi_string

if birthday and birthday in pi_string:
    print(f"Your birthday ({birthday}) appears in the digits of pi!")
    # Optionally show where it appears (first index and surrounding context)
    idx = pi_string.find(birthday)
    start = max(idx - 5, 0)
    end = idx + len(birthday) + 5
    context = pi_string[start:end]
    print(f"...{context}...")
else:
    print(f"Your birthday ({birthday}) does not appear in the selected digits of pi.")

