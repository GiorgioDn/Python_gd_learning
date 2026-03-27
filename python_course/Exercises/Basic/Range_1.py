# break the while loop with a choice
while True:
    # input choice
    choice = int(input("Choose 1 to enter a string, 2 for a number: "))
    
    if choice == 1:
        text = input("Enter a string: ")
        # get the length of the string
        pair = len(text)
        # check if the number of letters is even or odd
        if pair%2 == 0:
            print("The string contains an even number of letters: ", pair)
        else:
            print("The string contains an odd number of letters: ", pair)
    elif choice == 2:
        num = int(input("Enter a number: "))
        # check if the number is even or odd
        if num%2 == 0:
            print("The number", num, "is even")
        else:
            print("The number", num, "is odd")
    else:
        print("Invalid data entered")
    
    repeat = input("Do you want to repeat the choice? ")
    
    # exit the while loop
    if repeat.lower() == "no":
        break