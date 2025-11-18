#creo la superclasse animale
class Animale:
    def __init__(self, nome:str, eta:int):
        self.nome = nome
        self.eta = eta

    def fai_suono(self):
        print("Verso animale")