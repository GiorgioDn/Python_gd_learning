#classe base
class Animale:

    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print(f"{self.nome} fa suono generico.")


#classe derivata (eredita da Animale)
class Cane(Animale):

    #si sovrascrive il metodo 
    def parla(self):
        print(f"{self.nome} abbaia!")
        
animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla()
cane.parla()  

#multiereditarietà
#classi base
class Veicolo:
    def __init__(self, marca, modello):    
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")


class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

#classe che eredità entrambe le classi base       
class AutomobileSportiva(Veicolo, DotazioniSpeciali):

    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)  
        #alternativa a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self):
        super().mostra_informazioni()  
        #chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()  

auto_sportiva = AutomobileSportiva("Ferrari", "F8", ["ABS", "Controllotrazione", "Airbag laterali"], 720)

auto_sportiva.mostra_informazioni()