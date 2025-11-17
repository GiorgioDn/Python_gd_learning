#dichiarazione della classe Automobile
class Automobile:
    #attributo della classe
    numero_di_ruote = 4
    #metodo costruttore
    def __init__(self, marca, modello):
        #attributi di istanza
        self.marca = marca
        self.modello = modello
    #metodo speciale
    def __str__(self):
        #si usa nel print della classe
        return f"Automobile marca = {self.marca}, modello = {self.modello}"
    #metodo di istanza
    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello)
        
#creazione due oggetti di tipo Automobile
auto1 = Automobile("Fiat", "500")    
auto2 = Automobile("BMW", "X3")

#richiamo del metodo di istanza
auto1.stampa_info()            
auto2.stampa_info()

#stampa indirizzo di memoria o il metodo speciale __str__ se definito
print(auto1)

#dichiarazione della classe Persona
class Persona: 
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    #metodo
    def saluta(self):
        print(f"Ciao mi chiamo {self.nome}")
    
#Creazione di un oggetto di tipo Persona
p = Persona("Pippo", 30)

#Stampo i singoli attributi di istanza associati all'oggetto
print(p.nome)
print(p.eta)
#uso il metodo 
p.saluta()

#classe con metodo statico
class Calcolatrice:
    
    #metodo statico
    @staticmethod
    def somma(a, b):
        return a + b


#Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato)  

#classe con metodo di classe
class Contatore: 
    #attributo di classe
    numero_istanze = 0
    
    def __init__(self):
        Contatore.numero_istanze += 1

    #metodo di classe: cls indica la classe
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

#creo due istanze di classe   
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()