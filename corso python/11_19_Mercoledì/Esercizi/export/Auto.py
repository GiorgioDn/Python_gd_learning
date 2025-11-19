from .Veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, marca:str, modello:str, anno:int, accensione:bool, numero_porte:int):
        super().__init__(marca, modello, anno, accensione)
        self.__numero_porte = numero_porte
    
    def get_numero_porte(self):
        if self.__numero_porte > 0:
            return self.__numero_porte
        else:
            return False
        
    def set_numero_porte(self, numero_porte:int):
        if self.__numero_porte > 0:
            self.__numero_porte = numero_porte
        else:
            return False
        
    def suona_clacson(self):
        return "BEEEEEP"