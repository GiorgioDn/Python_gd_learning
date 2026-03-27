#checks the function argument and if it's negative makes it positive
def d_control_negative(function):
    def wrapper(*args, **kwargs):
        #requires the first argument of the function to be an integer
        if args[0]<0:
            new_args = list(args)
            new_args[0] = abs(new_args[0])
            return function(*new_args, **kwargs)
        else: 
            return function(*args, **kwargs)
    return wrapper

#DA TESTARE
#execute function based on whether the list is returned or not
def d_control_list(function):
    def wrapper(*args, **kwargs):
        #requires that the second argument of a function be a collection
        
        if len(args[1]) !=0:
            if function.__name__ == "subList":
                result = function(*args, **kwargs)
                return result
        else:
            if function.__name__ == "subList_withoutList":
                result = function(*args, **kwargs)
                return result
    return wrapper


@d_control_negative
def subList_on_decoration (n, base_list):
    
    #check that n is less than the length of the list
    if len(base_list)>n:
        #initialization of new list
        new_list = []
        end = 0
        
        #verify that n is correct
        print(n)
        
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
    
x = subList_on_decoration(-4, [9, 2, 2, 4, 5, 1, 3, 4])

print(x)
