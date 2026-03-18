from .Emplyee import *
from .RoleEmplyee import *

#polimorfismo
class Azienda:
    #prende come unico parametro obbligatorio una stringa
    def __init__(self, nome:str, dipendenti:list[Dipendente] = [], dipatrimenti:list[str] = []):
        self.__nome = nome
        self.__dipendenti = dipendenti
        self.__dipartimenti = dipatrimenti
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome:str):
        self.__nome = nome
        
    def aggiungi_dipendente(self, dipendente:Dipendente):
        self.__dipendenti.append(dipendente)
        
    def aggiungi_dipartimento(self, dipartimento:str):
        self.__dipartimenti.append(dipartimento)
        
    def rimuovi_dipendente(self, badge:str):
        for n in self.__dipendenti:
            for info in n.get_badge():
                if info.lower() == badge.lower():
                    self.__dipendenti.remove(n)
    
    def rimuovi_dipartimento(self, dipartimento:str):
        for n in self.__dipartimenti:
            if n.lower() == dipartimento:
                self.__dipartimenti.remove(n)
          
    #stampa un messaggio in base al tipo di impiegati contenuti nella lista dipendenti      
    def mostra_dipendenti(self):
        for n in self.__dipendenti:
            if type(n) == Impiegato:
                print(f"L'impiegato {n.get_badge()} ha i seguenti turni: {n.get_orari_turni}")
            elif type(n) == Amministratore:
                print(f"L'amministratore {n.get_badge()} ha i seguenti turni: {n.get_orari_turni} e gestisce il dipartimento {n.get_dipartimento()}")
            elif type(n) == Direttore:
                print(f"Il direttore {n.get_badge()} ha i seguenti turni: {n.get_orari_turni} e gestisce i dipartimenti {n.get_list_dipartimenti()}")
            else:
                print("Sconosciuto")