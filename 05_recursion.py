''' 
factorial(1) = 1    1! = 1
factorial(2) = 2X1
factorial(3) = 3X2X1
factorial(4) = 4X3X2X1
factorial(5) = 5X4X3X2X1

factorial(n) =n x n-1x....3x2x1

factorial(n)= n*factorial(n-1)'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return factorial(n)* factorial(n-1)

n = int(input("Enter your number: "))
print(f"The factorial of this number is:{factorial(n)}")

