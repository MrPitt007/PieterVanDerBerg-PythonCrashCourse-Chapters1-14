 Chapter 6/page108_list_inside_dictionary.py


 A dictionary that contains a list as one of its values


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

 Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      f"with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
