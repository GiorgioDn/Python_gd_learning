from .RoleEmplyee import Staff as Employee

# the fixed employee class uses the same constructor method
class FixedEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float):
        super().__init__(first_name, last_name, base_salary)

    # overrides the abstract method        
    def calculate_salary(self):
        return f"The salary of {self.first_name} {self.last_name} is {self.base_salary} euros"
        
# the commission employee class uses the same constructor method
class CommissionEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float):
        super().__init__(first_name, last_name, base_salary)
    
    # overrides the abstract method by adding an attribute
    def calculate_salary(self, commission: float):
        salary = self.base_salary + commission
        return f"The salary of {self.first_name} {self.last_name} is {salary} euros, of which {commission} is commission"