

def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.

    Required parameters:
        first : first name (string)
        last  : last name (string)

    Arbitrary keyword arguments (**user_info):
         Collect any number of additional named fields (key=value)
         Stored in the dict 'user_info'

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


 Example call shown on the page:
user_profile = build_profile(
    'albert', 'einstein',
    location='princeton',
    field='physics'
)
print(user_profile)
 Expected (order may vary by Python version):
 {'location': 'princeton', 'field': 'physics',
  'first_name': 'albert', 'last_name': 'einstein'}



scientist = build_profile(
    'marie', 'curie',
    location='paris',
    field='chemistry',
    awards=2
)
print(scientist)

developer = build_profile(
    'ada', 'lovelace',
    occupation='mathematician',
    known_for='analytical engine notes'
)
print(developer)


PAGE 148 SUMMARY

1) Use **kwargs (arbitrary keyword arguments) when a function should
   accept any number of named parameters:

       def build_profile(first, last, **user_info):
           ...
