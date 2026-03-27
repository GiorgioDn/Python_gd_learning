from .module.RoleEmplyee import *
from .module.Company import *

def main():
    
    company = Company("Python Academy Class")
    
    while True:
        
        print("\n Select company option")
        print("1. Add an employee")
        print("2. Add an administrator")
        print("3. Add a director")
        print("4. Add departments")
        print("5. View employees")
        print("6. View departments")
        print("7. Verify entries")
        print("8. Exit")
        choice = int(input("Choose an option: "))
        
        match choice:
            case 1:
                badge = []
                shifts = []
                info = input("Enter first name for the badge: ")
                badge.append(info)
                
                info = input("Enter last name for the badge: ")
                badge.append(info)
                
                info = input("Enter role for the badge: ")
                badge.append(info)
                
                info = input("Enter company name for the badge: ")
                badge.append(info)
                
                info = float(input("Enter entry time: "))
                shifts.append(info)
                
                info = float(input("Enter exit time: "))
                shifts.append(info)
                
                employee = Employee(badge, shifts)
                
                company.add_employee(employee)
                
            case 2:
                badge = []
                shifts = []
                info = input("Enter first name for the badge: ")
                badge.append(info)
                
                info = input("Enter last name for the badge: ")
                badge.append(info)
                
                info = input("Enter role for the badge: ")
                badge.append(info)
                
                info = input("Enter company name for the badge: ")
                badge.append(info)
                
                info = float(input("Enter entry time: "))
                shifts.append(info)
                
                info = float(input("Enter exit time: "))
                shifts.append(info)
                
                info = input("Enter responsible department: ")
                
                administrator = Administrator(badge, shifts, info)
                
                company.add_employee(administrator)
            case 3:
                badge = []
                shifts = []
                departments = []
                info = input("Enter first name for the badge: ")
                badge.append(info)
                
                info = input("Enter last name for the badge: ")
                badge.append(info)
                
                info = input("Enter role for the badge: ")
                badge.append(info)
                
                info = input("Enter company name for the badge: ")
                badge.append(info)
                
                info = float(input("Enter entry time: "))
                shifts.append(info)
                
                info = float(input("Enter exit time: "))
                shifts.append(info)
                
                for n in range(3):
                    info = input("Enter department of competence: ")
                    departments.append(info)
                
                director = Director(badge, shifts, departments)
                
                company.add_employee(director)
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
else: 
    print("Module imported")