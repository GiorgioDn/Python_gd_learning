class MembroSquadra:
    #la classe prende il nome come stringa e l'età come intero
    def __init__(self, nome:str, eta:int):
        self.nome = nome
        self.eta = eta
    
    def __str__(self):
        return f"{self.nome} ha {self.eta} anni"
        