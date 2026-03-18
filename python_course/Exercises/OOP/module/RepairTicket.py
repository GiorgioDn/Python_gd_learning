from .Appliance import Elettrodomestico


class TicketRiparazione:
    #prende in input una stringa ed un Elettrodomestico
    def __init__(self, id_ticket:str, elettrodomestico:Elettrodomestico): # type: ignore
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = "aperto"
        self.__note = []
        self.__preventivo = elettrodomestico.stima_costo_base() # type: ignore

    #getter
    def get_id_ticket(self):
        return self.__id_ticket

    def set_id_ticket(self, value:str):
        self.__id_ticket = value

    #getter
    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def set_elettrodomestico(self, value:Elettrodomestico): # type: ignore
        self.__elettrodomestico = value

    #getter
    def get_stato(self):
        return self.__stato

    def set_stato(self, value:str):
        self.__stato = value
        
    #getter
    def get_preventivo(self):
        return self.__preventivo

    #getter
    def get_note(self):
        return self.__note

    #aggiunge elementi alla lista di stringhe note
    def aggiungi_nota(self, nota:str):
        self.__note.append(nota)
    
    #prende una lista di default di valori
    def calcola_preventivo(self, list_param:list[float] = [0]):
        for prev in list_param:
            self.__preventivo += prev
    