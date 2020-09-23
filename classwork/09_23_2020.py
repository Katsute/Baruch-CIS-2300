# ex1
# get total income
# if <$100k then 1% tax
# else if >$100k then 5% tax
# else if >$500k then 5% tax and 2¢ per dollar past $500k

totalIncome = float(input("Total Income: "))

if totalIncome < 100_000:
    tax = totalIncome * .01
else:
    # only charge 5% tax on income under $500k
    tax = min(totalIncome, 500_000) * .05  
    
    if totalIncome > 500_000:
        # 2¢ per dollar past $500k
        tax += (totalIncome - 500_000) * .02

print("Total tax payment: $", format(tax, '.2f'), sep=' ')

# ex2 (see homework_3 leap year)

# ex3

if totalIncome < 100_000:
    tax = totalIncome * .01
else:
    # double comparator!
    if 100_000 < totalIncome < 500_000:
        tax = totalIncome * .02