# definisco la lista che conterrà i numeri primi
prime = []

# ciclo finché non trovo 5 numeri primi
while len(prime) < 5:
    num = int(input("Inserire un numero positivo: "))

    if num < 2:
        print("Numero non valido o non primo")
    else:
        # verifichiamo se num è primo o no
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Il numero non è primo")
                break
        else:
            # se il ciclo non si interrompe con break significa che è un numero primo
            print("Il numero è primo")
            prime.append(num)

print("Sono stati trovati 5 numeri primi:", prime)
