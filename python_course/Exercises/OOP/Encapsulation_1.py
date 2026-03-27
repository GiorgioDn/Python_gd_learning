from .module.BankAccount import BankAccount

while True:
    
    print("Register with the holder's name and the initial balance")
    holder = input("Holder: ")
    balance = float(input("Balance: "))     
    
    account = BankAccount(holder, balance)
    
    holder = account.get_holder()
    
    while True:
        if holder == False:
            holder = input("Name not present, you must select a name for the holder: ")
            account.set_holder(holder)
            holder = account.get_holder()
        else:
            break
        
    print(f"The account holder is: {holder}")
    
    balance = account.view_balance()
    
    print(f"The current balance is {balance} euro")
    
    choice = int(input("Select 1 to deposit, 2 to withdraw: "))
    
    match choice:
        case 1:
            choice = float(input("Select the amount to deposit: "))
            deposit = account.deposit(choice)
            while True:
                if deposit == False:
                    choice = float(input("Invalid amount, select a new amount to deposit: "))
                    deposit = account.deposit(choice)
                else: 
                    break
            balance = account.view_balance()
            print(f"The current balance is {balance} euro")
            
        case 2:
            choice = float(input("Select the amount to withdraw: "))
            withdraw = account.withdraw(choice)
            while True:
                if withdraw == False:
                    if choice > account.view_balance():
                        choice = float(input("Insufficient balance, select a new amount to withdraw: "))
                        withdraw = account.withdraw(choice)
                    else:
                        choice = float(input("Invalid amount, select a new amount to withdraw: "))
                        withdraw = account.withdraw(choice)
                else: 
                    break
            balance = account.view_balance()
            print(f"The current balance is {balance} euro")
        case _:
            print("Invalid choice")
    
    choice = input("Do you want to log in as a different person? ")
    
    if choice.lower() == "no":
        break