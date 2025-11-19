#classe computer con metodo privato
class Computer:
    #l'attributo processore è privato
    def __init__(self, nome_proc):
        self.__processore = nome_proc

    #accedo all'attributo tramite il metodo get
    def get_processore(self):
        return self.__processore

    #modifico l'attributo tramite il metodo set
    def set_processore(self, processore):
        self.__processore = processore
    
    #metodo privato 
    def __metodo_privato(self):
        return "Questo è un metodo privato"
    
    #metodo pubblico per accedere al metodo privato
    def metodo_pubblico(self):
        return self.__metodo_privato()


pc = Computer("Intel i5")
print(pc.get_processore()) 

#accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5") 

#modifica l'attributo privato tramite il setter
print(pc.get_processore())

#da evitare anche per motivi di sicurezza
print(pc._Computer__processore)

print(pc.metodo_pubblico())

print("\n")

#variabile globale
numero = 10

def funzione_esterna():
    #variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna (locale):", numero)    

    def funzione_interna():
        #utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3

        print("Numero dentro funzione_interna (nonlocal):", numero)

    funzione_interna()

print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)

#classe con variabile protetta
class ClasseBase:
    def __init__(self):
        self._variabile_protetta = "Sono protetta"


class SottoClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        #la variabile viene ereditata dalla classe figlio
        print(self._variabile_protetta)


obj = SottoClasse()
#da evitare anche per motivi di sicurezza
print(obj._variabile_protetta)