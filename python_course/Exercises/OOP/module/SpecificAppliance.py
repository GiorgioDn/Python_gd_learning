from .Appliance import Appliance

class WashingMachine(Appliance):
    # takes two strings, an int, a string, and two ints as input
    def __init__(self, make: str, model: str, purchase_year: int, fault: str, capacity_kg: int, spin_speed: int):
        super().__init__(make, model, purchase_year, fault)
        self.__capacity_kg = capacity_kg
        self.__spin_speed = spin_speed

    # getter
    def get_capacity_kg(self):
        return self.__capacity_kg

    def set_capacity_kg(self, value: int):
        self.__capacity_kg = value

    # getter
    def get_spin_speed(self):
        return self.__spin_speed

    def set_spin_speed(self, value: int):
        self.__spin_speed = value
    
    # override of the base cost estimation method 
    def estimate_base_cost(self):
        est_cost = super().estimate_base_cost
        if self.__capacity_kg >= 20:
            est_cost += 5.0
            return est_cost
        else:
            return est_cost


class Refrigerator(Appliance):
    # takes two strings, an int, a string, an int, and a boolean as input
    def __init__(self, make: str, model: str, purchase_year: int, fault: str, liters: int, has_freezer: bool):
        super().__init__(make, model, purchase_year, fault)
        self.__liters = liters
        self.__has_freezer = has_freezer

    # getter
    def get_liters(self):
        return self.__liters

    def set_liters(self, value: int):
        self.__liters = value

    # getter
    def get_has_freezer(self):
        return self.__has_freezer

    def set_has_freezer(self, value: bool):
        self.__has_freezer = value
       
    # override of the base cost estimation method  
    def estimate_base_cost(self):
        est_cost = super().estimate_base_cost
        if self.__has_freezer == True or self.__liters > 5:
            est_cost += 2.0
            return est_cost
        
        elif self.__has_freezer == True and self.__liters > 5:
            est_cost += 6.5
            return est_cost
            
        else:
            return est_cost


class Oven(Appliance):
    # takes two strings, an int, two strings, and a boolean as input
    def __init__(self, make: str, model: str, purchase_year: int, fault: str, fuel_type: str, has_fan: bool):
        super().__init__(make, model, purchase_year, fault)
        self.__fuel_type = fuel_type
        self.__has_fan = has_fan

    # getter
    def get_fuel_type(self):
        return self.__fuel_type

    def set_fuel_type(self, value: str):
        self.__fuel_type = value

    # getter
    def get_has_fan(self):
        return self.__has_fan

    def set_has_fan(self, value: bool):
        self.__has_fan = value

    # override of the base cost estimation method  
    def estimate_base_cost(self):
        est_cost = super().estimate_base_cost
        if self.__has_fan == True or self.__fuel_type.lower() == "electric" or self.__fuel_type.lower() == "gas":
            est_cost += 2.5
            return est_cost
        
        elif self.__has_fan == True and self.__fuel_type.lower() == "electric" or self.__fuel_type.lower() == "gas":
            est_cost += 5.5
            return est_cost
            
        else:
            return est_cost