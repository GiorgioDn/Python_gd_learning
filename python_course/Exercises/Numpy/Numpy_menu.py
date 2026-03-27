import numpy as np

def main():
    
    # user id creation
    rand_id = str(np.random.randint(0, 100, 10))
    txt = "python_course/Exercises/Numpy/export/data_2.txt"
    # creates or initializes the file if it already exists
    with open (txt, "w") as file:
        string = f"{rand_id}\n" 
        file.write(string)
    
    while True:
        
        # reads the first line
        file = open(txt, "r")
        line = file.readline().strip()
        file.close()
        # overwrites the file if the same id is not present
        if line != rand_id:
            string = f"{rand_id}\n"  
            file = open (txt, "w")
            file.write(string)
            file.close()
        
        print("\n Choose the operation to perform: ")
        print("1. Create a new 2D matrix")
        print("2. Extract and print the central sub-matrix")
        print("3. Transpose the matrix and print it")
        print("4. Calculate and print the sum of all matrix elements")
        print("5. Multiplication with another matrix")
        print("6. Mean of the matrix elements")
        print("7. Determinant of the matrix")
        print("8. Exit")
        choice = int(input("Choose an option: "))
        
        match choice:
            case 1:
                start = int(input("Select the starting value of the matrix: "))
                end = int(input("Select the final value of the matrix: "))
                row = int(input("Select the number of rows of the matrix: "))
                col = int(input("Select the number of columns of the matrix: "))
                
                matrix = np.random.randint(start, end, size=(row, col))
                string = f"2D Matrix: \n{matrix}\n"
                print(matrix)
                with open (txt, "a") as file:
                    file.write(string)
            case 2:
                
                # creation of the central sub-matrix
                sub_matrix = matrix[1: row-1, 1: col-1]
                string = f"Central sub-matrix: \n{sub_matrix}\n"
                print(sub_matrix)
                with open (txt, "a") as file:
                    file.write(string)
            case 3:
                
                # creation of the transposed matrix
                transpose_matrix = matrix.transpose()
                string = f"Transposed matrix: \n{transpose_matrix}\n"
                print(transpose_matrix)
                with open (txt, "a") as file:
                    file.write(string)
            case 4:
                
                # sum of the matrix elements
                total_sum = matrix.sum()
                string = f"Sum of the matrix elements: \n{total_sum}\n"
                print(total_sum)
                with open (txt, "a") as file:
                    file.write(string)
            case 5:
                
                print("Enter data for the second matrix")
                # creation of second matrix 
                start = int(input("Select the starting value for the matrix: "))
                end = int(input("Select the final value for the matrix: "))
                second_matrix = np.random.randint(start, end, size=(row, col))
                
                # create the matrix to multiply element by element
                # matmul does row-by-column product
                # mult_matrix = np.matmul(matrix, second_matrix)
                # multiply element by element
                mult_matrix = matrix * second_matrix
                string = f"Second matrix: \n{second_matrix}\nProduct of the matrices: \n{mult_matrix}\n"
                print(mult_matrix)
                with open (txt, "a") as file:
                    file.write(string)
            case 6:
                
                # mean of the matrix elements
                mean = matrix.mean()
                string = f"Mean of the matrix elements: \n{mean}\n"
                print(mean)
                with open (txt, "a") as file:
                    file.write(string)
                    
            case 7:
                
                # check for square matrix
                if row == col:
                    # matrix determinant
                    det = np.linalg.det(matrix)
                    string = f"Matrix determinant: \n{det}\n"
                    print(det)
                    with open (txt, "a") as file:
                        file.write(string)
                else:
                    print("The matrix is not square")
                
            case 8:
                
                # choice to change user or exit
                choice = input("Do you want to enter data as a new user? yes/no: ")
                if choice.lower() == "yes":
                    rand_id = str(np.random.randint(0, 100, 10))
                else:
                    break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
else: 
    print("Module imported")