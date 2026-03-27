from .Emplyee import Employee
from .RoleEmplyee import *

# polymorphism
class Company:
    # takes a string as the only mandatory parameter
    def __init__(self, name: str, employees: list[Employee] = [], departments: list[str] = []):
        self.__name = name
        self.__employees = employees
        self.__departments = departments
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name: str):
        self.__name = name
        
    def add_employee(self, employee: Employee):
        self.__employees.append(employee)
        
    def add_department(self, department: str):
        self.__departments.append(department)
        
    def remove_employee(self, badge: str):
        for employee in self.__employees:
            for info in employee.get_badge():
                if info.lower() == badge.lower():
                    self.__employees.remove(employee)
    
    def remove_department(self, department: str):
        for dept in self.__departments:
            if dept.lower() == department.lower():
                self.__departments.remove(dept)
          
    # prints a message based on the type of employees contained in the employee list      
    def show_employees(self):
        for emp in self.__employees:
            if type(emp) == Staff:
                print(f"Staff member {emp.get_badge()} has the following shifts: {emp.get_shift_hours()}")
            elif type(emp) == Administrator:
                print(f"Administrator {emp.get_badge()} has the following shifts: {emp.get_shift_hours()} and manages the {emp.get_department()} department")
            elif type(emp) == Director:
                print(f"Director {emp.get_badge()} has the following shifts: {emp.get_shift_hours()} and manages the following departments: {emp.get_department_list()}")
            else:
                print("Unknown role")