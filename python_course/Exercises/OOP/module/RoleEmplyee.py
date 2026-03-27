from .Emplyee import Employee

# inheritance and polymorphism
class Staff(Employee):
    # does not expand the init of the abstract class
    def __init__(self, badge: list[str], shift_hours: list[float]):
        super().__init__(badge, shift_hours)
    
    # overrides the abstract method 
    def access_control(self, time: float):
        if time in self.get_shift_hours():
            return f"Access allowed"
        else:
            return f"Access denied"

class Administrator(Employee):
    # takes the abstract class parameters and adds a string parameter
    def __init__(self, badge: list[str], shift_hours: list[float], department: str):
        super().__init__(badge, shift_hours)
        self.__department = department
    
    def get_department(self):
        return self.__department
    
    def set_department(self, department: str):
        self.__department = department
    
    # overrides the abstract method 
    def access_control(self, time: float, department: str):
        if time in self.get_shift_hours() and self.__department.lower() == department.lower():
            return f"Access allowed"
        else:
            return f"Access denied"

class Director(Employee):
    # takes the abstract class parameters and adds a list of strings parameter in simulated overloading
    def __init__(self, badge: list[str], shift_hours: list[float], department_list: list[str] = []):
        super().__init__(badge, shift_hours)
        self.__department_list = department_list
        
    def get_department_list(self):
        return self.__department_list
    
    def add_to_department_list(self, department: str):
        self.__department_list.append(department.lower())
    
    # overrides the abstract method     
    def access_control(self, time: float, department: str):
        if time in self.get_shift_hours() and department.lower() in self.__department_list:
            return f"Access allowed"
        else:
            return f"Access denied"