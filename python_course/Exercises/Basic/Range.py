# let the user select three numbers for the step, the maximum, and the number of items per row
print("Choose the maximum number, the range steps, and the numbers displayed per row")
max_val = int(input("Maximum: "))
step = int(input("Step: "))
row_size = int(input("Numbers per row: "))

counter = 0

# check that the maximum is greater than the steps
if max_val > step:
    # print the numbers per row defined by the user up to the maximum
    for i in range(0, max_val + 1, step):
        print(i, end=" ")
        counter += 1
        if counter == row_size:
            # new line
            print()    
            counter = 0
else:
    print("Invalid data")