from .Seat import Seat

class StandardSeat(Seat):
    # define the seat class with parameters inherited from the Seat class and an additional float
    def __init__(self, number: int, row: str, cost: float):
        super().__init__(number, row)
        self.__cost = cost
    
    def get_cost(self):
        return self.__cost
    
    # override the reservation method
    def reserve(self):
        base = super().reserve()
        if super().get_occupied() == False:
            return f"{base} at a cost of {self.__cost}"
        else:
            return base

class VIPSeat(Seat):
    # define the seat class with parameters inherited from the Seat class plus a float and a list of strings
    def __init__(self, number: int, row: str, cost: float, extra_services: list[str]):
        super().__init__(number, row)
        self.__cost = cost
        self.__extra_services = extra_services
        
    def get_extra_services(self):
        return self.__extra_services
    
    # override the reservation method
    def reserve(self):
        base = super().reserve()
        if super().get_occupied() == False:
            return f"{base} at a cost of {self.__cost} with the possibility of activating the following services: {self.__extra_services}"
        else:
            return base

        