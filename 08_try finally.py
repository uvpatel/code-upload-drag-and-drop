def main():
    try:
        a = int(input("Hey, Enter the number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return 
    finally:
        print("I am inside finally")

main()
