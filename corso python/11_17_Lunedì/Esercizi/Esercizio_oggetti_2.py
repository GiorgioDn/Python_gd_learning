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

while True: 
    #inserisco i dati per istanziare la classe
    print("Dire l'autore del libro, il titolo e le pagine")
    titolo = input("Titolo ")
    autore = input("Autore ")
    pagine = int(input("Pagine "))
    
    libro = Libro(titolo, autore, pagine)
    
    #uso il metodo __str__
    print(Libro)

    chooice = input("Si vuole ripetere la scelta? ")
    
    #si esce dal ciclo while
    if chooice.lower() == "no":
        break