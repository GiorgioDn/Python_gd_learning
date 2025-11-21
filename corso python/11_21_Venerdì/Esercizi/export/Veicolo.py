from .VeicoloTrasporto import VeicoloTrasporto

#classe figlio della classe astratta VeicoloTrasporto
class Camion(VeicoloTrasporto):
    def __init__(self, targa:str, peso_massimo:int, numero_assi:int, carico_attuale:int = 0):
        super().__init__(targa, peso_massimo, carico_attuale)
        self.numero_assi = numero_assi
        
    #implementazione del metodo astratto
    def costo_manutenzione(self):
        costo = 100*self.numero_assi + 1*self._peso_massimo
        return costo

#classe figlio della classe astratta VeicoloTrasporto
class Furgone(VeicoloTrasporto):
    def __init__(self, targa:str, peso_massimo:int, alimentazione:str, carico_attuale:int = 0):
        super().__init__(targa, peso_massimo, carico_attuale)
        self.alimentazione = alimentazione
    
    #implementazione del metodo astratto
    def costo_manutenzione(self):
        if self.alimentazione.lower() == "elettrico":
            costo = 200
        else:
            costo = 150
        return costo

#classe figlio della classe astratta VeicoloTrasporto
class Motocarro(VeicoloTrasporto):
    def __init__(self, targa:str, peso_massimo:int, anni_servizio:int, carico_attuale:int = 0):
        super().__init__(targa, peso_massimo, carico_attuale)
        self.anni_servizio = anni_servizio
    
    #implementazione del metodo astratto   
    def costo_manutenzione(self):
        costo = 50*self.anni_servizio
        return costo