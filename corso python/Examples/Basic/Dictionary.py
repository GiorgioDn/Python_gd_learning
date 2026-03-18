#creo un dizionario associandolo ad una variabile
studente = {
    "nome": "Alice",
    "eta": 20,
    "sesso": "femmina",
}

#restituisco i dati del dizionario
print(studente["nome"])
print(studente["eta"])

#modifica del valore eta
studente["eta"] = 21
print(studente)

#aggiungere un elemento
studente["citta"] = "Roma"
print(studente)

#stampo solo le chiavi
print(studente.keys())

#stampo solo i valori
print(studente.values())

#stampa la lista delle coppie chiave valore
print(studente.items())

#stampa il valore associato ad una chiave
print(studente.get("nome"))

