#variables to initialize selected numbers, even, odd and their sums
even = []
odd = []

#user input list 
remember = []

#while for user's positive inputs
while True:
    num_int = int(input("Type a positive integer greater than 0: "))
    
    #while loop executed until the number is positive
    while num_int<=0:
        num_int = int(input("Type a positive integer greater than 0: "))

    print("The chosen number is: ", num_int)
    remember.append(num_int)
    
    #variables for the sum
    even_sum = 0
    odd_sum = 0

    #check if the selected number is even or odd
    for n in range(1, num_int):
        if n%2==0:
            even.append(n)
            even_sum += n
        else:
            odd.append(n)
            odd_sum += n
            
    print("Even numbers in the range are: ", even, "whose sum is: ", even_sum)
            
    print("Odd numbers in the range are: ", odd, "whose sum is: ", odd_sum)

    #check if the number is prime or not 
    if num_int < 2:
        print("The selected number is not prime")
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if num_int % i == 0:
                print("The selected number is not prime")
                break
        else:
            print("The selected number is prime")
    
    print("Numbers chosen so far are:", remember)
    chooice = input("Do you want to continue entering numbers? ")
    
    if chooice.lower() == "no":
        break
    #reset the variables used to reuse them in the new cycle
    else:
        even.clear()
        odd.clear()
