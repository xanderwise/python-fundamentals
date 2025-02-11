#A simple Python program to check whether a year is a leap year or not;
year = 2021
if year % 4 == 0 and year % 100 !=0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")



#.2.A Python program that checks whether a letter is a vowel or a consonant;
letter = "B"
vowels = "aeiouAEIOU"
if letter in vowels:
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")