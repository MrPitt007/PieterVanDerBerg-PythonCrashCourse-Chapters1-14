
def make_pizza(*toppings):
    """
    Print the list of toppings that have been requested.
    The asterisk in *toppings packs all extra positional arguments
    into a tuple named 'toppings'.
    """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

Examples mirroring the page:
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')



def show_messages(messages):
    """Print each message in the list."""
    for msg in messages:
        print(msg)

messages = [
    "Hello there!",
    "Functions are powerful.",
    "Keep practicing every day."
]
print("\n8-9 — Show messages:")
show_messages(messages)


def send_messages(messages, sent_messages):
    """
    Pop messages from 'messages' (source) one by one,
    print each as it's sent, and append to 'sent_messages' (destination).
    This function MODIFIES both lists.
    """
    while messages:
        current = messages.pop(0)  # send in original order
        print(f"Sending: {current}")
        sent_messages.append(current)

# Demo for 8-10 (modifies the original 'messages' list)
messages_8_10 = [
    "Remember to commit your code.",
    "Use docstrings for clarity.",
    "Write small, focused functions."
]
sent_messages = []

print("\n8-10 — Send messages (modifies original list):")
send_messages(messages_8_10, sent_messages)

print("messages_8_10 (should be empty):", messages_8_10)
print("sent_messages:", sent_messages)

messages_archive_src = [
    "Pack *args into tuples.",
    "Consider **kwargs for named options.",
    "Prefer clarity over cleverness."
]
archived_sent = []

print("\n8-11 — Send messages using a COPY to preserve the original:")
send_messages(messages_archive_src[:], archived_sent)  # pass a copy

print("Original messages_archive_src (should be intact):", messages_archive_src)
print("archived_sent:", archived_sent)


PAGE 146 SUMMARY

1) Arbitrary positional arguments:
     def make_pizza(*toppings):
         ...
   - The * packs extra positional args into a tuple 'toppings'.
   - Supports one or many values with the same function.

2) Exercises 8-9 to 8-11 reinforce:
   - Looping through a list to print messages (8-9).
   - Moving items between lists (source -> destination) (8-10).
   - Preserving the original list by passing a copy using [:] (8-11).

3) Patterns to remember:
   - Use *args when a function should accept an open-ended list of values.
   - When functions should not alter caller data, pass a copy: some_list[:]
"""
print(summary)
