class Vehicle:
    def __init__(self, make: str, model: str, year: int, ignition: bool = False):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__ignition = ignition
    
    # getter methods to retrieve values
    def get_make(self):
        if len(self.__make) > 0:
            return self.__make
        else:
            return False
        
    def get_model(self):
        if len(self.__model) > 0:
            return self.__model
        else:
            return False
    
    def get_year(self):
        if self.__year > 0:
            return self.__year
        else:
            return False
        
    def get_ignition(self):
        return self.__ignition
    
    # setter methods to modify values
    def set_make(self, make: str):
        if len(self.__make) > 0:
            self.__make = make
        else:
            return False
        
    def set_model(self, model: str):
        if len(self.__model) > 0:
            self.__model = model
        else:
            return False
    
    def set_year(self, year: int):
        if self.__year > 0:
            self.__year = year
        else:
            return False
        
    # methods for ignition on and off
    def turn_on(self):
        self.__ignition = True
        
    def turn_off(self):
        self.__ignition = False