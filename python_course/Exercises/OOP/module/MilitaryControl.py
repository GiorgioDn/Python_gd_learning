from .Unit import *

class MilitaryControl(Infantry, Artillery, Cavalry, LogisticSupport, Reconnaissance):
    # takes all parameters from parent classes plus a new one
    def __init__(self, name, soldier_count, weapons, range_dist, speed, material_quantity, mission_duration, registered_units):
        super().__init__(name, soldier_count, weapons)
        Artillery.__init__(self, name, soldier_count, range_dist)
        Cavalry.__init__(self, name, soldier_count, speed)
        LogisticSupport.__init__(self, name, soldier_count, material_quantity)
        Reconnaissance.__init__(self, name, soldier_count, mission_duration)
        self.registered_units = registered_units
        
    # registers the unit by appending it to the list
    def register_unit(self, unit):
        return self.registered_units.append(unit)
    
    def show_units(self):
        return self.registered_units
    
    # iterates the list to find the unit by name
    def unit_details(self, name):
        for specific_unit in self.registered_units:
            if specific_unit.name == name:
                return specific_unit