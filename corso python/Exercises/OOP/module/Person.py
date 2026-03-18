class Persona:
    #prende in input una stringa ed un intero
    def __init__(self, nome:str, eta:int):
        self.__nome = nome
        self.__eta = eta
    
    #con i get accedo ai corrispettivi parametri
    def get_nome(self):
        if len(self.__nome) > 0:
            return self.__nome
        else:
            return False
    
    def get_eta(self):
        if self.__eta > 0:
            return self.__eta
        else:
            return False
    
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