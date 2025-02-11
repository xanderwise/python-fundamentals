class Student:
    # Properties/Attributes
    name = "Alex"
    gender = "Male"
    age = 18

    #Behavior/Method/Function
    def study(self):
        print("Student is studying")

student1 = Student() #Creating an object
print(student1.name)
student1.study()

student2 = Student()