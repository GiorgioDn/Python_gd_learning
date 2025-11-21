from .VeicoloTrasporto import VeicoloTrasporto
from .Veicolo import * 

#classe generica per manipolare una lista di tipo VeicoloTrasporto
class GestoreFlotta:
    def __init__(self, veicoli:list[VeicoloTrasporto]):
        self.veicoli = veicoli
    
    def aggiungi_veicolo(self, veicolo:VeicoloTrasporto):
        self.veicoli.append(veicolo)
        
    def rimuovi_veicolo(self, targa:str):
        for n in self.veicoli:
            if n._targa == targa:
                self.veicoli.remove(n)
     
    #somma i costi totali eseguendo il metodo costo_manutenzione presente nella classe VeicoloTrasporto           
    def costo_totale_manutenzione(self):
        costo_tot = 0
        for n in self.veicoli:
            costo_tot += n.costo_manutenzione()
            
        return costo_tot
    
    #stampa in base al tipo della classe figlio di VeicoloTrasporto
    def stampa_veicoli(self):
        for n in self.veicoli:
            if type(n) == Camion:
                print(f"Veicolo: {n._targa} - Tipo: Camion - Carico attuale: {n._carico_attuale}")
            elif type(n) == Furgone:
                print(f"Veicolo: {n._targa} - Tipo: Furgone - Carico attuale: {n._carico_attuale}")
            else:
                print(f"Veicolo: {n._targa} - Tipo: Motocarro - Carico attuale: {n._carico_attuale}")