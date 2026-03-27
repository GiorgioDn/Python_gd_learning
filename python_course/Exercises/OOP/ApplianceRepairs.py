from .module.Workshop import Workshop
from .module.RepairTicket import RepairTicket
from .module.SpecificAppliance import *
from random import randint

def main():
    
    workshop = Workshop("Repair", [])
    
    while True:
        
        print("\n Enter items to be repaired")
        print("1. Washing Machine")
        print("2. Refrigerator")
        print("3. Oven")
        print("4. Open tickets")
        print("5. Close a ticket")
        print("6. Total estimate")
        print("7. Estimate statistics")
        print("8. Exit")
        choice = int(input("Choose an option: "))
        
        match choice:
            case 1:
                extra = []
                brand = input("Enter the brand of the washing machine: ")
                model = input("Enter the model of the washing machine: ")
                purchase_year = int(input("Enter the purchase year of the washing machine: "))
                fault = input("Describe the fault: ")
                capacity = int(input("Washing machine capacity: ")) 
                rpm = int(input("Spin speed of the washing machine: "))
                
                washing_machine = WashingMachine(brand, model, purchase_year, fault, capacity, rpm)
                
                choice = input("Are there other costs? yes/no: ")
                if choice.lower() == "yes":
                    while True:
                        extra_cost = float(input("Add the extra cost value: "))
                        extra.append(extra_cost)
                        choice = input("Are there other costs? yes/no: ")
                        if choice.lower() == "no":
                            break
                
                id = str(randint(0, 999999999999))
                
                tickets = RepairTicket(id, washing_machine)
                
                tickets.calculate_estimate(extra)
                
                workshop.add_ticket(tickets)

            case 2:
                extra = []
                brand = input("Enter the brand of the refrigerator: ")
                model = input("Enter the model of the refrigerator: ")
                purchase_year = int(input("Enter the purchase year of the refrigerator: "))
                fault = input("Describe the fault: ")
                liters = int(input("Liters it can hold: "))
                freezer = input("Does it have a freezer? yes/no: ")
                
                if freezer.lower() == "yes":
                    freezer = True
                else:
                    freezer = False
                
                refrigerator = Refrigerator(brand, model, purchase_year, fault, liters, freezer)
                
                choice = input("Are there other costs? yes/no: ")
                if choice.lower() == "yes":
                    while True:
                        extra_cost = float(input("Add the extra cost value: "))
                        extra.append(extra_cost)
                        choice = input("Are there other costs? yes/no: ")
                        if choice.lower() == "no":
                            break
                
                id = str(randint(0, 999999999999))
                
                tickets = RepairTicket(id, refrigerator)
                
                tickets.calculate_estimate(extra)
                
                workshop.add_ticket(tickets)
                
            case 3:
                extra = []
                brand = input("Enter the brand of the oven: ")
                model = input("Enter the model of the oven: ")
                purchase_year = int(input("Enter the purchase year of the oven: "))
                fault = input("Describe the fault: ")
                power_supply = input("State if it is electric or gas: ")
                fan_assisted = input("Is it fan-assisted? yes/no: ")
                
                if fan_assisted.lower() == "yes":
                    fan_assisted = True
                else:
                    fan_assisted = False
                
                oven = Oven(brand, model, purchase_year, fault, power_supply, fan_assisted)
                
                choice = input("Are there other costs? yes/no: ")
                if choice.lower() == "yes":
                    while True:
                        extra_cost = float(input("Add the extra cost value: "))
                        extra.append(extra_cost)
                        choice = input("Are there other costs? yes/no: ")
                        if choice.lower() == "no":
                            break
                
                id = str(randint(0, 999999999999))
                
                tickets = RepairTicket(id, oven)
                
                tickets.calculate_estimate(extra)
                
                workshop.add_ticket(tickets)
                
            case 4:
                workshop.print_open_tickets()
            case 5:
                pass
            case 6:
                print(workshop.total_estimates())
            case 7:
                pass
            case 8:
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
else: 
    print("Module imported")