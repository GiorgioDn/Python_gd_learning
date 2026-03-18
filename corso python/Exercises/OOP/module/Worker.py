from abc import ABC, abstractmethod

#classe astratta impegrato con un costruttore
class Impegato(ABC):
    #il costruttore prende in input due stringhe e lo stipendio base
    def __init__(self, nome:str, cognome:str, stipendio_base:float):
        super().__init__()
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
        
    #metodo da implementare nelle classi figlie
    @abstractmethod
    def calcola_stipendio(self):
        pass