#input dei dati dei dizionari
boolean = input("Inserisci un valore booleano: ")
integer = int(input("Inserisci un intero: "))
string = input("Inserisci la stringa: ")

#dizionario con i valori in input
diz = {
    "boolean": boolean,
    "integer": integer,
    "string": string,
}

#lista di dizionari
list_diz = [diz]

#dizionario con lista
date = {
    
    "tipodato": [boolean, integer, string],
    "dizionario": list_diz
    
}

#visualizzazione chiavi e valori
for x, y in diz.items():
    print("chiave: ", x)
    print("valore: ", y)