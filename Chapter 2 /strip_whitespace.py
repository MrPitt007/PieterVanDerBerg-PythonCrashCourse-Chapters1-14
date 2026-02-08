# strip_whitespace.py
name = "  ada lovelace  "
print(f"Raw: _{name}_")
print(f"rstrip: _{name.rstrip()}_")
print(f"lstrip: _{name.lstrip()}_")
print(f"strip: _{name.strip()}_")
clean = name.strip().title()
print(f"Cleaned + title: {clean}")
