# computer class with a private method
class Computer:
    # the processor attribute is private
    def __init__(self, proc_name):
        self.__processor = proc_name

    # access the attribute via the get method
    def get_processor(self):
        return self.__processor

    # modify the attribute via the set method
    def set_processor(self, processor):
        self.__processor = processor
    
    # private method 
    def __private_method(self):
        return "This is a private method"
    
    # public method to access the private method
    def public_method(self):
        return self.__private_method()


pc = Computer("Intel i5")
print(pc.get_processor()) 

# access the private attribute via the getter
pc.set_processor("AMD Ryzen 5") 

# modify the private attribute via the setter
print(pc.get_processor())

# to be avoided, also for security reasons
print(pc._Computer__processor)

print(pc.public_method())

print("\n")

# global variable
number = 10

def outer_function():
    # local variable in the outer function
    number = 5
    print("Number inside outer_function (local):", number)    

    def inner_function():
        # use nonlocal to modify the local variable of the outer function
        nonlocal number
        number = 3

        print("Number inside inner_function (nonlocal):", number)

    inner_function()

print("Number in main (global):", number)
outer_function()
print("Number in main after call (global unchanged):", number)

# class with protected variable
class BaseClass:
    def __init__(self):
        self._protected_variable = "I am protected"


class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        # the variable is inherited by the child class
        print(self._protected_variable)


obj = SubClass()
# to be avoided, also for security reasons
print(obj._protected_variable)