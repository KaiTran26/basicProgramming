'''
Define a Python class for a Rectangle.
The constructor should take parameters for the length and width of the rectangle.
Implement private attributes for these parameters.
Create methods to calculate the area and perimeter of the rectangle.

Instantiate more than one object from the class, and show suitable testing.  
'''

class Rectangle:
    def __init__(self, length : int, width : int):
        self._length = length
        self._width = width

    def find_perimeter(self) -> int:
        perimeter = (2 * self._length) + (2 * self._width)
        return perimeter

    def find_area(self):
        area = self._length * self._width
        return area

rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(10, 4)

print(rectangle1.find_area()) #prints 15
print(rectangle1.find_perimeter()) #prints 16

print(rectangle2.find_area()) #prints 40
print(rectangle2.find_perimeter()) #prints 28
