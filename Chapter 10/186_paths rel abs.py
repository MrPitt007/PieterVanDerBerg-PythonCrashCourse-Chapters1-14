
 Setup: make a folder and sample file

base_dir = Path("text_files")
base_dir.mkdir(exist_ok=True)

sample_file = base_dir / "filename.txt"
if not sample_file.exists():
    sample_file.write_text(
        "Line A\nLine B\nLine C\n",
        encoding="utf-8"
    )


 Relative path (as shown on the page)
 Path looks relative to the current working directory.

print("=== RELATIVE PATH READ ===")
rel_path = Path("text_files/filename.txt")   # relative path
contents_rel = rel_path.read_text(encoding="utf-8")
print(contents_rel, end="")


 Absolute path (full location from the filesystem root)
 Use resolve() to get a portable absolute path to an existing file.

print("\n=== ABSOLUTE PATH READ ===")
abs_path = rel_path.resolve()                 # absolute path to the same file
print("Absolute path is:", abs_path)
contents_abs = abs_path.read_text(encoding="utf-8")
print(contents_abs, end="")


Notes on separators (Windows vs macOS/Linux):
 Windows traditionally shows backslashes (e.g., C:\folder\file.txt)
#pathlib accepts forward slashes in your code and will translate as needed.
Always build paths with Path(...) or the / operator to stay portable.

