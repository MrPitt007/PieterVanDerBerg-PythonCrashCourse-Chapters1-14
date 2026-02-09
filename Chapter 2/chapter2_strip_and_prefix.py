# Chapter 2 - String Stripping and Prefix Removal
# Python Crash Course Exercises (Pages 22-23)
# Student: Pieter Van Der Berg

# --- Removing Whitespace ---

# Remove whitespace on the right side
favorite_language = 'python '
print("Original with right whitespace:", repr(favorite_language))
favorite_language = favorite_language.rstrip()
print("After rstrip():", favorite_language)

# Remove whitespace on the left side
favorite_language = ' python'
print("\nOriginal with left whitespace:", repr(favorite_language))
favorite_language = favorite_language.lstrip()
print("After lstrip():", favorite_language)

# Remove whitespace from both sides
favorite_language = ' python '
print("\nOriginal with both-side whitespace:", repr(favorite_language))
favorite_language = favorite_language.strip()
print("After strip():", favorite_language)

# --- Removing Prefixes ---
nostarch_url = 'https://nostarch.com'
clean_url = nostarch_url.removeprefix('https://')

print("\nOriginal URL:", nostarch_url)
print("After removeprefix('https://'):", clean_url)
