class Persona:
    #prende in input una stringa ed un intero
    def __init__(self, nome:str, eta:int):
        self.__nome = self.set_nome(nome)
        self.__eta = self.set_eta(eta)
    
    #con i get accedo ai corrispettivi parametri
    def get_nome(self):
        return self.__nome
    
    def get_eta(self):
        return self.__eta
    
    #con i set modifico i parametri
    def set_nome(self, nome:str):
        if len(nome) > 0:
            self.__nome = nome
        else:
            return False
    
    def set_eta(self, eta:int):
        if eta > 0:
            self.__eta = eta
        else:
            return False
    
    #metodo di presentazione
    def presentazione(self):
        return f"{self.__nome}, ha {self.__eta} anni"