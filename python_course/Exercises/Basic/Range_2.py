# definisco la lista che conterrà i numeri primi e non 
prime = []
non_prime = []

while True:
    #Scelta dell'intervallo di numeri
    print("Scegliere un intervallo di due numeri ")
    num1 = int(input("Primo numero: "))
    num2 = int(input("Secondo numero: "))
    
    #creo la lista compreso con num2
    numeri = [*range(num1, num2 + 1)]
    
    print(numeri)

    # verifichiamo se i numeri sono primi o no
    for n in numeri:
        if n < 2:
            non_prime.append(n)
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    non_prime.append(n)
                    break
            else:
                prime.append(n)
    
    #stampo i numeri primi e non primi
    print("Numeri primi nell'intervallo:", prime)
    print("Numeri non primi nell'intervallo:", non_prime)

    #si esce dal ciclo while
    choice = input("Vuoi ripetere la scelta? (sì o no): ")
    if choice.lower() == "no":
        break