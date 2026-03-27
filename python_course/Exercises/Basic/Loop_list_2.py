# Initialize the list
list_num = [3, 4, 6, 7, 8, 10]

# check if the list is not empty
if len(list_num) > 0:
       
    # initialize the maximum value 
    max_val = list_num[0]
    
    # find the maximum
    for n in list_num:
        if n > max_val:
            max_val = n
        
    print("Maximum value:", max_val, "\n")

    # initialize variables for counting with while
    list_len = len(list_num)
    n=0 
    
    # count the numbers in the list with while
    while n<list_len:
        print(f"Element at index {n}: {list_num[n]}")
        n += 1
    
    # print total count
    print("Total count:", n)
    
else:
    print("Empty list")