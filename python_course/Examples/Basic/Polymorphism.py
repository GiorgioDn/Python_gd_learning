# polymorphism with overriding
class Animal:

    def make_sound(self):
        print("This animal makes a sound")


class Dog(Animal):

    def make_sound(self):
        print("Woof")
    
    # used for passive polymorphism
    def speak(self):
        return "Woof!"


class Cat(Animal):

    def make_sound(self):
        print("Meow")
    
    # used for passive polymorphism
    def speak(self):
        return "Meow!"
        
animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()

        
# Simulating overloading
class Print:

    # optional or variadic arguments to simulate overloading
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print(a + b)

        elif a is not None:
            print(a)

        else:
            print("Nothing to show")
            
printer = Print()
printer.show()
printer.show(1)
printer.show(1, 2)

# Passive polymorphism: duck typing with a function that uses the polymorphic method
def make_speak(animal):
    print(animal.speak())

make_speak(dog) 
make_speak(cat) 

# duck typing with a polymorphic loop
class Circle:
    def draw(self):
        print("Drawing a circle")


class Rectangle:
    def draw(self):
        print("Drawing a rectangle")


def draw_shape(shape):
    # as long as draw exists
    shape.draw()


shapes = [Circle(), Rectangle()]

# iterate through each shape
for shape in shapes:
    draw_shape(shape)