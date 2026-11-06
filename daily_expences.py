num_of_days=int(input("Enter number of days you want to record:"))
if num_of_days<1:
    print("Invalid Number")

else:
    total=0.0
    for day in range(1,num_of_days+1,):
        expense=float(input(f"Enter expense for day {day}:"))
        total=total+expense
        average_expense=total/num_of_days


    print(f"Number of days:{num_of_days}")
    print(f"Total expenses:NGN{total:.2f}")
    print(f"Average per day: NGN {average_expense:.2f}")
    
