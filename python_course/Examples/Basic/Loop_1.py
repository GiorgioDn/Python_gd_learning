conteggio = 0

#inizializzo un ciclo while che viene eseguito finchè la condizione non è soddisfatta
#ciclo matematico
while conteggio < 5:
    print(conteggio)
    conteggio += 1
    
controllor = True

#ciclo booleano
while controllor:
    print(controllor)
    scelta = input("Vuoi continuare? ")
    if scelta.lower() == "no":
        controllor = False
    else:
        print("Stai continuando ")
        
numeri = [1, 2, 3, 4, 5]

#ciclo for 
for numero in numeri:
    print(numero)
    
#vado a capo per distinguere meglio i cicli for
print("\n")
    
#ciclo for con range solo stop
for i in range(5):
    print(i)

print("\n")

#ciclo for con range start e stop
for i in range(2, 8):
    print(i)

print("\n")

#ciclo for con range start e stop e step
for i in range(2, 10, 2):
    print(i)

print("\n")