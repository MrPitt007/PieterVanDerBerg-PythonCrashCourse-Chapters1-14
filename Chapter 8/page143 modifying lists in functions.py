
Start with some designs that need to be printed:
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

Simulate printing each design until none are left.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

 Display completed models.
print("\nThe following models have been printed:")
for model in completed_models:
    print(model)

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, moving items from one list
    (unprinted_designs) to another (completed_models).
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Display all models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)


 Safe demo call:
unprinted = ['cube', 'pyramid', 'sphere']
completed = []

print_models(unprinted, completed)
show_completed_models(completed)



