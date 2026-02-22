
import json


 Data to store

numbers = [2, 3, 5, 7, 11, 13]


# Serialize to JSON text and write to a file

path = Path("numbers.json")
contents = json.dumps(numbers)             # convert Python list -> JSON string

# Write JSON string to disk (UTF-8)
path.write_text(contents, encoding="utf-8")

print("Wrote JSON to:", path)
print("Raw JSON text:")
print(contents)                            # e.g., [2, 3, 5, 7, 11, 13]


 (Convenience) Read back and parse to confirm round-trip
 (The book covers loading on the next page, but we preview it here.)

json_text = path.read_text(encoding="utf-8")
loaded = json.loads(json_text)             # convert JSON string -> Python object

print("\nLoaded back from JSON (Python type):", type(loaded).__name__)
print("Loaded list:", loaded)

