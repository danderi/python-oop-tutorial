class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Test code
if __name__ == "__main__":
    person = Person("John")
    person.greet()
