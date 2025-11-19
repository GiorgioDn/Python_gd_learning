class Veicolo:
    def __init__(self, marca:str, modello:str, anno:int, accensione:bool):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = accensione
    
    #metodi get per prendere i valori
    def get_marca(self):
        if len(self.__marca) > 0:
            return self.__marca
        else:
            return False
        
    def get_modello(self):
        if len(self.__modello) > 0:
            return self.__modello
        else:
            return False
    
    def get_anno(self):
        if self.__anno > 0:
            return self.__anno
        else:
            return False
        
    def get_accensione(self):
        return self.__accensione
    
    #metodi set per modificare i valori
    def set_marca(self, marca:str):
        if len(self.__marca) > 0:
            self.__marca = marca
        else:
            return False
        
    def set_modello(self, modello:str):
        if len(self.__modello) > 0:
            self.__modello = modello
        else:
            return False
    
    def set_anno(self, anno:int):
        if self.__anno > 0:
            self.__anno = anno
        else:
            return False
        
    #metodi per l'accensione e lo spegnimento
    def accendi(self):
        self.__accensione = True
        
    def spegni(self):
        self.__accensione = False