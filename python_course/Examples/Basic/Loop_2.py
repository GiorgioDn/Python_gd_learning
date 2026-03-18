numeri = [1, 2, 3, 4, 5]

#break fa terminare il ciclo
#conntinue salta l'interazione, ma poi continua con la successiva
for numero in numeri:
    if numero == 2:
        continue
    elif numero == 4:
        break
    else:
        print(numero)
    
print("\nRisultati pass:")
#pass non esegue alcuna azione
for i in range(5):
    if i == 3:
        pass
    print(i)

print("\nRisultati operatore splat:")    
#splat: * prima della variabile iterabile per espanderla 
numeri = [*range(1, 11)]
print(numeri)