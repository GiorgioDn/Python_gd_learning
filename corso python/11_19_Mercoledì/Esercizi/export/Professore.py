from .Persona import *

class Professore(Persona):
    #prende in input i valori della superclasse e una stringa
    def __init__(self, nome:str, eta:int, materia:str):
        super().__init__(nome, eta)
        self.__materia = materia
     
    #con i get accedo ai corrispettivi parametri   
    def get_materia(self):
        if len(self.__materia) > 0:
            return self.__materia
        else:
            return False
    
    #con i set modifico i parametri
    def set_materia(self, materia:str):
        if len(materia) > 0:
            self.__materia = materia
        else:
            return False
    
    #metodo di presentazione sovrascritto
    def presentazione(self):
        base = super().presentazione()
        return f"Il professore {base} ed insegna la seguente materia: {self.__materia}"