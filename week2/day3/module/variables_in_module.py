# Variables in modules:-
'''
The module can contain functions, but also variables of all types (arrays, dictionaries, objects etc).
'''

# Example:-

import person
# importing person module which have the following dictionary:-
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

age = person.person1["age"]
print(age)

# Output:- 36

