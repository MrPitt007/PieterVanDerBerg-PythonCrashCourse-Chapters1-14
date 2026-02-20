
def make_pizza_basic(*toppings):
    """Print the toppings requested for a pizza (arbitrary number)."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

 These calls produce working output whether 1 or many toppings:
make_pizza_basic('pepperoni')
make_pizza_basic('mushrooms', 'green peppers', 'extra cheese')



def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    The size argument is positional.
    The *toppings argument collects any remaining arguments.
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

Example calls (directly from page 147):
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


PAGE 147 SUMMARY

1) When mixing positional parameters and arbitrary positional parameters:
       def function(positional_param, *args)
   The positional parameter MUST come first.

2) Python assigns the first value in the function call to the
   positional parameter, then packs all remaining values into *args.

3) Example:
       make_pizza(16, 'pepperoni')
   → size = 16
   → toppings = ('pepperoni',)

4) *args lets a function accept one or many extra positional values.

This page completes the introduction to *args by showing how to
combine it with regular positional arguments cleanly.
"""
print(summary)
