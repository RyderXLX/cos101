student_name= input("student_name:")
daily_transport_cost= int(input("daily_transport_cost:"))
daily_feeding_cost= int(input("daily_feeding_cost:"))
days_on_campus= int(input("days_on_campus:"))
other_weekly_expenses= int(input("other_weekly_expenses:"))
weekly_budget= int(input("weekly_budget:"))


if (
    weekly_budget <0
    or days_on_campus <0
    or daily_feeding_cost <0
    or other_weekly_expenses <0
    or weekly_budget <0
):
    print("Invalid Value. Try again")

else:
    Transport_total= daily_transport_cost*days_on_campus
    Feeding_total= daily_feeding_cost*days_on_campus
    Weekly_total= Transport_total+Feeding_total+other_weekly_expenses
    
    


if Weekly_total<weekly_budget:
    Amount_remaining= weekly_budget-Weekly_total
    print("Within Budget")
    print(f"Amount_remaining:, NGN{Amount_remaining:}")
elif Weekly_total==weekly_budget:
    print("Exactly on budget")
    print("Amount_remaining:, NGN 0")
else:
    Amount_exceeded= Weekly_total-weekly_budget
    print("Over budget")
    print(f"Amount_exceeded:, NGN{Amount_exceeded:}")



print(f"Student:{student_name}")
print(f"Transport_total:, NGN{Transport_total:,.2f}")
print(f"Feeding_total:, NGN{Feeding_total:2f}")
print(f"Weekly_total:, NGN{Weekly_total:2f}") 

