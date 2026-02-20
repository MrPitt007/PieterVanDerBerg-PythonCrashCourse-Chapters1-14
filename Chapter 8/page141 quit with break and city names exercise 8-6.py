
def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


 while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

   f_name = input("First name: ")
    if f_name == 'q':
         break

     l_name = input("Last name: ")
    if l_name == 'q':
         break

      print(f"\nHello, {formatted_name}!")

 Example output shown in the book:
   Please tell me your name:
  (enter 'q' at any time to quit)
   First name: eric
  Last name: matthes
   Hello, Eric Matthes!
   ...
   First name: q  -> loop stops


