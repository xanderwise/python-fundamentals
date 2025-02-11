class Student:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def study(self):
        print(self.name,"is studying")

student1 = Student("John","male",18)
print(student1.name, student1.gender, student1.age)
student1.study()

student2 = Student("Alex","Male",18)
print(student2.name, student2.gender, student2.age)
student2.study()

student3 = Student("Victor","Male",18)
student4 = Student("Brian","Male",18)
student4 = Student("Brian","Male",18)