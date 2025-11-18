from export.Libro import Libro
from export.Libreria import Libreria

catalogo =[]

libro_1 = Libro("me", "dfjssf", 12334423232)

print(libro_1)

libro_2 = Libro("me22121", "dfjsdasdsf", 12333423232)

catalogo.append([libro_1.titolo, libro_1.autore, libro_1.isbn])

libreria = Libreria(catalogo)

print(libreria)

libreria.aggiungi_libro(libro_2)

print(libreria)

print(libreria.cerca_per_titolo(libro_2))

libreria.rimuovi_libro(libro_2)

print(libreria)