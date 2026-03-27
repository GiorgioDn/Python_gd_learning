#define the recursive fibonacci function that returns only the last element
def fibonacci_recursive(n):

    #return -1 as value in case of errors for any [reason]
    if n < 0:
        return -1
    elif n< 2:
        return n
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

#define the fibonacci function that returns the list of elements during each iteration
def fibonacci_succ(n, list_res):
    
    a = 0
    b = 1
    count = 1

    while count <= n +1:
        list_res.append(a)
        count += 1
        next = a + b
        a = b
        b = next
        
    return list_res