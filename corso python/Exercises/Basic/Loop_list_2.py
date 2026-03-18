#Inizializzo la lista
list_num = [3, 4, 6, 7, 8, 10]

#controllo se la lista non sia vuota
if len(list_num) > 0:
       
    #inizializzo il valore massimo 
    max = list_num[0]
    
    #trovo il massimo
    for n in list_num:
        if n > max:
            max = n
        
    print(max, "\n")

    #iniializzo le variabili per contare con il while
    list_len = len(list_num)
    n=0 
    
    #conto i numeri presenti nella lista con il while
    while n<list_len:
        print(list_num[n])
        n += 1
    
    #stampo i numeri nella lista
    print(n)
    
else:
    print("Lista vuota")