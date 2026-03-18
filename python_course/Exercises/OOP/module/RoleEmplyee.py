from .Emplyee import Dipendente

#ereditarietà e polimorfismo
class Impiegato(Dipendente):
    #non espande l'init della classe astratta
    def __init__(self, badge:list[str], orari_turni:list[float]):
        super().__init__(badge, orari_turni)
    
    #sovrascrive il metodo astratto 
    def controllo_accesso(self, ora:float):
        if ora in self.get_orari_turni():
            return f"Accesso consentito"
        else:
            return f"Accesso non consentito"

class Amministratore(Dipendente):
    #prende i parametri della classe astratta e ci aggiunge un parametro stringa
    def __init__(self, badge:list[str], orari_turni:list[float], dipartimento:str):
        super().__init__(badge, orari_turni)
        self.__dipartimento = dipartimento
    
    def get_dipartimento(self):
        return self.__dipartimento
    
    def set_dipartimento(self, dipartimento:str):
        self.__dipartimento = dipartimento
    
    #sovrascrive il metodo astratto 
    def controllo_accesso(self, ora:float, dipartimento:str):
        if ora in self.get_orari_turni() and self.__dipartimento.lower() == dipartimento.lower():
            return f"Accesso consentito"
        else:
            return f"Accesso non consentito"

class Direttore(Dipendente):
    #prende i parametri della classe astratta e ci aggiunge un parametro lista di stringhe in overloading simulato
    def __init__(self, badge:list[str], orari_turni:list[float], list_dipartimenti:list[str] = []):
        super().__init__(badge, orari_turni)
        self.__list_dipartimenti = list_dipartimenti
        
    def get_list_dipartimenti(self):
        return self.__list_dipartimenti
    
    def aggiungere_list_dipartimenti(self, dipartimento:str):
        self.__list_dipartimenti.append(dipartimento.lower())
    
    #sovrascrive il metodo astratto     
    def controllo_accesso(self, ora:float, dipartimento:str):
        if ora in self.get_orari_turni() and dipartimento.lower() in self.__list_dipartimenti:
            return f"Accesso consentito"
        else:
            return f"Accesso non consentito"
