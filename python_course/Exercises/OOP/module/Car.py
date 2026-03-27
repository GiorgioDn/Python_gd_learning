from .Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, ignition: bool, door_count: int):
        super().__init__(make, model, year, ignition)
        self.__door_count = door_count
    
    def get_door_count(self):
        if self.__door_count > 0:
            return self.__door_count
        else:
            return False
        
    def set_door_count(self, door_count: int):
        if door_count > 0:
            self.__door_count = door_count
        else:
            return False
        
    def honk_horn(self):
        return "BEEEEEP"