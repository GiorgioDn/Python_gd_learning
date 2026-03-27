from Import.Import_1 import Sell

while True: 
    
    sell_data = []
    
    print("Enter sales amounts")
    
    while True:
        data = input("Amount: ")
        sell_data.append(data)
        
        choice = input("Do you want to select another amount? ")
    
        #exit the while loop
        if choice.lower() == "no":
            break
        
    sell = Sell(sell_data)
    
    x = sell.total_sell()
    
    print(x)
    
    choice = input("Do you want to repeat the choice? ")
    
    #exit the while loop
    if choice.lower() == "no":
        break