#non riesce ad esportare (?)
from .module.Squad import *

while True:
    
    print("Digitare il nome del giocatore, l'età, il ruolo ed il numero della maglia")
    nome = input("Nome: ")
    eta = int(input("Età: "))
    ruolo = input("Ruolo: ")
    numero_maglia = int(input("Numero maglia: "))
    
    giocatore = Giocatore(nome, eta, ruolo, numero_maglia)
    
    print(giocatore)
    
    action = input("Scrivere l'azione tra: tira, para o passa  ")
    
    giocatore.gioca_partita(action)
    
    print("Digitare il nome dell'allenatore, l'età e gli anni esperienza")
    nome = input("Nome: ")
    eta = int(input("Età: "))
    anni = input("Anni esperienza: ")
    
    allenatore = Allenatore(nome, eta, anni)
    
    print(allenatore)
    
    print("Digitare il nome dell'assistente, l'età e la specializzazione tra: fisioterapista ed analista di gioco")
    nome = input("Nome: ")
    eta = int(input("Età: "))
    specializzazione = input("fisioterapista o analista di gioco: ")
    
    assistente = Assistente(nome, eta, specializzazione)
    
    print(assistente)
    
    assistente.supporta_team()
    
    chooice = input("Si vuole ripetere la scelta? ")
    
    #si esce dal ciclo while
    if chooice.lower() == "no":
        break