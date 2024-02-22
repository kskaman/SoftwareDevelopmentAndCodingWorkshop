# Caluclates the expense

n = int(input("\nHow many different items you bought : "))

# expenses is a dictionary
# Format of each item is {item_name : [total_units_bought, price_per_unit]}
expenses = {}

total = 0

for i in range(n):
    print("\nEnter details for ITEM %d : " %(i+1))
    name = input("Name of item bought : ")
    units = float(input("Units of " + name + " bought : "))
    price = float(input("Price per unit of " + name + " : "))

    total += price*units
    expenses[name] = [units, price]


print("\n\nYour Bill\n\n")
print("{:>10} \t {:>10} \t {:>10} \t {:>10}".format(str("Item"), str("Units"), str("Price per Unit"), str("Total")))
for key, value in expenses.items():
    print("{:>10} \t {:>10} \t {:>10} \t {:>15}".format(str(key), str(value[0]), str(value[1]), str(value[0]*value[1])))

print("\n\nTotal expense : %.2f\n" % (total))