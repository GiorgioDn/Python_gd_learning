from .RoleEmplyee import Impiegato as Impegato

#la classe impiegato fisso prende il metodo costruttore uguale
class ImpiegatoFisso(Impegato):
    def __init__(self, nome:str, cognome:str, stipendio_base:float):
        super().__init__(nome, cognome, stipendio_base)

    #sovrascrive il metodo astratto        
    def calcola_stipendio(self):
        return f"Lo stipendio di {self.nome} {self.cognome} è di {self.stipendio_base} euro"
        
#la classe impiegato a provvigione prende il metodo costruttore uguale
class ImpiegatoAProvvigione(Impegato):
    def __init__(self, nome:str, cognome:str, stipendio_base:float):
        super().__init__(nome, cognome, stipendio_base)
    
    #sovrascrive il metodo astratto aggiungedoci un attributo
    def calcola_stipendio(self, provvigione:float):
        stipendio = self.stipendio_base + provvigione
        return f"Lo stipendio di {self.nome} {self.cognome} è di {stipendio} euro di cui {provvigione} sono di provvigione"