
 DEMO 1: What happens WITHOUT try/except (crash)
 (Shown on the page; commented so this file runs cleanly)


 path = Path('alice.txt')
 contents = path.read_text(encoding='utf-8')  
 This would raise:
 FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'



 DEMO 2: Handling FileNotFoundError properly

print("=== Handling FileNotFoundError ===")

path = Path("alice.txt")  # File intentionally does NOT exist

try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("Sorry, the file 'alice.txt' does not exist in this folder.")
else:
    # This only runs if no exception occurs
    print(contents[:200], "...")  # Preview the first 200 chars



