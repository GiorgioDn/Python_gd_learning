from abc import ABC, abstractmethod

#classe astratta
class Animale(ABC):
    #il pass è facoltivo
    #il metodo astratto deve essere per forza sovrascritto dalle classi figlie
    @abstractmethod
    def muovi(self):
        pass
    
class Cane(Animale):
    def muovi(self):
        print("Corro")
    
class Pesce(Animale):
    def muovi(self):
        print("Nuoto")

cane = Cane()
cane.muovi()

pesce = Pesce()
pesce.muovi()

#classe astratta con metodi astratti e concreti
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass 
    
    @abstractmethod
    def perimetro(self):
        pass
    
class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza
        
    def area(self):
        return self.larghezza * self.altezza
    
    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)
    
# f = Forma() #TypeError perchè non si può inizializzare

r = Rettangolo(5, 10)
print(r.area())
print(r.perimetro())
        