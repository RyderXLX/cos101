num_of_days=int(input("Enter number of days:"))


if num_of_days <=0:
    print("Invalid Number of days")
    num_of_days=int(input("Enter number of days:"))

total_sales=0
high_sales_days=0
low_sales_days=0

for day in range(1,num_of_days+1):
    sales_amount=float(input("Enter sales amount:"))

    while sales_amount <0:
        print("Enter valid sales amount")
        sales_amount=float(input("Enter sales amount:"))

    total_sales+=sales_amount
    if sales_amount>=10000:
        high_sales_days +=1
    else:
        low_sales_days+=1

average_daily_sales=total_sales/num_of_days


print(f"Total sales:{total_sales:,.2f}")
print(f"Average daily sales:{average_daily_sales:,.2f}")
print(f"Days with sales of at least NGN 10000:{high_sales_days}")
print(f"Days with sales below NGN 10000:{low_sales_days}")



   




