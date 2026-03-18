#definisco la classe Libro
class Libro: 
    #metodo costruttore con titolo, autore, pagine
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    #metodo per modificare il risultato del print con la classe
    def __str__(self):
        return f"Il libro {self.titolo} è stato scritto da: {self.autore} ed ha {self.pagine} pagine"

#definisco la classe Biblioteca
class Biblioteca: 

    def __init__(self):
        self.list_libri = []
        
    def aggiungi_libro(self, titolo, autore, pagine):
        libro = Libro(titolo, autore, pagine)
        self.list_libri.append([titolo, autore, pagine])
        print(libro)
    def __str__(self):
        return f"La biblioteca ha i seguenti libri: {self.list_libri}"
    
biblioteca = Biblioteca()

while True: 
    #inserisco i dati per istanziare la classe
    print("Dire l'autore del libro, il titolo e le pagine del libro da aggiungere in biblioteca")
    titolo = input("Titolo ")
    autore = input("Autore ")
    pagine = int(input("Pagine "))
     
    biblioteca = biblioteca.aggiungi_libro(titolo, autore, pagine)
    
    print(biblioteca)

    chooice = input("Si vuole ripetere la scelta? ")
    
    #si esce dal ciclo while
    if chooice.lower() == "no":
        break