full_name_title.py
# full_name_title.py
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")  # Hello, Ada Lovelace!

full_name_message.py
# full_name_message.py
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)  # Hello, Ada Lovelace!

whitespace_demo.py
# whitespace_demo.py
print("Python")
print("\tPython")  # tab
print("Languages:\nPython\nC\nJavaScript")  # newlines

strip_whitespace.py

# strip_whitespace.py
name = "  ada lovelace  "
print(f"Raw: _{name}_")
print(f"rstrip: _{name.rstrip()}_")
print(f"lstrip: _{name.lstrip()}_")
print(f"strip: _{name.strip()}_")
print(f"Cleaned + title: {name.strip().title()}")







# Chapter 2 – Variables and Simple Data Types

This folder contains my completed examples and practice scripts for Chapter 2 of *Python Crash Course* (p. 21–22).

## ✔ Concepts practiced
- Building strings with **f-strings**: `f"{first} {last}"`
- Formatting names with **`.title()`**
- Storing a final **message** in a variable and printing it
- Adding **whitespace** with `\t` (tab) and `\n` (newline)
- Stripping whitespace with **`rstrip()`**, **`lstrip()`**, and **`strip()`**

---

## 🗂 Files in this folder

- `full_name.py` — prints a full name using an f-string  
- `full_name_title.py` — prints **Hello, Ada Lovelace!** using `.title()`  
- `full_name_message.py` — stores the greeting in `message` and prints it  
- `whitespace_demo.py` — shows `\t` (tab) and `\n` (newline)  
- `strip_whitespace.py` — demonstrates `rstrip()`, `lstrip()`, and `strip()`

> Run on Windows from the project root:
> ```bash
> python "Chapter 2\full_name.py"
> python "Chapter 2\full_name_title.py"
> python "Chapter 2\full_name_message.py"
> python "Chapter 2\whitespace_demo.py"
> python "Chapter 2\strip_whitespace.py"
> ```
> If `python` doesn’t work, try `py`.

---

## 🔎 Code previews

### `full_name.py`
```python
# full_name.py
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)  # ada lovelace


