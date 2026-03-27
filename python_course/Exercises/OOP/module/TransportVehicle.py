from abc import ABC, abstractmethod

# abstract class that takes a string and two integers as input
class TransportVehicle(ABC):
    # current_load has a default value of 0
    def __init__(self, license_plate: str, max_weight: int, current_load: int = 0):
        self._license_plate = license_plate
        self._max_weight = max_weight
        self._current_load = current_load
    
    # to be implemented in child classes
    @abstractmethod
    def maintenance_cost(self):
        pass
    
    # getter
    def get_license_plate(self):
        return self._license_plate
    
    # getter
    def get_max_weight(self):
        return self._max_weight
    
    # getter
    def get_current_load(self):
        return self._current_load
    
    # getter
    def set_license_plate(self, license_plate: str):
        self._license_plate = license_plate
    
    # setter
    def set_max_weight(self, max_weight: int):
        self._max_weight = max_weight

    # checks if it is possible to add the int value and then updates the current_load attribute
    def load(self, weight: int):
        if self._current_load + weight <= self._max_weight:
            self._current_load += weight
            return f"It has been loaded, the current load is: {self._current_load} kg out of {self._max_weight} kg maximum"
        else:
            return f"It cannot be inserted because it exceeds the maximum load of {self._max_weight} kg"
    
    # sets current_load to 0    
    def unload(self):
        self._current_load = 0