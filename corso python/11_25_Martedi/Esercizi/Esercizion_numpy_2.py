import numpy as np

def main():
    
    rand_id = str(np.random.randint(0, 100, 10))
    txt = "corso python/11_25_Martedi/Esercizi/export/dati_1.txt"
    
    chooice = input("Si vuole scrivere un file txt con i dati? si/no: ")
    if chooice.lower() == "si":
        while True:

            #legge la prima riga
            file = open(txt, "r")
            riga = file.readline().strip()
            file.close()
            #sovrascrive il file se non è presente lo stesso id
            if riga != rand_id:
                string = f"{rand_id}\n"  
                file = open (txt, "w")
                file.write(string)
                file.close()
            
            arr_lin = np.linspace(0, 10, 50)
            
            arr_rand = np.random.random(50)
            

            sum_arr = np.add(arr_lin, arr_rand)

            sum_tot = sum_arr.sum()

            new_sum = sum_arr[sum_arr > 5].sum()

            print(arr_lin, arr_rand, sum_arr, sum_tot, new_sum)
  
                    
            with open (txt, "a") as file:
                string = f"Array con linspace: {arr_lin} \nArray random: {arr_rand} \nSomma array: {sum_arr} \nSomma elementi array somma: {sum_tot} \nSomma elementi maggiori di 5: {new_sum}\n"
                file.write(string)

            chooice = input("Si vogliono inserire altri dati? si/no: ")
            if chooice.lower() == "no":
                break
            
            chooice = input("Si vvuole sovrascrivere il file? si/no: ")
            if chooice.lower() == "si":
                rand_id = str(np.random.randint(0, 100, 10))
            
            
if __name__ == "__main__":
    main()
else: 
    print("È stato importato")