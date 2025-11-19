from .Persona import *

class Professore(Persona):
    #prende in input i valori della superclasse e una stringa
    def __init__(self, nome:str, eta:int, materia:str):
        super().__init__(nome, eta)
        self.__materia = self.set_materia(materia)
     
    #con i get accedo ai corrispettivi parametri   
    def get_materia(self):
        return self.__materia
    
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