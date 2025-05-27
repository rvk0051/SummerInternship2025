'''
Adding __init__ function in child class:-

If the child class does not define its own __init__() method, it will automatically inherit the one from the parent class.
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
'''

class Person:  # Creating a class 'Person', with 'name' attribute, and a 'print_name' method
  def __init__(self, name):
    self.name = name

  def print_name(self):
    print(f"Hello, {self.name}")

class Student(Person):  #Creating a class 'Student', which inherits the 'Person' class
  def __init__(self, name, number):
    self.name = name
    self.number = number  # 'number is the property of 'Student' not 'Person'.


# Creating an instance of 'Student'
student1 = Student("Ram",46)
# '__init__' function of 'Student' overrides the inherited '__init__' function of 'Person

print(student1.number)  # Output: 46

student1.print_name()   # Output: Hello, Ram