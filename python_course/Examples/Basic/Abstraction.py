from abc import ABC, abstractmethod

#abstract clasas
class Animal(ABC):
    #pass is optional
    #the abstract method must be overridden by the subclasses
    @abstractmethod
    def move(self):
        pass
    
class Dog(Animal):
    def move(self):
        print("I run")
    
class Fish(Animal):
    def move(self):
        print("I swim")

dog = Dog()
dog.move()

fish = Fish()
fish.move()

#abstract class with abstract method
class Form(ABC):
    @abstractmethod
    def area(self):
        pass 
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Form):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# f = Form() #TypeError because it can't be initialize 

r = Rectangle(5, 10)
print(r.area())
print(r.perimeter())
        