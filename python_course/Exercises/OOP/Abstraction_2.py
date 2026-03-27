from .module.Vehicle_1 import *
from .module.ManageFleet import *

def main():
    
    vehicle_list = []
    
    manager = FleetManager(vehicle_list)
    
    truck = Truck("Df433k", 100, 4)
    
    print(truck.load(150))
    
    print(truck.get_current_load())
    
    truck.unload()
    
    print(truck.get_current_load())
    
    manager.add_vehicle(truck)
    
       
    van = Van("Se230po", 150, "diesel")
    
    print(van.load(50))
    
    print(van.get_current_load())
    
    van.unload()
    
    print(van.get_current_load())
    
    manager.add_vehicle(van)
    
    
    motor_tricycle = MotorTricycle("As700kk", 150, 10)
    
    print(motor_tricycle.load(50))
    
    print(motor_tricycle.get_current_load())
    
    motor_tricycle.unload()
    
    print(motor_tricycle.get_current_load())
    
    manager.add_vehicle(motor_tricycle)
    
    cost = manager.total_maintenance_cost()
    
    print(f"The total maintenance cost is: {cost}")
    
    print()
    
    manager.print_vehicles()
    
    print()
    
    manager.remove_vehicle("Se230po")
    
    manager.print_vehicles()
    
    
                
if __name__ == "__main__":
    main()
else: 
    print("Module imported")