
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, moving items from unprinted_designs
    into completed_models. This function modifies both lists.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Display each model that was printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)



unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

We send a COPY of the list using [:
This means print_models() empties the copy, not the original list.
print_models(unprinted_designs[:], completed_models)

show_completed_models(completed_models)

# Demonstration: original list remains unchanged
print("\nOriginal unprinted_designs list is still intact:")
print(unprinted_designs)    ['phone case', 'robot pendant', 'dodecahedron']

