class Employee:
    language = "python" #this is a class attribute
    salary = 12000000

Urvil = Employee()
Urvil.language = "c"    #This is an instance attribute
print(Urvil.language, Urvil.salary) 