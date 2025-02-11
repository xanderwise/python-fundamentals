# Built in functions/ Standard library functions.

y = max(45, 89, 75, 88, 56, 43)
print("The maximum value is",y)

x = min(75,65,55,90,58)
print("The minimum value is",x)

# User defined functions
def school():
    print("eMobilis")

school()

def add():
    num1 = 5
    num2 = 10
    print("The sum is",num1+num2)

add()

# Parameter/Variable and Argument/Value
def multiply(a , b):
    print("The product is",a*b)
multiply(6,5)
multiply(6,50)
multiply(68,5)

def employee(name, age, gender, salary, position):
    print(name,age,gender,salary,position)

employee("maureen",25,"male",560000,"CEO")
employee("Glory",25,"female",760000,"Developer")
employee("Freshian",23,"female",60000,"Receptionist")
employee("Alex",30,"male",300000,"Programmer")
employee("Faith",20,"female",300000,"Programmer")
employee("Kelvin",29,"male",300000,"Programmer")
employee("Shannel",22,"female",300000,"Programmer")
employee("Wendi",20,"male",300000,"Programmer")
employee("Tuco",21,"female",300000,"Programmer")
employee("Brian",34,"male",300000,"Programmer")



# A program to display details for 5 patients.
#Using a user defined function, implement parameter and argument
#Fullname, gender, age, disease.

def patient(fullname, gender, age, disease):
    print(fullname, gender, age, disease)

patient("Patric", "male", 55, "Tuberculosis")
patient("Mavin", "male", 35, "livermorium")
patient("Patric", "male", 55, "Hepatitis")
patient("Patric", "male", 55, "Brain tumor")
patient("Patric", "male", 55, "Varicose vein")

