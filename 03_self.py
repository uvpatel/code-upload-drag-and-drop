class Employee:
    language = "python" #this is a class attribute
    salary = 12000000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
Urvil = Employee()
Urvil.language = "c"    #This is an instance attribute
print(Urvil.language, Urvil.salary) 
Urvil.getInfo()
Employee.getInfo(Urvil)