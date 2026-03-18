#numero di partenza
start = int(input("Inserire un numero: "))
repeat = True

if start<0:
    #ciclo while per stampare il numero ridotto di uno
    while repeat:
        for n in range(start, 1, +1):
            print(n)
        #chiedo all'utente se vuole continuare
        ask = input("Vuoi stampare di nuovo? ")
        if ask.lower() == "no":
            repeat = False
else:
    #ciclo while per stampare il numero ridotto di uno
    while repeat:
        for n in range(start, -1, -1):
            print(n)
        #chiedo all'utente se vuole continuare
        ask = input("Vuoi stampare di nuovo? ")
        if ask.lower() == "no":
            repeat = False