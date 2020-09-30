"""
Create a new python file to finish homework_2

Exaple 2:
write a program to calculate the score:
1. Three scores are available now: quiz, mid_term, final (assign any values to variables)
2. calculate the average score
4. test the relationship between average and 90: if the average score is > 90 (if statement)
5. output "Congrats! You got A"

Remeber to add comments to your codes
"""

# get input from user and cast to float
quiz = float(input("quiz: "))
mid_term = float(input("midterm: "))
final = float(input("final: "))

# calc avg
avg = (quiz + mid_term + final) / 3

# if avg > 90 then A
if avg > 90:
    print("Congrats! You got an A")

"""
Example 4:
Here is a program to calculate the overtime payment, please add your own comments to
each of the line
"""

BASE_HOURS = 40  # declare float base hours
OT_MULTIPLIER = 2  # declare float overtime pay multiplier

hours = float(input('Enter the number of hours worked: '))  # ask user for hours worked then cast to float
pay_rate = float(input('Enter the hourly pay rate: '))  # ask user for hourly pay rate then case to float

# if hours exceeds base then calc overtime pay
if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS  # overtime is hours passed base
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER  # overtime pay is overtime hours * hourly wage * overtime multiplier
    gross_pay = BASE_HOURS * pay_rate + overtime_pay  # total pay is base pay + overtime pay
else:
    gross_pay = hours * pay_rate  # pay w/o overtime
print('The gross pay is $', format(gross_pay, ',.2f'), sep='')  # print total pay as a two point float
