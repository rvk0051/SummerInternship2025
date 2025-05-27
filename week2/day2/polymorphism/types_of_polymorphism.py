'''
Compile-time Polymorphism:-
Found in statically typed languages like Java or C++,
 where the behavior of a function or operator is resolved during the program's compilation phase.
Examples include method overloading and operator overloading,
where multiple functions or operators can share the same name but perform different tasks based on the context.
In Python, which is dynamically typed, compile-time polymorphism is not natively supported.
Instead, Python uses techniques like dynamic typing and duck typing to achieve similar flexibility.


Runtime Polymorphism:-
Occurs when the behavior of a method is determined at runtime based on the type of the object.
In Python, this is achieved through method overriding:
a child class can redefine a method from its parent class to provide its own specific implementation.
Python's dynamic nature allows it to excel at runtime polymorphism, enabling flexible and adaptable code.

'''

# Example:-
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())  # calls the overridden function based on the type of the object function.

#Output:-
# Bark
# Meow
# Some generic sound