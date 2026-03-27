from abc import ABC, abstractmethod

# abstract class employee with a constructor
class Employee(ABC):
    # the constructor takes two strings and the base salary as input
    def __init__(self, first_name: str, last_name: str, base_salary: float):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        
    # method to be implemented in child classes
    @abstractmethod
    def calculate_salary(self):
        pass