 # ===================================================
# Title: Student Weekly Expense Calculator
# Filename: weekly_expenses.py
# Course: COS 101 Practical Class
#
#1. INPUT-OUTPUT-PROCESS(IPO) ANALYSIS:
#   -Input: student_name (str), daily_transport (float),
#            daily_feeding (float), days_on_campus (int)
#             other_expenses (float)
#   -Process: Calculate transport total, feeding total,
#              and overall weekly total
#   -Output: Printed summary of expenses formatted to 2 decimal places
#2. DATA TYPE EXPLANATIONS:
#   student_name uses a string (str) because it represents text characters.
#   The same can be said for everything else enclosed in a quotation.
#   days_on_campus uses an integer (int) because days are counted in whole numbers.
#   daily_transport_cost, daily_feeding_cost_, and other_weekly_expenses use floats
#   (float) because they represent currency values which can include decimals.
#
#3.EXPECTED AND ACTUAL RESULTS FOR TWO TESTS:
#
#    TEST 1 (Sample Test)
# Expected Result:
# Student: Ada Okeke
# Transport total: NGN 5,000.00
# Feeding total: NGN 7,500.00
# Other expenses: NGN 2,000.00
# Weekly total: NGN 14,500.00
# Actual Result: 
# (Program executed in IDLE and produced the following output:)
# Student: Ada Okeke
# Transport total:, NGN 5,000.00
# Feeding total:, NGN 7,500.00
# Other expenses:, NGN 2,000.00
# Weekly total:, NGN 14,500.00
#   TEST 2 (Custom Test)
# Expected Result:
# Student: Nasiru Yusuf
# Transport total:, NGN 3,002.50
# Feeding_total:, NGN 22,501.50
# Weekly_total:, NGN 28,504.00
# Actual Result:
# (Program executed in IDLE and produced the following output:)
# Student: Nasiru Yusuf
# Transport total:, NGN 3,002.50
# Feeding_total:, NGN 22,501.50
# Weekly_total:, NGN 28,504.00
#
#4. PSEUDOCODE:
#   START
#       READ student_name
#       READ daily_transport, daily_feeding, days_on_campus, other_expenses
#       CALCULATE transpor_total = daily_transport * days_on_campus
#       CALCULATE feeding_total = daily_feeding * days_on_campus
#       CALCULATR weekly_total = transpor_total + feeding_total + other_expenses
#       DISPLAY results
#   END
# ===================================================


# --- PYTHON CODE STARTS HERE ---

student_name= input("student_name:")
daily_transport_cost= float(input("daily_transport_cost:"))
daily_feeding_cost= float(input("daily_feeding_cost:"))
days_on_campus= int(input("days_on_campus:"))
other_weekly_expenses= float(input("other_weekly_expenses:"))


Transport_total= daily_transport_cost*days_on_campus
Feeding_total= daily_feeding_cost*days_on_campus
Weekly_total= Transport_total+Feeding_total+other_weekly_expenses


print(f"Student:{student_name}")
print(f"Transport_total:, NGN{Transport_total:,.2f}")
print(f"Feeding_total:, NGN{Feeding_total:,.2f}")
print(f"Weekly_total:, NGN{Weekly_total:,.2f}") 
