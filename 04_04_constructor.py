class employee:         #class is like noun
    lang = "py"     #this is a class atributes
    salary = 1200000000

def getinfo(self):      #here getinfo is method(class)
     print(f"The language is{self.lang}.The salary is{self.salary}")
def __init__(self):#dunder method which is automatically called
     print("I am creating an object")
     
     
     
@staticmethod
def greet():
    print("Good morning")


urvil = employee() # urvil is obj

     # to do some is called method  

urvil.greet()
urvil.getinfo()
# employee.getinfo()

# isinstance attributes, take prefrence overr class attributes during assigment & retrival.