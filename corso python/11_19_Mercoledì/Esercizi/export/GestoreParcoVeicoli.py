from .Veicolo import Veicolo

class GestoreParcoVeicoli():
    def __init__(self, veicoli:list[Veicolo]):
        self.__veicoli = veicoli
        
    def lista_veicoli(self):
        if len(self.__veicoli) > 0:
            return self.__veicoli
        else:
            return False
        
    def aggiungi_veicolo(self, veicolo:Veicolo):
        self.__veicolo.append(veicolo)
    
    def rimuovi_veicolo(self, marca, modello):
        position = 0
        for n in self.__veicoli:
            if marca in n and modello in n:
                self.__veicoli.pop(position)
            else:
                position +=1