# base class
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a generic sound.")


# derived class (inherits from Animal)
class Dog(Animal):

# overwrite the method 
    def speak(self):
        print(f"{self.name} barks!")
        
generic_animal = Animal("GenericAnimal")
dog = Dog("Fido")

generic_animal.speak()
dog.speak()  

# multiple inheritance
# base classes
class Vehicle:
    def __init__(self, make, model):    
        self.make = make
        self.model = model

    def show_info(self):
        print(f"Vehicle make {self.make}, model {self.model}")


class SpecialEquipment:
    def __init__(self, equipment):
        self.equipment = equipment

    def show_equipment(self):
        print(f"Special equipment: {', '.join(self.equipment)}")

# class that inherits from both base classes       
class SportsCar(Vehicle, SpecialEquipment):

    def __init__(self, make, model, equipment, horsepower):
        Vehicle.__init__(self, make, model)  
        # alternative to super for multiple inheritance
        SpecialEquipment.__init__(self, equipment)
        self.horsepower = horsepower

    def show_info(self):
        super().show_info()  
        # call the method of the first superclass
        print(f"Power: {self.horsepower} HP")
        self.show_equipment()  

sports_car = SportsCar("Ferrari", "F8", ["ABS", "Traction Control", "Side Airbags"], 720)

sports_car.show_info()