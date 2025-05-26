'''

The __str__() Function:-

The __str__() function controls what should be returned when the class object is represented as a string.
If the __str__() function is not set, the string representation of the object is returned.

'''

# Example without __str__ function:-

class Person:  # defining a class 'Person'
  def __init__(self, name):
    self.name = name

person1 = Person("John")  # created object 'person1' of class 'Person'

print(person1)  # Output: <__main__.Person object at 0x000001A1CEF48D70>


# Example with __str__ function:-
class Person:  # redefining class 'Person'
  def __init__(self, name):
    self.name = name

  def __str__(self):  # defining __str__ function
      return f"{self.name}"

person2 = Person("John")  # created object 'person2'
print(person2)  # output: John