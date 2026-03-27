from .Appliance import Appliance

class RepairTicket:
    # takes a string and an Appliance as input
    def __init__(self, ticket_id: str, appliance: Appliance): # type: ignore
        self.__ticket_id = ticket_id
        self.__appliance = appliance
        self.__status = "open"
        self.__notes = []
        self.__estimate = appliance.estimate_base_cost() # type: ignore

    # getter
    def get_ticket_id(self):
        return self.__ticket_id

    def set_ticket_id(self, value: str):
        self.__ticket_id = value

    # getter
    def get_appliance(self):
        return self.__appliance

    def set_appliance(self, value: Appliance): # type: ignore
        self.__appliance = value

    # getter
    def get_status(self):
        return self.__status

    def set_status(self, value: str):
        self.__status = value
        
    # getter
    def get_estimate(self):
        return self.__estimate

    # getter
    def get_notes(self):
        return self.__notes

    # adds elements to the notes string list
    def add_note(self, note: str):
        self.__notes.append(note)
    
    # takes a default list of values
    def calculate_estimate(self, param_list: list[float] = [0]):
        for cost in param_list:
            self.__estimate += cost