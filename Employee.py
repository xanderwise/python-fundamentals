class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        print(self.position,"is earning",self.salary)

employee1 = Employee("John","CEO",300000)
print(employee1.name,employee1.position,employee1.salary)
employee1.info()

employee2 = Employee("Alex","Manager",400000)
print(employee2.name,employee2.position,employee2.salary)
employee2.info()

employee3 = Employee("Alex","Manager",400000)
employee4 = Employee("Alex","Manager",400000)
employee5 = Employee("Alex","Manager",400000)
employee6 = Employee("Alex","Manager",400000)