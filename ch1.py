'''
Create a Class for a dog in python.
Implement private attributes using the _attribute approach in python.
When a dog is instantiated the constructor takes in two parameters, the name and colour.
These are the only attributes within the dog class.
Also create a method that will take in a parameter integer and then output "Woof!" the number of times the value of the parameter. 
Create the necessary getter and setter methods for the object.
Instantiate a new instance of a dog, output its name and colour in a single message e.g. Hello Fido, you are a Brown colour. 

Make the dog woof 10 times. 
output the memory location of the Dog object you have instantiated. 
'''

class Dog:
    
    #Create private attributes when Dog object is initialised
    def __init__(self, name, colour):
        self._name = name
        self._colour = colour

    #Getter for the name
    def get_name(self):
        return self._name

    #Setter for the name
    def set_name(self, name):
        self._name = name

    #Getter for the colour
    def get_colour(self):
        return self._colour
    
    #Setter for the colour
    def set_colour(self, colour):
        self._colour = colour

    #Method to make the dog woof the inputted number of times
    def bark(self, number):
        for i in range(0, number):
            print("Woof!")


name = "Fido"
colour = "Brown"

#Initialise dog instance
dog = Dog(name, colour)

print(f"Hello {dog.get_name()}, you are a {dog.get_colour()} colour.")

dog.bark(10)

#print dog memory location
print(id(dog))
