#lista contenente i numeri da sommare
sum_num=[]

while True:
    print("Scegliere dei numeri interi, per terminare la scelta scegliere il numero 0")
    
    #variabile per dare una scelta infinita all'utente di numeri
    end_number = 1
    #aggiorno la lista con ogni numero finchè non viene scelto lo 0
    while end_number !=0:
        num = int (input("Scegliere il numero: "))
        sum_num.append(num)
        end_number = num
    
    #quando il numero finale è 0 sommo i numeri
    if end_number == 0:
        sum = 0
        n = 0
        while n<len(sum_num):
            sum += sum_num[n]
            n+=1 
        #stampo ed esco dal while
        print("La somma dei numeri è:", sum)
        break