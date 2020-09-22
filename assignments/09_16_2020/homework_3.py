"""
# Homework3:

# Question(1) update homework2 using if-elif-else statement
# First develop your pseudocode or flowchart, then convert to real codes:
Amita had written a program to calculate total wages of her employees using regular and overtime hours. 
Calculate the overtime payment: 
regular working hours are 40. once it exceeds 40, people are paid differently:      
A person working 65 hours with a regular wage of $10 per hour would work at $10 per hour for 40 hours,
at 1.5 * $10 for 20 hours of overtime, and 2 * $10 for 5 hours of double time, 
for a total of 10*40 + 1.5*10*20 + 2*10*5 = $800.

## some codes you can use:
#overtime = 0 
#regularHours = 40
#hours = float(input('Enter hours worked: '))
#hourlyWage = float(input('Enter dollars paid per hour: ')) 
#if hours <= 40: 
#wage = 10*hours 
#else:
#overtime = hours - 40 
#totalWages = hourlyWage*regularHours + (1.5*hourlyWage)*overtime
#if
#else
#print("Wages for ", hours, " hours at $", format(hourlyWage,'.2f'), " per hour are $", #format(totalWages,'.2f'), sep="")) 
"""


# declare regHours = 40
# ask for wage and hours worked
# add 1.5x wage for 0-20HR OT
# add 2x wage for 20HR+ passed OT
# calc wage

regularHours = 40
hours = float(input("Enter hours worked: "))
hourlyWage = float(input("Enter hourly wage: "))

overtime = hours - regularHours
wage = min(hours, regularHours) * hourlyWage
if overtime > 0:  # overtime hours (40+) x1.5
    wage += min(overtime, 20) * hourlyWage * 1.5
if overtime - 20 > 0:  # excessive overtime hours (60+) x2.0
    wage += (overtime - 20) * hourlyWage * 2.0
print(f"Wages for {hours} hours at ${format(hourlyWage,'.2f')} per hour are ${format(wage,'.2f')}")


"""
# Question(2): try to write flowchart and add comments to your codes.

## clue: remainder function

Use the Gregorian approach to determine whether a given year is a leap year. Here are the conditions: 
    Determine whether the year is divisible by 100. If it is, then it is a leap year if and only if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not. 
    If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4. For example, 2008 is a leap year, but 2009 is not.
"""

# if year/100 rem = 0 and year/400 rem = 0 then: leap year
# if year/100 rem != 0 and year/4 rem = 0 then: leap year
# else: not leap year


year = int(input("Year: "))

# isLeapYear year/100 and year/400     OR    !year/100 and year/4
isLeapYear = (year%100 == 0 and year%400 == 0) or (year%100 != 0 and year%4 == 0)

print(f"{str(year)} {'is' if isLeapYear else 'is not'} a leap year")  # print if is leap year

