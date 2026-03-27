from .Vehicle import Vehicle

class VehicleFleetManager():
    def __init__(self, vehicles: list[Vehicle] = []):
        self.__vehicles = vehicles
        
    def list_vehicles(self):
        if len(self.__vehicles) > 0:
            return self.__vehicles
        else:
            return False
        
    def add_vehicle(self, vehicle: Vehicle):
        self.__vehicles.append(vehicle)
    
    def remove_vehicle(self, make, model):
        for vehicle in self.__vehicles:
            if vehicle.get_make() == make and vehicle.get_model() == model:
                self.__vehicles.remove(vehicle)