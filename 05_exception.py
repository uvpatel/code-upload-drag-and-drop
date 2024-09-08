try:
    a = int(input("Hey, Enter the number: "))
    print(a)
except ValueError as v:
     print("Heyy")
     print(v)
except Exception as e:
     print(e)

     
print("Thanks")