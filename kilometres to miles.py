# Python program o convert kilometers to miles

def convert():
    print("want to convert kilometers to miles?")
    km = float(input("enter distance covered in kilometres: "))
    miles = km * 0.621371
    print("converted",km,"kilometers to miles is: ",miles,"miles")

convert()