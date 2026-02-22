
 Handled version with try/except (friendly message)

def safe_divide(a, b):
    """Return a/b, or print a friendly message if b == 0."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return None
    else:
        return result

print("=== ZeroDivisionError demo ===")
print("Dividing 5 by 0 (handled):")
value = safe_divide(5, 0)
print("Result:", value)

print("\nDividing 25 by 5 (handled):")
value = safe_divide(25, 5)
print("Result:", value)


