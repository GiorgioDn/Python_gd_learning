from .module.Theatre import *
from .module.SpecialSeat import *

def main():
    
    theatre = Theater([])   
    
    while True:
        
        print("\n Select the operation to perform")
        print("1. Add a standard seat")
        print("2. Add a VIP seat")
        print("3. View occupied seats")
        print("4. Book a seat")
        print("5. Exit")
        choice = int(input("Choose an option: "))
        
        match choice:
            case 1:
                number = int(input("Number: "))
                row = input("Row: ")
                cost = input("Cost: ")
                
                standard_seat = standard_seat(number, row, cost)
                theatre.add_seat(standard_seat)
                
            case 2:
                services = []
                number = int(input("Number: "))
                row = input("Row: ")
                cost = input("Cost: ")
                print("Add 2 special services")
                for n in range(2):
                    service = input("Service: ")
                    services.append(service)
                
                vip_seat = vip_seat(number, row, cost, services)
                theatre.add_seat(vip_seat)
            case 3:
                theatre.print_occupied_seats()
            case 4:
                number = int(input("Seat Number: "))
                row = input("Seat Row: ")
                theatre.reserve_seat(number, row)
            case 5:
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
else: 
    print("Module imported")