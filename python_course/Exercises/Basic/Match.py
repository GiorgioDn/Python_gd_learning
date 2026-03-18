#utente di verifica
verify_user = ["admin", "12345"]

#lista che conterrà i dati utente
entry_user = []

#richiesta per l'username
username = input("Inserire il nome utente: ")
entry_user.append(username)

#richiesta per la password
password = input("Inserire la password: ")
entry_user.append(password)

#verifico che il file utente e la password siano corretti
if entry_user[0] == verify_user[0] and entry_user[1] == verify_user[1]:
    print("Benvenuto")
    secret = []

    answer = input("Qual'è il tuo animale preferito: ")
    secret.append(answer)
else:
    print("Credenziali errate")
    

