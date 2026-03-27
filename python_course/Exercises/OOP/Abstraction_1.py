from .module.WorkerRole import *


def main():
    
    employees = []
    
    while True:
        
        print("\n Company employees")
        print("1. Add salaried employees")
        print("2. Add commissioned employees")
        print("3. View employee salaries")
        print("4. Exit")
        choice = int(input("Choose an option: "))
        
        match choice:
            case 1:
                first_name = input("Enter employee's first name: ")
                last_name = input("Enter last name: ")
                salary = float(input("Enter salary: "))

                salaried_employee = FixedEmployee(first_name, last_name, salary)
                employees.append(salaried_employee)

            case 2:
                first_name = input("Enter employee's first name: ")
                last_name = input("Enter last name: ")
                salary = float(input("Enter salary: "))

                commissioned_employee = CommissionEmployee(first_name, last_name, salary)
                employees.append(commissioned_employee)

            case 3:
                for emp in employees:
                    if isinstance(emp, CommissionEmployee):
                        commission = float(input("The employee is commissioned, enter the commission: "))
                        print(emp.calculate_salary(commission))
                    else:
                        print(emp.calculate_salary())

            case 4:
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
else: 
    print("Module imported")