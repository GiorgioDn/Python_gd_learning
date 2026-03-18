import random

#definisco la funzione che randomizza dato un certo intervallo
def randomNum (min, max):
    ran = random.randint(min, max)
    return ran

#definisco la funzione che confronta il numero randomico con le risposte dell'utente
def guess (casual):
    while True:
        answer = int(input("Provare ad indovinare il numero casule nell'intervallo: "))
        if answer<casual:
            print("Il numero selezionato è minore rispetto a quello giusto")
        elif answer>casual:
            print("Il numero selezionato è maggiore rispetto a quello giusto")
        else: 
            break
    
    return True
        
#seleziono il massimo e minimo per la randomizzazione
print("Selezionare numero minimo e massimo per l'intervallo randomico")
min = int(input("Minimo: "))
max = int(input("Massimo: "))

#genero il numero casuale
casual = randomNum(min, max)
#provo ad indovinare il numero
guess = guess(casual)
if guess == True:
    print("Complimenti hai indovinato")