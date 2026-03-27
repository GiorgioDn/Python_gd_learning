# creating the animal superclass
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Animal sound")