from export.Libro import Libro
from export.Libreria import Libreria

catalogo ={}

libro_1 = Libro("me", "dfjssf", 12334423232)

print(libro_1)

libro_2 = Libro("me22121", "dfjsdasdsf", 12333423232)

catalogo[libro_1.isbn] = [libro_1.titolo, libro_1.autore]

libreria = Libreria(catalogo)

print(libreria)