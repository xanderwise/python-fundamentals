# A python program that checks for room temperature.

temperature = 23
if temperature > 25 :
    print("It is too hot")

else :
    print("It is too cold")

# A program that returns the largest number.
first = 89
second = 30
third = 56

if first > second and first > third :
    print(first, "is the largest number")
elif second > first and second > third :
    print(second, "is the largest number")
else :
    print(third, "is the largest number")


# Program to check a number and return whether a number is even or odd.
number = 15
if number == 0:
    print(number, "is a nutral number")
elif number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")