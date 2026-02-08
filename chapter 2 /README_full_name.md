- ./full_name.py
- ./full_name_title.py
- ./full_name_message.py
- ./whitespace_demo.py
- ./strip_whitespace.py

# 2.1 — Names & f‑strings (Chapter 2)

This page contains my work for the **names + f‑strings** part of Chapter 2.

It covers:
- Variables for first/last name
- Building strings with **f‑strings**
- Formatting with **`.title()`**
- Storing a full **message** in a variable
- Whitespace basics: `\t` (tab) and `\n` (newline)
- Stripping whitespace: `rstrip()`, `lstrip()`, `strip()`

---

## 🔗 Files in this section (click to open)

- ./full_name.py
- ./full_name_title.py
- ./full_name_message.py
- ./whitespace_demo.py
- ./strip_whitespace.py

>  Run from your project root (Windows):
> ```bash
> python "Chapter 2\full_name.py"
> python "Chapter 2\full_name_title.py"
> python "Chapter 2\full_name_message.py"
> python "Chapter 2\whitespace_demo.py"
> python "Chapter 2\strip_whitespace.py"
> ```
> If `python` doesn’t work, try `py`.

---

##  Code previews

### `full_name.py`
```python
# full_name.py
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)  # ada lovelace

# full_name_title.py
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")  # Hello, Ada Lovelace!

# full_name_message.py
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)  # Hello, Ada Lovelace!

# whitespace_demo.py
print("Python")
print("\tPython")  # \t adds a tab before the word
print("Languages:\nPython\nC\nJavaScript")  # \n puts each on a new line

# strip_whitespace.py
name = "  ada lovelace  "

print(f"Raw: _{name}_")
print(f"rstrip: _{name.rstrip()}_")
print(f"lstrip: _{name.lstrip()}_")
print(f"strip: _{name.strip()}_")

clean = name.strip().title()
print(f"Cleaned + title: {clean}")
