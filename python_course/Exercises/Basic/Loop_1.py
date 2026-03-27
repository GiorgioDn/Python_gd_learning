repeat = True

#create a while loop that repeats until the user wants
while repeat:
    #get input number
    num = int(input("Type a positive number: "))
    #check that the number is positive
    if num<0:
        print("Number is invalid")
    else: 
        #print numbers in descending order
        for n in range(num, -1, -1):
            print(n)
            
    #ask user to exit the while
    ask = input("Do you want to continue? ")
    if ask.lower() == "no":
        repeat = False