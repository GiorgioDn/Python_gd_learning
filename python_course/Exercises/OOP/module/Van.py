from .Vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, make: str, model: str, year: int, ignition: bool, load_capacity: int):
        super().__init__(make, model, year, ignition)
        self.__load_capacity = load_capacity
    
    def get_load_capacity(self):
        if self.__load_capacity > 0:
            return self.__load_capacity
        else:
            return False
        
    def set_load_capacity(self, load_capacity: int):
        if self.__load_capacity > 0:
            self.__load_capacity = load_capacity
        else:
            return False
    
    def load(self, quantity):
        if self.__load_capacity >= quantity:
            self.__load_capacity -= quantity
        else:
            return "Insufficient capacity"
    
    def unload(self, quantity):
        if self.__load_capacity <= quantity:
            self.__load_capacity += quantity
        else:
            return "Insufficient quantity"