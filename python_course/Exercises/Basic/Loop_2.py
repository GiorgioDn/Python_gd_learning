#starting number
start = int(input("Enter a number: "))
repeat = True

if start<0:
    #while loop to print the number decremented by one
    while repeat:
        for n in range(start, 1, +1):
            print(n)
        #ask the user if they want to continue
        ask = input("Do you want to print again? ")
        if ask.lower() == "no":
            repeat = False
else:
    #while loop to print the number decremented by one
    while repeat:
        for n in range(start, -1, -1):
            print(n)
        #ask the user if they want to continue
        ask = input("Do you want to print again? ")
        if ask.lower() == "no":
            repeat = False