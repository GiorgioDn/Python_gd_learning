from .module.Car import Car
from .module.Van import Van
from .module.Motorcycle import Motorcycle
from .module.ManageVehicle import VehicleParkManager

while True:
    
    vehicle_list = []
    
    print("Create your car by entering brand, model, year, number of doors")
    brand = input("Brand: ")
    model = input("Model: ")
    year = int(input("Year: "))
    num_doors = int(input("number of doors: "))
    
    auto = Car(brand, model, year, num_doors)
    
    vehicle_list.append([auto])
    
    print("Create your van by entering brand, model, year, load capacity")
    brand = input("Brand: ")
    model = input("Model: ")
    year = int(input("Year: "))
    load_capacity = int(input("load capacity: "))
    
    van = Van(brand, model, year, load_capacity)
    
    vehicle_list.append([van])
    
    print("Create your motorcycle by entering brand, model, year, type")
    brand = input("Brand: ")
    model = input("Model: ")
    year = int(input("Year: "))
    type = (input("Type: "))
    
    motorcycle = Motorcycle(brand, model, year, type)
    
    vehicle_list.append([motorcycle])
    
    park_manager = VehicleParkManager(vehicle_list)
    
    print(park_manager.vehicle_list())
    
    choice = int(input("Select: \n1. Add a vehicle\n2. Remove a vehicle\n"))
    
    match choice:
        case 1:
            pass
        case 2:
            pass
        case _:
            print("Invalid choice")
    
    choice = input("Do you want to perform a new test? ")
    
    if choice.lower() == "no":
        break