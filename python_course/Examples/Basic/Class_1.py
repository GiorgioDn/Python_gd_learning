#declare of the class Car
class Car:
    #class attribute
    number_of_wheels = 4
    #constructor method
    def __init__(self, brand, model):
        #instance attributes
        self.brand = brand
        self.model = model
    #special method
    def __str__(self):
        #It is used in the class's print statement
        return f"Car brand = {self.brand}, model = {self.model}"
    #instance method
    def print_info(self):
        print("The car is a ", self.brand, self.model)
        
#creation of two objects of type Car
car1 = Car("Fiat", "500")    
car2 = Car("BMW", "X3")

#instance method call
car1.print_info()            
car2.print_info()

#print the memory address or the special __str__ method, if defined
print(car1)

#declare of the class Person
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #method
    def hello(self):
        print(f"Hello my name is {self.name}")
    
#creation of object of type Car
p = Person("Pippo", 30)

#Print the single instance attributes associated with the object
print(p.name)
print(p.age)
#use the method
p.hello()

#class with static method
class Calculator:
    
    #static method
    @staticmethod
    def sum(a, b):
        return a + b


#static method without instance
result = Calculator.sum(5, 3)

print(result)

#class using the class method
class Counter: 
    #class attribute
    number_instance = 0
    
    def __init__(self):
        Counter.number_instance += 1

    #class method: cls refers to the class
    @classmethod
    def show_number_instance(cls):
        print(f"{cls.number_instance} instances have been created.")

#creation of two class instances
c1 = Counter()
c2 = Counter()

Counter.show_number_instance()