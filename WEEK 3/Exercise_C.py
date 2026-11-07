price=float(input("Enter Price:"))

if price < 0:
    print("Error: Purchase amount cannot be negative. Please restart and enter a valid amount.")

else:
    if price<10000:
        Discount=0.0
    elif price<50000:
        Discount=0.05
    else:
        Discount=0.10



Discount_Amount= price*Discount
Final_Amount_Payable= price-Discount_Amount



print(f"Original amount: NGN{price:,.2f}")
print(f"Discount amount: NGN{Discount_Amount:,.2f}")
print(f"Final amount payable: NGN{Final_Amount_Payable:,.2f}")
