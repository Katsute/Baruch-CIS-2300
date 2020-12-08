#### Question 21
"""
Write a loop that asks the user to enter a number. 
The loop should iterate 5 times and keep a running 
total of all the numbers entered.

(clue: you can use for loops)
"""

total = 0  # set total variable
for _ in range(1, 6):  # (1-5)
    total += float(input("Please enter a number: "))  # ask user for a number and add to total
    print(total)  # print running total
    
#### Question 22
"""
Write a program that asks the user to enter the number 
of hours they worked for in a given week. Number of 
hours entered should be in the range of 0 to 40.

Also ask user to enter their pay rate. It should be a 
positive value above minimum wage 
(Assume minimum wage of $10).

Your program should ask user to re-enter the values 
for hours and wages until valid inputs are given. 
Based on the hours entered calculate their wages as follows:

20 hours or less: regular pay;

between  20 and 30: regular pay for 
first 20+ 1.5*regular pay for extra hours above 20;

between 30 and 40: regular pay for 
first 20 + 1.5*regular pay for next 10 hours + 2*regular 
pay for extra hours above 30
"""

hours = -1  # initialize hours
while hours < 0 or hours > 40:  # require 0-40 hours
    hours = int(input("Enter hours worked (0-40): "))  # ask user for hours

wage = -1 # initialize pay
while wage < 10:  # require $10+
    wage = float(input("Enter hourly wage (min $10): "))  # ask use for wage

pay = wage * min(hours, 20)  # calculate pay as wage times hours (up to 20 hours)
# use max() to ensure no negative hours on hours less than 20
pay += wage * 1.5 * min(max(0, hours-20), 10)  # calculate 1.5x pay as all hours after 20 (up to 10 hours after that)
# use max() to ensure no negative hours on hours less than 30
pay += wage * 2.0 * min(max(0, hours-30), 10)  # calculate 2x pay as all hours after 30 (up to 10 hours after that)
print("Wages owed: $", pay)

#### Question 23
"""
Nested loops:

The code below currently enters a loop where it keeps 
printing “Even”. Fix the code so that it prints 
“Even” and “Odd” for numbers 0 to 9.
"""
number = 0  # set initial num

while number < 10:  # set loop break condition (0-9)

    while number % 2 == 0:  # if 2/ no remainder
    
        print("Even")  # print even
        
        number += 1  # add to num to avoid infinite loop
    
    while number % 2 != 0:  # if 2/ has a remainder
    
        print("Odd")  # print odd

        number += 1  # add to num to avoid infinite loop

#### Question 24
"""
Here is a tax proposal for rich individuals:

If the total income is:

a. Less than $200,000, one pays just 1% tax 
 on the total income,

b. More than $200,000, then one pays 5% tax on
 the total income,

c. More than $500,000 then one pays 5% tax on
 the first $500,000 and 2 cents for every dollar above $500,000.

Write a program that calculates the tax Owed under
 this variation. Your program must ask user to enter
 their income and display their total tax owed in
 proper format. Write your code with various conditionals
 statements such that each case is executed only once.

(Clue: if-else; format statement)
"""

income = float(input("Total income: $"))  # ask user for total income
# if not needed because income is assumed to be positive
tax = 0.01 * min(income, 200_000)  # calculate tax as 1% of total income (up to 200k)
if income >= 200_000:  # if income exceeds 200k
    tax += 0.05 * min(income-200_000, 300_000)  # calculate tax as 5% total income after 200k (up to 500k (which is 300,000 after 200,000))
if income >= 500_000:  # if income exceeds 500k
    tax += 0.02 * (income-500_000)  # calculate tax as $0.02 per dollar after 500k

total = income + tax  # calculate total as income + tax
print("Tax owed: $" + "{:,.2f}".format(tax))  # print tax as two decimal float