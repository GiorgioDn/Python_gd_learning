from .Veicolo import Veicolo

class Furgone(Veicolo):
    def __init__(self, marca:str, modello:str, anno:int, accensione:bool, capacità_carico:int):
        super().__init__(marca, modello, anno, accensione)
        self.__capacità_carico = capacità_carico
    
    def get_capacità_carico(self):
        if self.__capacità_carico > 0:
            return self.__capacità_carico
        else:
            return False
        
    def set_capacità_carico(self, capacità_carico:int):
        if self.__capacità_carico > 0:
            self.__capacità_carico = capacità_carico
        else:
            return False
    
    def carica(self, quantita):
        if self.__capacità_carico >= quantita:
            self.__capacità_carico -= quantita
        else:
            return "Capacità insufficente"
    
    def scarica(self, quantita):
        if self.__capacità_carico <= quantita:
            self.__capacità_carico += quantita
        else:
            return "Quantità insufficente"