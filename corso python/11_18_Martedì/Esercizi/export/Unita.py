from UnitaMilitare import UnitaMilitare

class Fanteria(UnitaMilitare):
    #aggiunge nuovi attributi non ereditati
    def __init__(self, nome, numero_soldati, armi:str):
        super().__init__(nome, numero_soldati)
        self.armi = armi
    
    #metodo di classe
    def costruisci_trincea(self, materiali):
        print(f"Costruita una trincea con {materiali}")

class Artiglieria(UnitaMilitare):
    #aggiunge nuovi attributi non ereditati
    def __init__(self, nome, numero_soldati, gittata:int):
        super().__init__(nome, numero_soldati)
        self.gittata = gittata
    
    #metodo di classe
    def calibra_artiglieria(self, calibra:int):
        if calibra<self.gittata:
            print("Calibrazione completata per colpire il bersaglio")
        else:
            print("Bersaglio troppo distante")

class Cavalleria(UnitaMilitare):
    #aggiunge nuovi attributi non ereditati
    def __init__(self, nome, numero_soldati, velocita:int):
        super().__init__(nome, numero_soldati)
        self.velocita = velocita
    
    #metodo di classe
    def esplora_terreno(self, area):
        print(f"Le unità hanno esplorato {area} trovando informazioni")

class SupportoLogistico(UnitaMilitare):
    #aggiunge nuovi attributi non ereditati
    def __init__(self, nome, numero_soldati, quantita_materiali:int):
        super().__init__(nome, numero_soldati)
        self.quantita_materiali = quantita_materiali
    
    #metodo di classe
    def supporto_logistico(self, materiali_usati:int):
        if self.quantita_materiali>materiali_usati:
            print("L'unità ha rifornito ed eseguito la manutenzione")
        else:
            print("Materiali insufficienti")

class Ricognizione(UnitaMilitare):
    #aggiunge nuovi attributi non ereditati
    def __init__(self, nome, numero_soldati, durata_missione:int):
        super().__init__(nome, numero_soldati)
        self.durata_missione = durata_missione
    
    #metodo di classe
    def conduci_ricognizione(self, area):
        print(f"L'unità ha effettuato la ricognizione in {area} per {self.durata_missione}")