class Seat:
    # define the seat class with int and string parameters
    def __init__(self, number: int, row: str):
        self.__number = number
        self.__row = row
        # initially set the attribute to False
        self.__occupied = False 
    
    # use only getters because the data is not modifiable
    def get_number(self):
        return self.__number

    def get_row(self):
        return self.__row
    
    def get_occupied(self):
        return self.__occupied
    
    # reservation method to manage bookings
    def reserve(self):
        if self.__occupied == False:
            self.__occupied = True
            return f"Seat number: {self.__number} in row: {self.__row} has been reserved"
        else:
            return f"Seat number: {self.__number} in row: {self.__row} is occupied"
    
    # method to release the seat and change the occupied status
    def release(self):
        if self.__occupied == True:
            self.__occupied = False
            return f"Seat number: {self.__number} in row: {self.__row} has been released"
        else:
            return f"Seat number: {self.__number} in row: {self.__row} is free"