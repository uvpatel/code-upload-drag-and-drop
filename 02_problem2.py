# Check your percentage of pcm
p = int(input("Enter marks of phy: ")) # physics 
c = int(input("Enter marks of chem: ")) # chemistry
m = int(input("Enter marks of maths: ")) # maths


total_percentage = (100*(p+c+m))/300
if(((total_percentage)<33, p<33 and c<33 and m<33)):
   print("you are fail,better luck next time",total_percentage)




else: print("You are pass",total_percentage)