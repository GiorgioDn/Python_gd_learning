from .module.ManagePay import PaymentManager
from .module.Pay import *
from .module.PayMethod import *

def main():
    while True:
        
        print("\n Select payment method")
        print("1. Credit Card")
        print("2. Paypal")
        print("3. Iban")
        print("4. Exit")
        choice = int(input("Choose an option: "))
        
        match choice:
            case 1:
                card_number = input("Card number: ")
                expiry_date = input("Expiration date: ")
                cvv = int(input("cvv: "))
                
                card = CreditCard(card_number, expiry_date, cvv)
                
                amount = float(input("Select the amount: "))
                manager = PaymentManager()
                print(manager.process_payment(card, amount))
            case 2:
                account = input("Email account: ")
                
                paypal = PayPal(account)
                
                amount = float(input("Select the amount: "))
                manager = PaymentManager()
                print(manager.process_payment(paypal, amount))
            case 3:
                iban = input("Iban: ")
                swift = input("Swift: ")
                
                account = BankTransfer(iban, swift)
                
                amount = float(input("Select the amount: "))
                manager = PaymentManager()
                print(manager.process_payment(account, amount))
            case 4:
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
else: 
    print("Module imported")