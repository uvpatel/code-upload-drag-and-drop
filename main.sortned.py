import random  
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s": 1,"w":-1,"g":0}
reverseDict = {1: "Snake",-1: "water" ,0:"Gun"}
you = youDict[youstr]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")



if(computer == you):
    print("It's a draw")

else:
   if((computer - you) == -1 or (computer - you) == 2):
    print("You lose")  
   else:
    print("you win")   

'''
1 for snake
-1for water
0 for gun


 By now we have 2 numbers(variables),you and computer

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s": 1,"w":-1,"g":0}
reverseDict = {1: "Snake",-1: "water" ,0:"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")

else:    
    if(computer == -1 and you ==1):
         print("You win!")

    elif(computer ==-1 and you ==0):
         print("You lose!")  

    elif(computer ==1 and you ==-1):
        print("You lose!")    

    elif(computer ==1 and you ==0):
        print("You win!")    

    elif(computer ==0 and you==-1):
        print("You lose!")   

    elif(computer ==0 and you==1):
        print("You lose!")

    else: print("Something went wrong")'''                
  
#   The below logic is written on the basis of the value of computer - you
