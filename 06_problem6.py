a = int(input("Enter your marks "))

if(100>=a>=90):
    print("your gread is Ex")
elif(90>a>=80):
    print("your gread is a")
elif(80>a>=70):
    print("your gread is b")
elif(70>a>=60):
    print("your gread is c")
elif(60>a>=50):
    print("your gread is d")
elif(a<0 and a>100):
    print("your marks are not valid")
else: 
    print("you are fail")