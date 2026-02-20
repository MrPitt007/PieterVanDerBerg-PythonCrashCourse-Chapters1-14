
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make (local simulation)."""
    print(f"\n[LOCAL DEMO] Making a {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")

 Simulated calls as if they were pizza.make_pizza(...)
print("\nSimulated imported module usage:")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


modules_explained = """
When Python runs:


