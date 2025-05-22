# Arbitrary Keyword Argument
# Used when we do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly.

# Example:-
def child_details(**kid): # Here, 'kid' is a tuple.
  print("His last name is " + kid["last_name"])

child_details(first_name = "Mohan", last_name = "Gupta")

# If the number of keyword arguments is unknown, add a double ** before the parameter name.

# Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentations.