
Ensure small demo file exists: pi_digits.txt (3 lines; 10 decimals per line)

pi_small_path = Path("pi_digits.txt")
if not pi_small_path.exists():
    pi_small_path.write_text(
        "3.1415926535\n"
        " 8979323846\n"      # leading space on purpose (matches book’s left padding)
        " 2643383279\n",
        encoding="utf-8",
    )


 Build a single string (use lstrip to drop leading whitespace from each line)

contents = pi_small_path.read_text(encoding="utf-8")
lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.lstrip()   # remove left-padding spaces only

print("=== pi_string built from pi_digits.txt ===")
print(pi_string)
print("Length of pi_string:", len(pi_string))   # 32 for 30 decimals including '3.'


pi_million_path = Path("pi_million_digits.txt")

if pi_million_path.exists():
    contents_big = pi_million_path.read_text(encoding="utf-8")
    lines_big = contents_big.splitlines()

    pi_string_big = ""
    for line in lines_big:
        pi_string_big += line.lstrip()

    # Print only the first 52 characters: "3." + 50 decimal places
    print("\n=== First 50 decimals of pi (from pi_million_digits.txt) ===")
    print(f"{pi_string_big[:52]}...")
    print(f"Total length read: {len(pi_string_big)} characters")

else:
    print("\n[Note] 'pi_million_digits.txt' not found. "
          "Place it next to this script to run the large-file demo.")


