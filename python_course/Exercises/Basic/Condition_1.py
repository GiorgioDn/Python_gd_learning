#input variable for number selected by user
number = int(input("Select an integer number: "))

#check number based on met conditions
if number > 0:
    if number%2 == 0:
        if number > 10:
            print("The number is even and greater than 10")
        else:
            print("The number is even and less than 10")
    else:
        print("The number is odd")
else:
    print("The number is negative")