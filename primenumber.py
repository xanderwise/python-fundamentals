#.1. Write a pyrthon progrsm to check whether a number is a prime number or not.

# Function to check if a number is prime
def prime(number):
    if number <= 1:
        print(False)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(False)
print(True)

# Input from the user
num = int(input("Enter a number: "))

if prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

