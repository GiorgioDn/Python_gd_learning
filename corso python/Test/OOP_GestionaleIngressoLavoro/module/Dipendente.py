from abc import ABC, abstractmethod

#classe astratta con incapsulamento
class Dipendente(ABC):
    #definisco la classe padre astratta dipendente che prende una lista di stringhe ed una lista di float
    def __init__(self, badge:list[str], orari_turni:list[float]):
        super().__init__()
        self.__badge = badge
        self.__orari_turni = orari_turni
    
    #metodo astratto da implementare nelle classi filgie  
    @abstractmethod
    def controllo_accesso(self):
        pass
    
    #getter 
    def get_badge(self):
        return self.__badge
    
    #setter
    def set_badge(self, badge:list[str]):
        self.__badge = badge
     
    #getter    
    def get_orari_turni(self):
        return self.__orari_turni
    
    #setter
    def set_orari_turni(self, orari_turni:list[float]):
        self.__orari_turni = orari_turni