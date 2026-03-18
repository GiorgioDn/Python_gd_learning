#classe Libro che richiede titolo, autore, isbn
class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    #Il metodo che sovrascrive il print per stampare con il print la descrizione
    def __str__(self):
        description = f"Il libro {self.titolo}, scritto da {self.autore}, ha il seguente codice isbn: {self.isbn}"
        return description