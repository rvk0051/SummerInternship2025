'''
Objects can also contain methods. Methods in objects are functions that belong to the object.
'''

#Example:
class Person:
  def __init__(self, name):
    self.name = name

  def welcome(self):  # 'welcome' is an object function
    print("Welcome, " + self.name)

person1 = Person("John")
person1.welcome()  # Output:- Welcome, John