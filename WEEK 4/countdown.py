positive_number=int(input("Enter a positive number:"))

while positive_number<1:
    print("Invalid Number.Try again")

for number in range(positive_number,0,-1):
    print(number)

print("Countdown Complete")
