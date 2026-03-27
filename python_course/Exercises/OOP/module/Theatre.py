class Theater:
    def __init__(self, seats: list[Seat]): # type: ignore
        self.__seats = seats
        
    def add_seat(self, seat: Seat): # type: ignore
        return self.__seats.append(seat)
        
    def print_occupied_seats(self):
        for seat in self.__seats:
            if seat.get_occupied() == True:
                print(seat.reserve())
    
    def reserve_seat(self, number: int, row: str):
        for seat in self.__seats:
            if seat.get_number() == number and seat.get_row() == row:
                print(seat.reserve())