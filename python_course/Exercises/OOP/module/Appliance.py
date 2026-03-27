class Appliance:
    # takes two strings, an int, and another string as input
    def __init__(self, make: str, model: str, purchase_year: int, fault: str):
        self.__make = make
        self.__model = model
        self.__purchase_year = purchase_year
        self.__fault = fault

    # getter
    def get_make(self):
        return self.__make

    # setter
    def set_make(self, value: str):
        self.__make = value

    # getter
    def get_model(self):
        return self.__model

    # setter
    def set_model(self, value: str):
        self.__model = value

    # getter
    def get_purchase_year(self):
        if self.__purchase_year <= 2025:
            return self.__purchase_year
        else:
            return False

    # setter
    def set_purchase_year(self, value: int):
        self.__purchase_year = value

    # getter
    def get_fault(self):
        return self.__fault

    # setter
    def set_fault(self, value: str):
        self.__fault = value
    
    # returns a descriptive string of the class
    def description(self):
        return f"{self.__make}, {self.__model} produced in the year {self.__purchase_year} with the following problem: {self.__fault}"

    # returns a float value
    def estimate_base_cost(self):
        base_cost = 10.0
        return base_cost