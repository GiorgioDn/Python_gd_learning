class Person:
    # takes a string and an integer as input
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
    
    # use getters to access the corresponding parameters
    def get_name(self):
        if len(self.__name) > 0:
            return self.__name
        else:
            return False
    
    def get_age(self):
        if self.__age > 0:
            return self.__age
        else:
            return False
    
    # use setters to modify the parameters
    def set_name(self, name: str):
        if len(name) > 0:
            self.__name = name
        else:
            return False
    
    def set_age(self, age: int):
        if age > 0:
            self.__age = age
        else:
            return False
    
    # introduction method
    def introduction(self):
        return f"{self.__name} is {self.__age} years old"