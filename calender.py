# Python program used to display a calender

import calendar

def calenda():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print(calendar.month(year, month))

calenda()