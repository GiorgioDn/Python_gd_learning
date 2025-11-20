from .TicketRiparazione import TicketRiparazione

class Officina:
    #prende una stringa ed una lista di ticket di riparazione
    def __init__(self, nome:str, tickets:list[TicketRiparazione] = []):
        self.__nome = nome
        self.__tickets = tickets
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, value:str):
        self.__nome = value
        
    def aggiungi_ticket(self, tickets:TicketRiparazione):
        self.__tickets.append(tickets)
        
    #metodo che chiude il ticket dopo aver trovato quello con l'id 
    def chiudi_ticket(self, id_ticket:str):
        for ticket in self.__tickets:
            if ticket.get_id_ticket() == id_ticket:
                ticket.set_stato("chiuso")
                
    #restituisce i ticket che hanno l'attributo id ad aperto
    def stampa_ticket_aperti(self):
        for ticket in self.__tickets:
            if ticket.get_id_ticket() == "aperto":
                print(f"{ticket.get_id_ticket()} - {ticket.get_elettrodomestico} - {ticket.get_stato}")
    
    #definisco il costo totale
    def totale_preventivi(self):
        prev_tot = 0
        for ticket in self.__tickets:
            prev_tot += ticket.get_preventivo()
        return prev_tot
                