# Simple Tax Calculator
amount = float(input("Enter amount = "))
tax = float(input("Enter tax percent (if tax is 15% then type 15 )= "))
print("Tax, you  need to pay is %0.2f" % (amount*(tax/100)))
