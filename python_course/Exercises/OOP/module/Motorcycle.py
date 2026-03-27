from .Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, ignition: bool, vehicle_type: str):
        super().__init__(make, model, year, ignition)
        self.__vehicle_type = vehicle_type
    
    def get_vehicle_type(self):
        if len(self.__vehicle_type) > 0:
            return self.__vehicle_type
        else:
            return False
        
    def set_vehicle_type(self, vehicle_type: str):
        if len(vehicle_type) > 0:
            self.__vehicle_type = vehicle_type
        else:
            return False
    
    def perform_wheelie(self):
        if self.__vehicle_type == "sport":
            return "Performing a wheelie"
        else:
            return "Cannot perform a wheelie"
        
