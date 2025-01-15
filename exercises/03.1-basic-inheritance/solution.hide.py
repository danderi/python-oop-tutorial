class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def fetch(self):
        print(f"{self.name} is fetching the ball")

# Test code
if __name__ == "__main__":
    dog = Dog("Buddy", "Canine")
    dog.make_sound()
    dog.fetch()
