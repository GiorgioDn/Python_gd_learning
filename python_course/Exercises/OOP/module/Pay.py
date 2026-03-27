from .PayMethod import PaymentMethod

class CreditCard(PaymentMethod):
    def __init__(self, card_number: str, expiry_date: str, cvv: int):
        self.__card_number = card_number
        self.__expiry_date = expiry_date
        self.__cvv = cvv
        
    def get_card_number(self):
        return self.__card_number
    
    def get_expiry_date(self):
        return self.__expiry_date
    
    def get_cvv(self):
        return self.__cvv
    
    def process_payment(self, amount: float):
        if len(self.__card_number) >= 16:
            # Note: Validating numeric strings usually involves .isdigit()
            if self.__card_number.isdigit():
                if len(str(self.__cvv)) == 3:
                    return f"Credit card payment processed for the amount: {amount} euros"
        else: 
            return False

class PayPal(PaymentMethod):
    def __init__(self, account: str):
        self.__account = account
        
    def get_account(self):
        return self.__account
    
    def process_payment(self, amount: float):
        return f"PayPal payment of {amount} euros processed"

class BankTransfer(PaymentMethod):
    def __init__(self, iban: str, swift: str):
        self.__iban = iban
        self.__swift = swift
    
    def get_swift(self):
        return self.__swift  
        
    def get_iban(self):
        return self.__iban
        
    def process_payment(self, amount: float):
        if len(self.__iban) >= 27:
            return f"Bank transfer of {amount} euros processed"
        else: 
            return False
        
    
    
