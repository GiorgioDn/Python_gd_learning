# define the lists that will contain prime and non-prime numbers
prime = []
non_prime = []

while True:
    # Choice of number range
    print("Choose a range of two numbers")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    
    # create the list including num2
    numeri = [*range(num1, num2 + 1)]
    
    print(numeri)

    # check if numbers are prime or not
    for n in numeri:
        if n < 2:
            non_prime.append(n)
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    non_prime.append(n)
                    break
            else:
                prime.append(n)
    
    # print prime and non-prime numbers
    print("Prime numbers in the range:", prime)
    print("Non-prime numbers in the range:", non_prime)

    # exit the while loop
    choice = input("Do you want to repeat? (yes or no): ")
    if choice.lower() == "no" or choice.lower() == "n":
        break