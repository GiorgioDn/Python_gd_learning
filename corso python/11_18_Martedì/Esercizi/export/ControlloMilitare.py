from Unita import *

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self, nome, numero_soldati, armi, gittata, velocita, quantita_materiali, durata_missione, unita_registrate):
        super().__init__(nome, numero_soldati, armi)
        Artiglieria.__init__(nome, numero_soldati, gittata)
        Cavalleria.__init__(nome, numero_soldati, velocita)
        SupportoLogistico.__init__(nome, numero_soldati, quantita_materiali)
        Ricognizione.__init__(nome, numero_soldati, durata_missione)
        self.unita_registrate = unita_registrate