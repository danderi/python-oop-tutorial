# Create your Person class here

# Create your Person class here
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}")



person = Person("John")
person.greet()