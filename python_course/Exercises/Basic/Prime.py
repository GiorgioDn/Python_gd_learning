# define the list that will contain prime numbers
prime = []

# loop until 5 prime numbers are found
while len(prime) < 5:
    num = int(input("Enter a positive number: "))

    if num < 2:
        print("Invalid number or not prime")
    else:
        # check if num is prime or not
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("The number is not prime")
                break
        else:
            # if the loop doesn't break, it means it's a prime number
            print("The number is prime")
            prime.append(num)

print("5 prime numbers found:", prime)
