 Ensure demo file exists (same 3-line sample used earlier)

path = Path("pi_digits.txt")
if not path.exists():
    path.write_text(
        "3.1415926535\n"
        "8979323846\n"
        "2643383279\n",
        encoding="utf-8",
    )


# 1) Read entire file text, then split into lines for per-line processing

contents = path.read_text(encoding="utf-8")
lines = contents.splitlines()   # returns a list of lines without trailing '\n'

print("=== LINES (splitlines + simple loop) ===")
for line in lines:
    print(line)                 # prints exactly like the original text


 Build a single string of digits (remove all whitespace)
 Start with an empty string and append each line.

pi_string = ""
for line in lines:
    pi_string += line  # no extra spaces or newlines

print("\n=== SINGLE STRING (no whitespace) ===")
print(pi_string)
print("Length of pi_string:", len(pi_string))

 Optional sanity check: show first 10 chars
print("First 10 chars:", pi_string[:10])
