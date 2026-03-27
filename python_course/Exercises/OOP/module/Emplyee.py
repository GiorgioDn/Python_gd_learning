from abc import ABC, abstractmethod

# abstract class with encapsulation
class Employee(ABC):
    # define the abstract parent class Employee which takes a list of strings and a list of floats
    def __init__(self, badge: list[str], shift_hours: list[float]):
        super().__init__()
        self.__badge = badge
        self.__shift_hours = shift_hours
    
    # abstract method to be implemented in child classes  
    @abstractmethod
    def access_control(self):
        pass
    
    # getter 
    def get_badge(self):
        return self.__badge
    
    # setter
    def set_badge(self, badge: list[str]):
        self.__badge = badge
     
    # getter    
    def get_shift_hours(self):
        return self.__shift_hours
    
    # setter
    def set_shift_hours(self, shift_hours: list[float]):
        self.__shift_hours = shift_hours