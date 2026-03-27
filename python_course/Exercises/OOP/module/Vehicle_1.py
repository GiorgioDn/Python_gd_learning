from .TransportVehicle import TransportVehicle

# child class of the abstract class TransportVehicle
class Truck(TransportVehicle):
    def __init__(self, license_plate: str, max_weight: int, axle_count: int, current_load: int = 0):
        super().__init__(license_plate, max_weight, current_load)
        self.axle_count = axle_count
        
    # implementation of the abstract method
    def maintenance_cost(self):
        cost = 100 * self.axle_count + 1 * self._max_weight
        return cost

# child class of the abstract class TransportVehicle
class Van(TransportVehicle):
    def __init__(self, license_plate: str, max_weight: int, fuel_type: str, current_load: int = 0):
        super().__init__(license_plate, max_weight, current_load)
        self.fuel_type = fuel_type
    
    # implementation of the abstract method
    def maintenance_cost(self):
        if self.fuel_type.lower() == "electric":
            cost = 200
        else:
            cost = 150
        return cost

# child class of the abstract class TransportVehicle
class MotorTricycle(TransportVehicle):
    def __init__(self, license_plate: str, max_weight: int, service_years: int, current_load: int = 0):
        super().__init__(license_plate, max_weight, current_load)
        self.service_years = service_years
    
    # implementation of the abstract method   
    def maintenance_cost(self):
        cost = 50 * self.service_years
        return cost