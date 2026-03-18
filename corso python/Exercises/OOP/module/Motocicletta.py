from .Veicolo import Veicolo

class Motocicletta(Veicolo):
    def __init__(self, marca:str, modello:str, anno:int, accensione:bool, tipo:str):
        super().__init__(marca, modello, anno, accensione)
        self.__tipo = tipo
    
    def get_tipo(self):
        if len(self.__tipo) > 0:
            return self.__tipo
        else:
            return False
        
    def set_tipo(self, tipo:int):
        if len(self.__tipo)  > 0:
            self.__tipo = tipo
        else:
            return False
    
    def esegui_wheelie(self):
        if self.__tipo == "sportivo":
            return "Esegue un wheelie"
        else:
            return "Non esegue il wheelie"
        
