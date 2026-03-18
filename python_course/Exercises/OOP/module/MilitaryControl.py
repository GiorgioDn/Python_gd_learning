from .Unit import *

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    #prende tutti i parametri delle classi padre più una nuova
    def __init__(self, nome, numero_soldati, armi, gittata, velocita, quantita_materiali, durata_missione, unita_registrate):
        super().__init__(nome, numero_soldati, armi)
        Artiglieria.__init__(nome, numero_soldati, gittata)
        Cavalleria.__init__(nome, numero_soldati, velocita)
        SupportoLogistico.__init__(nome, numero_soldati, quantita_materiali)
        Ricognizione.__init__(nome, numero_soldati, durata_missione)
        self.unita_registrate = unita_registrate
        
    #splitta l'unita creando una lista di liste
    def registra_unita(self, unita):
        return self.unita_registrate.append(*unita)
    
    def mostra_unita(self):
        return self.unita_registrate
    
    #itera la lista per trovare il nome
    def dettagli_unita(self, nome):
        for specific_unit in self.unita_registrate:
            if specific_unit[0] == nome:
                return specific_unit