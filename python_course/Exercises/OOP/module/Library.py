#classe Libreria che prende come argomenti iniziali un dizionario di libri 
class Libreria:
    def __init__(self, catalogo):
        self.catalogo = catalogo
    #metodo per stampare con il print il catalogo
    def __str__(self):
        catalogo = f"I libri presenti nel catalogo sono: {self.catalogo}"
        return catalogo
    #metodo per aggiungere un libro dato come argomento del metodo 
    def aggiungi_libro(self, libro):
        isbn = libro.isbn
        self.catalogo[isbn] = [libro.titolo, libro.autore]
    #metodo per rimuovere un libro dato come argomento del metodo 
    def rimuovi_libro(self, libro):
        isbn = libro.isbn
        if isbn in self.catalogo:
            del self.catalogo[isbn]
        else:
            return False
    #metodo per cercare un libro dato come argomento del metodo 
    def cerca_per_titolo(self, titolo):
        list_search = []
        index = 0
        for n in self.catalogo.values():
            if n[0] == titolo or n[1] == titolo:
                list_search.append(self.catalogo.items()[index])
            else:
                index += 1
        return list_search
    