'''
Delete Object Properties or Object:-
You can delete properties on objects or the whole object by using the del keyword.
'''

# Example:

class Person:  # created 'Person' class
  def __init__(self, name, number):
    self.name = name  # 'name' and 'number' are the attributes of the 'self' referring to the object created.
    self.number = number


person1 = Person("John",34)  # created object 'person1'
print(person1.name)  # Output:- John

del person1.name  # deleting object parameter
print(person1.name)  # OUtput:- AttributeError: 'Person' object has no attribute 'name'

del person1  # deleting object 'person1'
print(person1.number)  # Output:- NameError: name 'person1' is not defined. Did you mean: 'Person'?

