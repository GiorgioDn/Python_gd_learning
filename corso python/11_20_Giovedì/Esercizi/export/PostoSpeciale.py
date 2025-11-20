from .Posto import Posto

class PostoStandard(Posto):
    #definisco la classe posto con parametri ereditati dalla classe Posto ed in aggiunta un float
    def __init__(self, numero:int, fila:str, costo:float):
        super().__init__(numero, fila)
        self.__costo = costo
    
    def get_costo(self):
        return self.__costo
    
    #sovrascrivo il metodo di prenotazione
    def prenota(self):
        base = super().prenota()
        if super().get_occupato() == False:
            return f"{base} al costo di {self.__costo}"
        else:
            return base

class PostoVIP(Posto):
    #definisco la classe posto con parametri ereditati dalla classe Posto ed in aggiunta un float ed una lista di scringhe
    def __init__(self, numero:int, fila:str, costo:float, servizi_extra:list[str]):
        super().__init__(numero, fila)
        self.__costo = costo
        self.__servizi_extra = servizi_extra
        
    def get_servizi_extra(self):
        return self.__servizi_extra
    
    #sovrascrivo il metodo di prenotazione
    def prenota(self):
        base = super().prenota()
        if super().get_occupato() == False:
            return f"{base} al costo di {self.__costo} con la possibilità di attivare i seguenti servizi: {self.__servizi_extra}"
        else:
            return base
    
        