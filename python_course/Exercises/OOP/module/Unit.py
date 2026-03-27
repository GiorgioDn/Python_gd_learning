from .MilitaryUnit import MilitaryUnit

class Infantry(MilitaryUnit):
    # adds new non-inherited attributes
    def __init__(self, name, soldier_count, weapons: str):
        super().__init__(name, soldier_count)
        self.weapons = weapons
    
    # class method
    def build_trench(self, materials):
        print(f"Built a trench with {materials}")

class Artillery(MilitaryUnit):
    # adds new non-inherited attributes
    def __init__(self, name, soldier_count, range_dist: int):
        super().__init__(name, soldier_count)
        self.range_dist = range_dist
    
    # class method
    def calibrate_artillery(self, calibrate: int):
        if calibrate < self.range_dist:
            print("Calibration completed to hit the target")
        else:
            print("Target too distant")

class Cavalry(MilitaryUnit):
    # adds new non-inherited attributes
    def __init__(self, name, soldier_count, speed: int):
        super().__init__(name, soldier_count)
        self.speed = speed
    
    # class method
    def explore_terrain(self, area):
        print(f"The units explored {area} finding information")

class LogisticSupport(MilitaryUnit):
    # adds new non-inherited attributes
    def __init__(self, name, soldier_count, material_quantity: int):
        super().__init__(name, soldier_count)
        self.material_quantity = material_quantity
    
    # class method
    def logistic_support(self, materials_used: int):
        if self.material_quantity > materials_used:
            print("The unit supplied and performed maintenance")
        else:
            print("Insufficient materials")

class Reconnaissance(MilitaryUnit):
    # adds new non-inherited attributes
    def __init__(self, name, soldier_count, mission_duration: int):
        super().__init__(name, soldier_count)
        self.mission_duration = mission_duration
    
    # class method
    def conduct_reconnaissance(self, area):
        print(f"The unit conducted reconnaissance in {area} for {self.mission_duration}")