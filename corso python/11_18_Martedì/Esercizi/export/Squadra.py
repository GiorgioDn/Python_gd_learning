import MembroSquadra

class Giocatore(MembroSquadra):
    #ridefinisco gli attributi iniziali
    def __init__(self, nome:str, eta:int, ruolo:str, numero_maglia:int):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    #sovrascrivo il metodo toString della superClasse
    def __str__(self):
        return f"Il giocatore {self.nome} di {self.eta} anni, giocherà nel ruolo di {self.ruolo}, con il numero maglia {self.numero_maglia}"

    #da errore sugli argomenti
    def gioca_partita(self, action:str):
        match action.lower():
            case "tiro":
                print("Il giocatore tira in porta")
            case "para":
                print("Il giocatore para")
            case "passa":
                print("Il giocatore passa al suo compagno")
            case _:
                print(f"Il giocatore fa {action}")

class Allenatore(MembroSquadra):
    #ridefinisco gli attributi iniziali
    def __init__(self, nome:str, eta:int, anni_esperienza:int):
        super().__init__(nome, eta)
        self.anni_esperienza = anni_esperienza
        
    #sovrascrivo il metodo toString della superClasse
    def __str__(self):
        return f"L'allenatore {self.nome} di {self.eta} anni, con alle spalle {self.anni_esperienza} anni di esperienza"

class Assistente(MembroSquadra):
    #ridefinisco gli attributi iniziali
    def __init__(self, nome:str, eta:int, specializzazione:str):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
    
    #sovrascrivo il metodo toString della superClasse
    def __str__(self):
        return f"L'assistente {self.nome} di {self.eta} anni, è un {self.specializzazione}"
    
    def supporta_team(self):
        match self.specializzazione:
            case "fisioterapista":
                print(f"{self.nome} supporta la squadra assicurandosi che siano tutti in salute")
            case "analista di gioco":
                print(f"{self.nome} supporta la squadra assicurandosi che siano tutti giochino bene")
    

giocatore = Giocatore("ciao", 10, "cia", 10)

print(giocatore)