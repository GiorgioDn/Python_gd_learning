from .Veicolo import Veicolo

class GestoreParcoVeicoli():
    def __init__(self, veicoli:list[Veicolo] = []):
        self.__veicoli = veicoli
        
    def lista_veicoli(self):
        if len(self.__veicoli) > 0:
            return self.__veicoli
        else:
            return False
        
    def aggiungi_veicolo(self, veicolo:Veicolo):
        self.__veicolo.append(veicolo)
    
    def rimuovi_veicolo(self, marca, modello):
        for n in self.__veicoli:
            if n.get_marca() == marca and n.get_modello() == modello:
                self.__veicoli.remove(n)