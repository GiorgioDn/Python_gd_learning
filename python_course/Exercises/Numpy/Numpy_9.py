import numpy as np

def main():
    
    rand_id = str(np.random.randint(0, 100, 10))
    txt = "python_course/Exercises/Numpy/export/data_1.txt"
    
    choice = input("Do you want to write a txt file with data? yes/no: ")
    if choice.lower() == "yes":
        while True:

            # reads the first line
            file = open(txt, "r")
            line = file.readline().strip()
            file.close()
            # overwrites the file if the same ID is not present
            if line != rand_id:
                string = f"{rand_id}\n"  
                file = open (txt, "w")
                file.write(string)
                file.close()
            
            arr_lin = np.linspace(0, 10, 50)
            
            arr_rand = np.random.random(50)
            

            sum_arr = np.add(arr_lin, arr_rand)

            sum_tot = sum_arr.sum()

            new_sum = sum_arr[sum_arr > 5].sum()
            
            # string for data visualization
            string = f"Array with linspace: {arr_lin} \nRandom array: {arr_rand} \nArray sum: {sum_arr} \nSum of sum array elements: {sum_tot} \nSum of elements greater than 5: {new_sum}\n"

            print(string)
                
            # add new data to the file
            with open (txt, "a") as file:
                file.write(string)

            choice = input("Do you want to enter more data? yes/no: ")
            if choice.lower() == "no":
                break
            
            choice = input("Do you want to overwrite the file? yes/no: ")
            if choice.lower() == "yes":
                rand_id = str(np.random.randint(0, 100, 10))
            
            
if __name__ == "__main__":
    main()
else: 
    print("Module imported")