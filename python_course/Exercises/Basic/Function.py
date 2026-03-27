import random

#define the function that randomizes given a certain interval
def randomNum (min, max):
    ran = random.randint(min, max)
    return ran

#define the function that compares the random number with user responses
def guess (casual):
    while True:
        answer = int(input("Try to guess the random number in the interval: "))
        if answer<casual:
            print("The selected number is lower than the correct one")
        elif answer>casual:
            print("The selected number is higher than the correct one")
        else: 
            break
    
    return True
        
#select max and min for randomization
print("Select minimum and maximum number for the random interval")
min = int(input("Minimum: "))
max = int(input("Maximum: "))

#generate random number
casual = randomNum(min, max)
#try to guess the number
guess = guess(casual)
if guess == True:
    print("Congratulations you guessed it")