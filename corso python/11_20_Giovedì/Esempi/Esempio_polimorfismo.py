#polimorfimo con overriding
class Animale:

    def emetti_suono(self):
        print("Questo animale fa un suono")


class Cane(Animale):

    def emetti_suono(self):
        print("Bau")
    
    #usato per il polimorfismo passivo
    def parla(self):
        return "Bau!"


class Gatto(Animale):

    def emetti_suono(self):
        print("Miao")
    
    #usato per il polimorfismo passivo
    def parla(self):
        return "Miao!"
        
animale = Animale()
animale.emetti_suono()

cane = Cane()
cane.emetti_suono()

gatto = Gatto()
gatto.emetti_suono()

        
#Simulazione overloading
class Stampa:

    #argomenti opzionali o variadici con cui simulare l'overloading
    def mostra(self, a=None, b=None):
        if a is not None and b is not None:
            print(a + b)

        elif a is not None:
            print(a)

        else:
            print("Niente da mostrare")
            
stampa = Stampa()
stampa.mostra()
stampa.mostra(1)
stampa.mostra(1, 2)

#Polimorfismo passivo: duck typing con funzione che usa il metodo polimorfico
def fai_parlare(animale):
    print(animale.parla())

fai_parlare(cane) 
fai_parlare(gatto) 

#duck typing con ciclo polimorfico (duck typing)
class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")


class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")


def disegna_figura(figura):
    #basta che esista disegna
    figura.disegna()


figure = [Cerchio(), Rettangolo()]

#si itera ogni figura
for figura in figure:
    disegna_figura(figura)