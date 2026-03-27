from .module.Animal import *

# Lion class child of Animal class
class Lion(Animal):
    # create initial attributes with additions
    def __init__(self, name, age:int, gender):
        super().__init__(name, age)
        self.gender = gender
        
    # define custom string representation
    def __str__(self):
        return f"The lion {self.name}, is {self.age} years old and is {self.gender}"
        
    # override Animal class method make_sound
    def make_sound(self):
        print("ROAR!")
    
    # class method
    def hunt(self, prey):
        print(f"The lion is hunting a {prey}")

# Giraffe class child of Animal class
class Giraffe(Animal):
    # create initial attributes with additions
    def __init__(self, name, age:int, gender, height:int):
        super().__init__(name, age)
        self.gender = gender
        self.height = height
        
    # define custom string representation
    def __str__(self):
        return f"The giraffe {self.name}, is {self.age} years old, is {self.gender} and reaches a height of {self.height} meters"
    
    # override Animal class method make_sound
    def make_sound(self):
        print("Bleat")
        
    # class method   
    def eat(self, tree):
        print(f"The giraffe is eating leaves from a {tree}")

# Penguin class child of Animal class
class Penguin(Animal):
    # create initial attributes with additions
    def __init__(self, name, age:int, gender):
        super().__init__(name, age)
        self.gender = gender
        
    # define custom string representation
    def __str__(self):
        return f"The penguin {self.name}, is {self.age} years old and is {self.gender}"
    
    # override Animal class method make_sound
    def make_sound(self):
        print("Honk")
    
    # class method   
    def swim(self):
        print("The penguin is swimming")
 
#TEST       
lion = Lion("Leon", 4, "male")

print(lion)

lion.make_sound()

lion.hunt("deer")

giraffe = Giraffe("Gir", 7, "female", 5)

print(giraffe)

giraffe.make_sound()

giraffe.eat("acacia")

penguin = Penguin("Pingu", 2, "male")

print(penguin)

penguin.make_sound()

penguin.swim()
