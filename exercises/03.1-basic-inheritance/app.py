# Create your Animal and Dog classes here
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name, species):
      super().__init__(name, species)

    def make_sound(self):
        print("Woof!")

    def fetch(self):
        print(f'{self.name} is fetching the ball')

my_dog = Dog("Buddy", "Canine")

my_dog.make_sound()
my_dog.fetch()