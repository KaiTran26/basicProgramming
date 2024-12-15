'''
Implement a Python class for a Shape.
This class should have methods to calculate the area and perimeter of the shape.
Then, create subclasses for specific shapes like Rectangle, Circle, and Triangle.
Each subclass should override the methods to calculate the area and perimeter based on its specific formula.
'''
import math

class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width


    def find_perimeter(self):
        pass

    def find_area(self):
        pass
    
class Square(Shape):
    def __init__(self, height, width):
         super().__init__(height, width)

    def find_perimeter(self):
        return (2 * self.height) + (2 * self.width)

    def find_area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self, height, width, radius):
         super().__init__(height, width)
         self.radius = radius

    def find_perimeter(self):
        return 2 * math.pi * self.radius

    def find_area(self):
        return math.pi * self.radius ** 2
    
class Triangle(Shape):
    def __init__(self, height, width, side1, side2, side3):
        super().__init__(height, width)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def find_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def find_area(self):
        return self.height * self.width / 2
    

#I used chatgpt to write a test

def test_shapes():
    # Test Square
    square = Square(4, 4)
    print(f"Square (4, 4) -> Expected Area: 16, Calculated Area: {square.find_area()}")
    print(f"Square (4, 4) -> Expected Perimeter: 16, Calculated Perimeter: {square.find_perimeter()}")

    # Test Circle
    circle = Circle(0, 0, 3)
    expected_circle_area = math.pi * 3 ** 2
    expected_circle_perimeter = 2 * math.pi * 3
    print(f"Circle (radius 3) -> Expected Area: {expected_circle_area}, Calculated Area: {circle.find_area()}")
    print(f"Circle (radius 3) -> Expected Perimeter: {expected_circle_perimeter}, Calculated Perimeter: {circle.find_perimeter()}")

    # Test Triangle
    triangle = Triangle(6, 8, 3, 4, 5)
    print(f"Triangle (height 6, base 8, sides 3, 4, 5) -> Expected Area: 24, Calculated Area: {triangle.find_area()}")
    print(f"Triangle (height 6, base 8, sides 3, 4, 5) -> Expected Perimeter: 12, Calculated Perimeter: {triangle.find_perimeter()}")

# Run the tests
test_shapes()