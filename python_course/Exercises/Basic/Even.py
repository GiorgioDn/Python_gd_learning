#definisco la lista che conterrà i numeri pari
pair =[]

#verifico se il numero è pari
while len(pair)<6:
    #chiedo all'utente il numero da inserire
    num = int(input("Inserire un numero positivo: "))
    
    if num%2 == 0:
        print("il numero è pari")
        pair.append(num)
    else:
        print("il numero è dispari")
    
print("5 numeri pari trovati")