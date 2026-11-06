while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice=int(input("Enter Choice from 1-5:"))

    if choice ==5:
        print("Googbye. Thank you")
        break

    if choice !=1 and choice !=2 and choice !=3 and choice !=4 and choice !=5:
        print("Invalid choice. Try again")
        continue     

    first_number= float(input("Enter first Number:"))
    second_number= float(input("Enter second Number:"))

    if choice==1:
        result=first_number+second_number
        print(f"Result: {result:.2f}")

    elif choice==2:
        result=first_number-second_number
        print(f"Result: {result:.2f}")

    elif choice==3:
        result=first_number*second_number
        print(f"Result: {result:.2f}")

    elif choice==4:
        if second_number==0:
            print("Cannot divide by zero.")
        else:
            result=first_number/second_number
            print(f"Result: {result:.2f}")



    
        
    


