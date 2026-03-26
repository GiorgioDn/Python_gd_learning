# ask the user to select a number to check the if or else
number = int(input("Select an integer number: "))

# if the condition is true, the code after the colon is executed
if number > 0: 
    print ("The number is positive")
# if the first condition is false, elif can be used
elif number < 0:
    print("The number is negative")
# if the if and elif conditions are not met, the else code is used
else: 
    print("The number is 0")
    
# match compares the value with the case
command = input("Enter a command: ")

match command:
    case "start":
        print("Starting the program")
    case "stop":
        print("Closing the program")
    case "pause":
        print("Program paused")
    case _:
        print("Unrecognized command")