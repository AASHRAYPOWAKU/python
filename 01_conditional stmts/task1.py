name=input("Enter Student Name:")
grade=int(input("Enter Student grade level:"))
tuition_fee=int(input("Base tuition fee:"))
Discount_percentage=float(input("Enter discount percentage:"))
Discount_percentage2=float(input("Enter discount percentage2:"))
Discount_percentage3=float(input("Enter discount percentage3:"))
Discount_amount=tuition_fee*(Discount_percentage/100)
Discount_amount2=tuition_fee*(Discount_percentage2/100)
Discount_amount3=tuition_fee*(Discount_percentage3/100)
status=input(("Enter student academic Status:"))
final_price=tuition_fee-Discount_amount
final_price2=tuition_fee-Discount_amount2
final_price3=tuition_fee-Discount_amount3
if grade>=1 and grade<=12:
    print("Process  with discount calculation")
else:
    print("Invalid grade")
if grade>=9 and grade<=12:
    if status=="topper":
        print(final_price)
    else:
        print(final_price2)
elif grade>=6 and grade<=8:
    print(final_price3)
else:
    print("No Discount")



        
     



