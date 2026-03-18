#variabile di input per far selezionare il tipo di operazione e la parola iniziale
start = input("Scrivere una parola: ")
cond = input("Scrivere il tipo di operazione voluta per la parola iniziale tra: aggiungi, aggiorna ed elimina: ")
cond.lower()

#condizioni dati dall'input
if cond == "aggiungi":
    cond = input("Scrivere la parola da aggiungere: ")
    print("La nuova frase è:", start, cond)
elif cond == "aggiorna":
    cond = input("Scrivere con che parola sostituire: ")
    start = cond
    print("La nuova parola è:", start)
elif cond == "elimina": 
    start = ""
    print("La parola è stata eliminata", start)
else: 
    print("Operazione non valida")