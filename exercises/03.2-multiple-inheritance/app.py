class Flying:
    def __init__(self):
        super().__init__()

    def fly(self):
        print("I can fly!")

class Swimming:
    def __init__(self):
        super().__init__()

    def swim(self):
        print("I can swim!")

class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        super().__init__()

class Duck(Bird, Swimming, Flying):
    def __init__(self, name, species):
        super().__init__(name, species)

    def introduce(self):
        print(f"I'm {self.name}, a {self.species} that can both fly and swim!")

duck = Duck("Donald", "Mallard")

duck.introduce()
duck.fly()
duck.swim()