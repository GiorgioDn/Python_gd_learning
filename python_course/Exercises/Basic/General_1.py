""" 
    Create a function that takes a positive integer to generate a sublist of the first n elements of a user-defined list, furthermore the function must let you choose whether to return the sublist, eliminate duplicates or check for any differences between the list and the sublist.
"""
from random import randint

#function to perform exercise features
def subList (n, base_list):
    
    #check that n is less than the length of the list
    if len(base_list)>n:
        #initialization of new list
        new_list = []
        end = 0
        
        #fill the new list
        while end < n:
            new_list.append(base_list[end])
            end +=1
        
        #choice of operation
        chooice = int(input("Choose one of the following operations: \n 1. Return the sublist \n 2. Eliminate duplicates of the sublist\n 3. Verify the different elements of the sublist \n"))
        
        match chooice:
            case 1:
                return new_list
            case 2:
                #conversion to eliminate duplicates
                list_without_double = set(new_list)
                return list_without_double
            case 3:
                #make comparison of the two lists
                set_new = set(new_list)
                set_ori = set(base_list)
                return set_ori.difference(set_new)
            case _:
                return False
    else:
        return False

#in case a list is not entered as input      
def subList_withoutList (n):
    
    #initialization of new list with random values
    
    new_list = []
    end = 0
    base_list = []
    
    #create the initial list with random values
    for num in range(n+1):
        base_list.append(randint(0, n*2))
    
    #fill the new list
    while end < n:
        new_list.append(base_list[end])
        end +=1
    
    #choice of operation
    chooice = int(input("Choose one of the following operations: \n 1. Return the sublist \n 2. Eliminate duplicates of the sublist\n 3. Verify the different elements of the sublist \n"))
    
    match chooice:
        case 1:
            return new_list
        case 2:
            #conversion to eliminate duplicates
            list_without_double = set(new_list)
            return list_without_double
        case 3:
            #make comparison of the two lists
            set_new = set(new_list)
            set_ori = set(base_list)
            return set_ori.difference(set_new)
        case _:
            return False

#executes the function automatically when imported 
#x = subList(4, [9, 2, 2, 4, 5, 1, 3, 4])

#print(x)