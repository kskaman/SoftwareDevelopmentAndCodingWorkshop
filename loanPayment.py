# LOAN PAYMENT CALCULATOR
# This script inputs loan amount, interest rate and number of months to make payment
# and return the total amount to be paid and monthly amount to be paid

# Get deatils
print("\n")
Loan = float(input("How much money did you borrow from bank : CAD "))
rate = float(input("What is the insterest rate : "))
months = int(input("How many monthly installments you want "))


monthlyRate = rate/1200

for i in range(months):
    # Calculate interest
    interestAmount = Loan*monthlyRate
    Loan = Loan + interestAmount



print("\nYou have to pay %.2f\n in total in %d months. Your monthly payment is %.2f\n" % (Loan, months, Loan/months))
