class Dog:
    def __init__(self, name, color):
        # Private attributes for name and color
        self._name = name
        self._color = color

    # Getter for the name
    def get_name(self):
        return self._name

    # Setter for the name
    def set_name(self, name):
        self._name = name

    # Getter for the color
    def get_color(self):
        return self._color

    # Setter for the color
    def set_color(self, color):
        self._color = color

    # Method to make the dog woof a specified number of times
    def woof(self, times):
        print("Woof! " * times)

    # Method to display the dog's information
    def display_info(self):
        print(f"Hello {self._name}, you are a {self._color} color.")

# Instantiate a Dog object
my_dog = Dog("Fido", "Brown")

# Output the dog's name and color
my_dog.display_info()

# Make the dog woof 10 times
my_dog.woof(10)

# Output the memory location of the dog object
print(f"The memory location of the Dog object is: {hex(id(my_dog))}")
