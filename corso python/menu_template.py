while True:
    
    print("")
    
    chooice = int(input("Selezionare: \n1. \n2. \n3. \n4. \n5."))
    
    match chooice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            print("Scelta non valida")
    
    chooice = input("Si vuole effettuare una nuova prova?")
    
    if chooice.lower() == "no":
        break