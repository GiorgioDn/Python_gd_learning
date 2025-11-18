from export.Animale import *

#classe Leone figlio della classe Animale
class Leone(Animale):
    #creo gli attributi iniziali con delle aggiunte
    def __init__(self, nome, eta:int, sesso):
        super().__init__(nome, eta)
        self.sesso = sesso
        
    #definisco il mnetodo toString personalizzato
    def __str__(self):
        return f"Il leone {self.nome}, ha {self.eta} anni ed è {self.sesso}"
        
    #sovrascrizione del metodo della classe Animale fai_suono
    def fai_suono(self):
        print("ROAR!")
    
    #metodo di classe
    def caccia(self, preda):
        print(f"Il leone sta cacciando un {preda}")

#classe Giraffa figlio della classe Animale
class Giraffa(Animale):
    #creo gli attributi iniziali con delle aggiunte
    def __init__(self, nome, eta:int, sesso, altezza:int):
        super().__init__(nome, eta)
        self.sesso = sesso
        self.altezza = altezza
        
    #definisco il mnetodo toString personalizzato
    def __str__(self):
        return f"La giraffa {self.nome}, ha {self.eta} anni, è {self.sesso} e raggiunge l'altezza di {self.altezza} metri"
    
    #sovrascrizione del metodo della classe Animale fai_suono
    def fai_suono(self):
        print("Landito")
        
    #metodo di classe   
    def cibo(self, albero):
        print(f"La giraffa sta mangiando le foglie da un {albero}")

#classe Pinguino figlio della classe Animale
class Pinguino(Animale):
    #creo gli attributi iniziali con delle aggiunte
    def __init__(self, nome, eta:int, sesso):
        super().__init__(nome, eta)
        self.sesso = sesso
        
    #definisco il mnetodo toString personalizzato
    def __str__(self):
        return f"Il pinguino {self.nome}, ha {self.eta} anni ed è {self.sesso}"
    
    #sovrascrizione del metodo della classe Animale fai_suono
    def fai_suono(self):
        print("Raglio")
    
    #metodo di classe   
    def nuoto(self):
        print("Il pinguino sta nuotando")
 
#TEST       
leone = Leone("Leon", 4, "maschio")

print(leone)

leone.fai_suono()

leone.caccia("cervo")

giraffa = Giraffa("Gir", 7, "femmina", 5)

print(giraffa)

giraffa.fai_suono()

giraffa.cibo("acacia")

pinguino = Pinguino("Pingu", 2, "maschio")

print(pinguino)

pinguino.fai_suono()

pinguino.nuoto()

