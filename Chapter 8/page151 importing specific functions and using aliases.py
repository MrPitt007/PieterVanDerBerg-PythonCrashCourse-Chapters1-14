
def make_pizza(size, *toppings):
    """Simplified local demo version used to simulate an import."""
    print(f"\nMaking a {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")

 Simulate this call:
  from pizza import make_pizza
print("\nSimulated: imported make_pizza() directly:")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def make_pizza_original(size, *toppings):
    """Another demo function to show alias usage."""
    print(f"\n[ALIAS DEMO] A {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")

 Simulate:
  from pizza import make_pizza as mp
mp = make_pizza_original

print("\nSimulated: imported make_pizza_original as mp:")
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


PAGE 151 SUMMARY

1) Instead of importing the whole module, you can import specific functions:
       from pizza import make_pizza
   Then call it directly without module_name.

2) You can import multiple functions by separating them with commas.

3) Aliases let you rename imported functions:
       from pizza import make_pizza as mp
   Use mp(...) throughout the file to avoid naming conflicts or to shorten long names.

4) Benefits:
   • Cleaner code
   • Avoids overwriting existing function names in your program
   • Makes frequently called functions easier to reference
"""
print(summary)
