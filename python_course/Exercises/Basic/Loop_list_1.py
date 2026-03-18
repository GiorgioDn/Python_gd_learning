#Inizializzo la lista
list_num = []

#faccio selezionare all'utente 5 numeri da aggiungere alla lista
while len(list_num)<6:
    list_num.append(float(input("Digitare un numero: ")))

#stampo il quadrato di ogni numero nella lista
for n in list_num:
    n = n**2
    print(n)