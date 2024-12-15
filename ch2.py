'''
Develop a Python class for a Student.
The constructor should take parameters for the student's name, ID, and university major. 
Implement private attributes for these parameters. 
Create methods to get and set the student's major, as well as to display the student's information. 

Instantiate more than one object from the class, and show suitable testing.  
'''
class Student:

    #Instantiates objects
    def __init__(self, name, ID, major):
        self._name = name
        self._ID = ID
        self._major = major
    
    def get_major(self):
        return self._major
    
    def set_major(self, major):
        self._major = major
    
    #Creates method to print student info
    def display_student_info(self):
        print(f"Name: {self._name}\nID: {self._ID}\nMajor: {self._major}")
    
    
student = Student("Bob", 123, "Computer Science")
student.display_student_info() #prints properly