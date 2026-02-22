
 Build one string containing all lines (each ends with '\n')

contents = ""
contents += "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

Write the multi-line string to a text file
Note: write_text() creates the file if missing, and OVERWRITES if it exists.

path = Path("programming.txt")
path.write_text(contents, encoding="utf-8")

 Quick verification: read back and print to terminal
print("=== programming.txt (after write) ===")
print(path.read_text(encoding="utf-8"), end="")

 To write multiple lines with pathlib, build one string containing all lines:
      contents  = "line 1\\n"
      contents += "line 2\\n"
      contents += "line 3\\n"

 Then write it in one call:
      from pathlib import Path
      Path('programming.txt').write_text(contents)

 'write_text()' creates the file if it doesn't exist and OVERWRITES it if it does.
 If you need to *append* instead of overwrite, you'll use file modes with open()
  (coming up next in the chapter).

print(summary)
