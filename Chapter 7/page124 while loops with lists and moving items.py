# Chapter 7/page124_while_loops_with_lists_and_moving_items.py

# -------------------------------------------------------------
# Using a while loop to move items from one list to another
# -------------------------------------------------------------

# Start with a list of users that need to be verified
unconfirmed_users = ['alice', 'brian', 'candace']

# Empty list to hold confirmed users
confirmed_users = []

# Verify each user until there are no more unconfirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # remove from end of list

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)  # add to confirmed list

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
