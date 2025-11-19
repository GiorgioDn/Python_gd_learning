from export.Studente import Studente
from export.Professore import Professore

while True:
    
    voti = []
    
    print("Digitare il nome dello studente e l'età")
    nome = input("Nome: ")
    eta = int(input("Eta: "))
    
    while True:
        print("Inserire il voto dello studente: ")
        voto = int(input("Voto: "))
        
        voti.append(voto)
        
        chooice = input("Si vuole inserire un altro voto?")
    
        if chooice.lower() == "no":
            break
        
    studente = Studente(nome, eta, voti)
    
    if studente.get_nome() == False or studente.get_eta() == False:
        if studente.get_nome() == False:
            nome = input("nome non valido digitare un nuovo nome: ")
            studente.set_nome(nome)
        else:
            eta = int(input("eta non valido digitare un nuovo eta: "))
            studente.set_eta(eta)
    
    #vedere perchè mi setta a non i parametri        
    print(studente.presentazione())
        
    print("Digitare il nome, l'età, la materia del professore")
    nome = input("Nome: ")
    eta = int(input("Eta: "))
    materia = input("Materia: ")
    
    professore = Professore(nome, eta, materia)
    
    if professore.get_nome() == False or professore.get_eta() == False or professore.get_materia == False:
        if professore.get_nome() == False:
            nome = input("nome non valido digitare un nuovo nome: ")
            professore.set_nome(nome)
        elif professore.get_materia() == False:
            materia = input("materia non valido digitare un nuovo materia: ")
            professore.set_materia(materia)
        else:
            eta = int(input("eta non valido digitare un nuovo eta: "))
            professore.set_eta(eta)
    
    print(professore.presentazione())
    
    chooice = int(input("Selezionare cosa fare con lo studente: \n1. Aggiungere voto\n2. Calcolo media"))
    
    match chooice:
        case 1:
            voto = int(input("Aggiungere il voto: "))
            studente.add_voto(voto)
            print(f"I voti dello studente sono: {studente.get_voti()}")
        case 2: 
            average = studente.calcola_media()
            print(f"La media dello studente è {average}")
        case _:
            print("Scelta non valida")
    
    chooice = input("Si vuole effettuare una nuova prova?")
    
    if chooice.lower() == "no":
        break