class Elettrodomestico:
    #prende in input due stringhe un int ed un'altra stringa
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto

    #gettter
    def get_marca(self):
        return self.__marca

    #setter
    def set_marca(self, value:str):
        self.__marca = value

    #gettter
    def get_modello(self):
        return self.__modello

    #setter
    def set_modello(self, value:str):
        self.__modello = value

    #gettter
    def get_anno_acquisto(self):
        if self.__anno_acquisto <= 2025:
            return self.__anno_acquisto
        else:
            return False

    #setter
    def set_anno_acquisto(self, value:int):
        self.__anno_acquisto = value

    #gettter
    def get_guasto(self):
        return self.__guasto

    #setter
    def set_guasto(self, value:str):
        self.__guasto = value
    
    #ritorna una stringa descrittiva della classe
    def description(self):
        return f"{self.__marca}, {self.__modello} prodotta nell'anno {self.__anno_acquisto} con il seguente problema: {self.__guasto}"

    #restituisce un valore float
    def stima_costo_base(self):
        costo_base = 10.0
        return costo_base