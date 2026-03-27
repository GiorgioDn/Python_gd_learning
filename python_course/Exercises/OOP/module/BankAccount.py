class BankAccount:
    
    # the class takes a string and a float as input and assigns them as private values
    def __init__(self, account_holder: str, balance: float):
        self.__account_holder = account_holder
        self.__balance = balance
    
    # displays the private variable account_holder
    def get_account_holder(self):
        if len(self.__account_holder) > 0:
            return self.__account_holder
        else:
            return False
    
    # modifies the value of the private variable account_holder
    def set_account_holder(self, account_holder: str):
        if len(account_holder) > 0:
            self.__account_holder = account_holder
        else:
            return False
    
    # increases the balance based on the float value entered
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            return False

    # decreases the balance based on the float value entered
    def withdraw(self, amount: float):
        if amount > 0 and self.__balance >= amount:   
            self.__balance -= amount
        else:
            return False
    
    # displays the private variable balance
    def display_balance(self):
        return self.__balance