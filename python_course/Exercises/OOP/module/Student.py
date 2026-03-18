from .Person import *

class Studente(Persona):
    #prende in input i valori della superclasse e una lista di interi
    def __init__(self, nome:str, eta:int, voti:list[int]):
        super().__init__(nome, eta)
        self.__voti = voti
    
    #con i get accedo ai corrispettivi parametri
    def get_voti(self):
        if len(self.__voti) > 0:
            return self.__voti
        else:
            return False
    
    #con i set modifico i parametri
    def set_voti(self, voti:list[int]):
        if len(voti) > 0:
            self.__voti = voti
        else:
            return False
    
    #metodo per aggiungere un singolo voto
    def add_voto(self, voto:int):
        if voto > 0 and voto <= 10:
            self.__voti.append(voto)
        else:
            return False
    
    #metodo per calcolare
    def calcola_media(self):
        average = 0
        elem = len(self.__voti)
        if elem > 0:
            for voti in self.__voti:
                average += voti
            average = average/elem
            return average
        else:
            return False
    
    #metodo di presentazione sovrascritto
    def presentazione(self):
        base = super().presentazione()
        return f"Lo studente {base} ed i seguenti voti: {self.__voti}"