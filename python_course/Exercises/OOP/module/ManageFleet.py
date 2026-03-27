from .TransportVehicle import TransportVehicle
from .Vehicle import *
from .Vehicle_1 import Truck, Van, MotorTricycle

# generic class to manipulate a list of TransportVehicle types
class FleetManager:
    def __init__(self, vehicles: list[TransportVehicle]):
        self.vehicles = vehicles
    
    def add_vehicle(self, vehicle: TransportVehicle):
        self.vehicles.append(vehicle)
        
    def remove_vehicle(self, license_plate: str):
        for vehicle in self.vehicles:
            if vehicle.get_license_plate() == license_plate:
                self.vehicles.remove(vehicle)
     
    # sums total costs by executing the maintenance_cost method present in the TransportVehicle class           
    def total_maintenance_cost(self):
        total_cost = 0
        for vehicle in self.vehicles:
            total_cost += vehicle.maintenance_cost()
            
        return total_cost
    
    # prints information based on the child class type of TransportVehicle
    def print_vehicles(self):
        for vehicle in self.vehicles:
            vehicle_type = type(vehicle).__name__
            if isinstance(vehicle, (Truck, Van, MotorTricycle)):
                print(f"Vehicle: {vehicle.get_license_plate()} - Type: {vehicle_type} - Current load: {vehicle.get_current_load()}")
            else:
                print(f"Vehicle: {vehicle.get_license_plate()} - Type: Unknown - Current load: {vehicle.get_current_load()}")