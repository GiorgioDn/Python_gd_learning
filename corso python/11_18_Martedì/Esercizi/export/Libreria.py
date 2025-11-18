#classe Libreria che prende come argomenti iniziali una lista di libri 
class Libreria:
    def __init__(self, catalogo):
        self.catalogo = catalogo
    #metodo per stampare con il print il catalogo
    def __str__(self):
        catalogo = f"I libri presenti nel catalogo sono: {self.catalogo}"
        return catalogo
    #metodo per aggiungere un libro dato come argomento del metodo 
    def aggiungi_libro(self, libro):
        self.catalogo.append([libro.titolo, libro.autore, libro.isbn])
    #metodo per rimuovere un libro dato come argomento del metodo 
    def rimuovi_libro(self, libro):
        isbn = libro.isbn
        index = 0
        for n in self.catalogo:
            if isbn == n[2]:
                self.catalogo.pop(index)
            else:
                index +=1
    #metodo per cercare un libro dato come argomento del metodo 
    def cerca_per_titolo(self, libro):
        titolo = libro.titolo
        list_search = []
        for n in self.catalogo:
            if n[0] == libro.titolo:
                list_search.append([libro.titolo, libro.autore, libro.isbn])
        return list_search
    