    run=1
while run==1:
    digit= int(input("Enter any digit here:"))

    if digit <1:
        print("Enter 1 or a value greater than 1.")
    elif digit>=1:
        for multiplier in range (1,13):
            print(f"{digit}*{multiplier}={digit*multiplier}")
    else:
        print("Enter valid number.")

    load= input("To end enter the digit 5, enter any other thing to continue:")
    if load== "5":
        run=0
