from .Appliance import Elettrodomestico

class Lavatrice(Elettrodomestico):
    #prende in input due stringhe un int una stringa e due int
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str, capacità_kg:int, giri_centrifuga:int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__capacità_kg = capacità_kg
        self.__giri_centrifuga = giri_centrifuga

    #getter
    def get_capacità_kg(self):
        return self.__capacità_kg

    def set_capacità_kg(self, value:int):
        self.__capacità_kg = value

    #getter
    def get_giri_centrifuga(self):
        return self.__giri_centrifuga

    def set_giri_centrifuga(self, value:int):
        self.__giri_centrifuga = value
    
    #override del metodo stima costo 
    def stima_costo_base(self):
        stima_costo = super().stima_costo_base
        if self.__capacità_kg >= 20:
            stima_costo += 5.0
            return stima_costo
        else:
            return stima_costo


class Frigorifero(Elettrodomestico):
    #prende in input due stringhe un int una stringa e un int ed un booleano
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str, litri:int, ha_freezer:bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer

    #getter
    def get_litri(self):
        return self.__litri

    def set_litri(self, value:int):
        self.__litri = value

    #getter
    def get_ha_freezer(self):
        return self.__ha_freezer

    def set_ha_freezer(self, value:bool):
        self.__ha_freezer = value
       
    #override del metodo stima costo  
    def stima_costo_base(self):
        stima_costo = super().stima_costo_base
        if self.__ha_freezer == True or self.__litri>5:
            stima_costo += 2.0
            return stima_costo
        
        elif self.__ha_freezer == True and self.__litri>5:
            stima_costo += 6.5
            return stima_costo
            
        else:
            return stima_costo


class Forno(Elettrodomestico):
    #prende in input due stringhe un int due stringhe ed un bool
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str, tipo_alimentazione:str, ha_ventilato:bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__tipo_alimentazione = tipo_alimentazione
        self.__ha_ventilato = ha_ventilato

    #getter
    def get_tipo_alimentazione(self):
        return self.__tipo_alimentazione

    def set_tipo_alimentazione(self, value:str):
        self.__tipo_alimentazione = value

    #getter
    def get_ha_ventilato(self):
        return self.__ha_ventilato

    def set_ha_ventilato(self, value:bool):
        self.__ha_ventilato = value

    #override del metodo stima costo  
    def stima_costo_base(self):
        stima_costo = super().stima_costo_base
        if self.__ha_vetilato == True or self.__tipo_alimentazione.lower() == "elettrico" or self.__tipo_alimentazione.lower() == "gas":
            stima_costo += 2.5
            return stima_costo
        
        elif self.__ha_vetilato == True and self.__tipo_alimentazione.lower() == "elettrico" or self.__tipo_alimentazione.lower() == "gas":
            stima_costo += 5.5
            return stima_costo
            
        else:
            return stima_costo