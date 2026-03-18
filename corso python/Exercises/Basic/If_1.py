#inizializzo la variabile età di tipo int che verrà scelta dall'utente
eta = int(input("Scrivere la propria età: "))

#confronto l'età
if eta>=18 and eta<105:
    print("Puoi vedere questo film")
elif eta<0 or eta>105:
    print("Età non valida")
else:
    print("Mi dispiace, non puoi vedere questo film")