from abc import ABC,abstractmethod

#classe astratta che prende in input una stringa e due interi
class VeicoloTrasporto(ABC):
    #carico_attuale ha un valore di default di 0
    def __init__(self, targa:str, peso_massimo:int, carico_attuale:int = 0):
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = carico_attuale
    
    #da implementare nelle classi filgie
    @abstractmethod
    def costo_manutenzione(self):
        pass

    #controlla se è possibile aggiungere il valore int per poi aggiornare l'attributo carico_atttuale
    def carica(self, peso:int):
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            return f"È stato caricato, il carico attuale è: {self._carico_attuale} kg su {self._peso_massimo} kg massimi"
        else:
            return f"Non può essere inserito perchè supera il carico massimo di {self._peso_massimo} kg"
    
    #imposta a 0 il carico_attuale    
    def scarica(self):
        self._carico_attuale = 0