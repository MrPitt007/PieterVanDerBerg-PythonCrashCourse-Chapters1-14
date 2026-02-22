
 1) Demonstration: what happens WITHOUT try/except
    (Commented out so this script runs without crashing)

 path = Path('alice.txt')
 contents = path.read_text(encoding='utf-8')
 This would produce a long traceback like the one shown on page 196:

 FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'



 2) Proper handling: catch FileNotFoundError and keep running


path = Path("alice.txt")  # Intentionally missing file

print("=== Clean FileNotFoundError handling ===")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Runs only if file is successfully read
    print(contents[:200], "...\n")   # Preview first 200 chars



 Notes from the page: -
When a traceback appears, read from the BOTTOM line first to identify
   the exact exception type (here: FileNotFoundError). 
Then look at the FIRST file/line listed that belongs to YOUR code, not
the internal library files.
 That tells you which line to surround with try/except.



