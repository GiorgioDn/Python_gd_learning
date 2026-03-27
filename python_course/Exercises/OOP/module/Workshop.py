from .RepairTicket import RepairTicket

class Workshop:
    # takes a string and a list of repair tickets
    def __init__(self, name: str, tickets: list[RepairTicket] = []):
        self.__name = name
        self.__tickets = tickets
        
    def get_name(self):
        return self.__name
    
    def set_name(self, value: str):
        self.__name = value
        
    def add_ticket(self, ticket: RepairTicket):
        self.__tickets.append(ticket)
        
    # method that closes the ticket after finding the one with the id 
    def close_ticket(self, ticket_id: str):
        for ticket in self.__tickets:
            if ticket.get_ticket_id() == ticket_id:
                ticket.set_status("closed")
                
    # returns the tickets that have the status attribute set to open
    def print_open_tickets(self):
        for ticket in self.__tickets:
            if ticket.get_status() == "open":
                print(f"{ticket.get_ticket_id()} - {ticket.get_appliance} - {ticket.get_status}")
    
    # define the total cost
    def total_estimates(self):
        total_est = 0
        for ticket in self.__tickets:
            total_est += ticket.get_estimate()
        return total_est
                