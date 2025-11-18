class UnitaMilitare:
    ritirata = False
    #prende in input un nome di tipo stringa ed il numero dei soldati di tipo intero
    def __init__(self, nome:str, numero_soldati:int):
        self.nome = nome
        self.numero_soldati = numero_soldati
    #metodo che prende in input una posizione
    def muovi(self, position:str):
        print(f"L'unità si è mossa fino a {position}")
    #metodo che prende in input un bersaglio
    def attacca(self, bersaglio:str):
        print(f"L'unità l'unità attacca {bersaglio}")
    def ritira(self):
        self.ritirata = True
        return self.ritirata