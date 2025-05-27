'''
Polymorphism in Object Oriented Programming:-

In OOP, polymorphism allows methods in different classes to share the same name but perform distinct tasks.
This is achieved through inheritance and interface design.

'''

#Example:-
class Shape:  # Shape is the parent class
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):   # overriding the function 'area()' of parent class
        return self.length * self.width

class Circle(Shape):  # overriding the function 'area()' of parent class
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(2, 3), Circle(5)]
# created list of objects,
# so now we can access those using the list.

for shape in shapes:
    print(f"Area: {shape.area()}")  # 'area()' function is called by the list

#Output:
# Area: 6     # Area of rectangle
# Area: 78.5  # Area of circle