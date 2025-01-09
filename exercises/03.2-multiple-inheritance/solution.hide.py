class Flying:
    def fly(self):
        print("I can fly!")

class Swimming:
    def swim(self):
        print("I can swim!")

class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Duck(Bird, Flying, Swimming):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def introduce(self):
        print(f"I'm {self.name}, a {self.species} that can both fly and swim!")

# Test code
if __name__ == "__main__":
    duck = Duck("Donald", "Mallard")
    duck.introduce()
    duck.fly()
    duck.swim()
