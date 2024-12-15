'''
Create a Class for a dog in python. 
Implement private attributes using the _attribute approach in python. 
When a dog is instantiated the constructor takes in two parameters, the name and colour. 
These are the only attributes within the dog class.

Also create a method that will take in a parameter integer and then output "Woof!" the number of times the value of the parameter. 

Create the necessary getter and setter methods for the object. 

Instantiate a new instance of a dog. 
    output its name and colour in a single message e.g. Hello Fido, you are a Brown colour. 

Create new class of Puppy that inherits from Dog ( you can use your code for the above from the previous task if you wish) 

The puppy should have a new attribute ShoesChewed that is set to 0 when a puppy is instantiated. 
It should inherit all other Dog attributes. 

Use polymorphism to change the method for Bark so that the puppy Yaps instead of Woofs. 
Also create new method called chewShoe that takes in a number parameter that then increases the number of shoesChewed for that puppy accordingly. 

Ensure you also create any new necessary getter and setter methods for the puppy class. (taking into consideration what has already been inherited)
'''

class Dog:
    def __init__(self, name, colour):
        self._name = name
        self._colour = colour

    def get_name(self):
        print(self._name)
    def set_name(self, name):
        self._name = name

    def get_colour(self):
        print(self._colour)
    def set_colour(self, colour):
        self._colour = colour


    def make_noise(self, times):
        for i in range(times):
            print("Woof!")


class puppy(Dog):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.ShoesChewed = 0

    def get_ShoesChewed(self):
        print(self.ShoesChewed)

    def chewShoes(self, amount):
        self.ShoesChewed += amount


    def make_noise(self, times):
        for i in range(times):
            print("Yap!")


# Test cases for Dog and Puppy classes

def test_dog_and_puppy():
    # Create a Dog instance
    my_dog = Dog("Buddy", "Brown")
    
    # Test Dog getters
    print("Testing Dog getters:")
    print("Expected Name: Buddy")
    my_dog.get_name()  # Should print "Buddy"
    
    print("Expected Colour: Brown")
    my_dog.get_colour()  # Should print "Brown"
    
    # Test Dog setters
    print("\nTesting Dog setters:")
    my_dog.set_name("Max")
    my_dog.set_colour("Black")
    
    print("Expected Name after set: Max")
    my_dog.get_name()  # Should print "Max"
    
    print("Expected Colour after set: Black")
    my_dog.get_colour()  # Should print "Black"
    
    # Test Dog make_noise method
    print("\nTesting Dog make_noise:")
    print("Expected noise: Woof! Woof! Woof!")
    my_dog.make_noise(3)  # Should print "Woof!" three times
    
    # Create a Puppy instance
    my_puppy = puppy("Tiny", "Golden")
    
    # Test Puppy getters
    print("\nTesting Puppy getters:")
    print("Expected Name: Tiny")
    my_puppy.get_name()  # Should print "Tiny"
    
    print("Expected Colour: Golden")
    my_puppy.get_colour()  # Should print "Golden"
    
    # Test Puppy chewShoes method and ShoesChewed tracking
    print("\nTesting Puppy chewShoes and ShoesChewed attribute:")
    print("Initial shoes chewed: 0")
    my_puppy.get_ShoesChewed()  # Should print 0
    
    print("Expected shoes chewed after chewing 5 shoes: 5")
    my_puppy.chewShoes(5)
    my_puppy.get_ShoesChewed()  # Should print 5
    
    print("Expected shoes chewed after chewing 2 more shoes: 7")
    my_puppy.chewShoes(2)
    my_puppy.get_ShoesChewed()  # Should print 7
    
    # Test Puppy make_noise method (polymorphism)
    print("\nTesting Puppy make_noise (polymorphism):")
    print("Expected noise: Yap! Yap! Yap!")
    my_puppy.make_noise(3)  # Should print "Yap!" three times

# Run the test
test_dog_and_puppy()