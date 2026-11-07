  # Form a multiplication from user input


number= int(input("Enter number b/w 2 & 10:"))

if number <=0:
    print("Number cannot be zero or negative!")
elif number==1:
    print("Invalid input. Try again")
elif number>10:
    print("Invalid input. Try again")
else:
    for count in range(1,13):
        print(f"{number}*{count}={number*count}")
