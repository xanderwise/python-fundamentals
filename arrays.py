courses = ["MIT", "Cybersecurity", "Datascience"]
print(courses)

#Accessing an element.
print(courses[2])

#Loopin through an array.
for x in courses:
    print("Course is",x)

# Adding a new element
courses.append("Laravel")
print(courses)

#Removing ana element from an array.
courses.remove("Cybersecurity")
print(courses)

