"""
Write a program that asks the user to enter the number of hours they worked for in a given week.
Number of hours entered should be in the range of 0 to 60.
Also ask user to enter their pay rate. It should be a positive value above minimum wage (Assume minimum wage of $15).
Your program should ask user to re-enter the values for hours and wages until valid inputs are given. Based on the hours entered calculate their wages as follows:
40 hours or less: regular pay
between 40 and 50: regular pay for first 40 + 1.5*regular pay for extra hours above 40
between 50 and 60: regular pay for first 40 + 1.5*regular pay for next 10 hours + 2*regular pay for extra hours above 50
"""

# TESTS:
# hours | rate  | expected
# ------|-------|---------
# 0     | 15    | 0
# 40    | 15    | 600
# 50    | 15    | 825
# 60    | 15    | 1125

hours = None

# do{
#   hours = input()
# }while(hours < 0 || hours > 60)

# unfortunately Python doesn't have a do while equivalent
while True:
    hours = float(input("Enter hours worked: "))
    if 0 <= hours <= 60:  # break from loop if hours are within range 0-60
        break
    print("Hours worked must be from 0-60")

pay_rate = None

while True:
    pay_rate = float(input("Enter pay rate: $"))
    if pay_rate >= 15:  # break from loop if pay rate is $15 or above
        break
    print("Pay rate must be at least $15")

# calculate base rate as hours * rate (max 40 hours)
pay = pay_rate * min(hours, 40)
# calculate 1.5x overtime as hours * rate (min 0 hours max 10 hours past 40)
pay += pay_rate * 1.5 * max(min(hours-40, 10), 0)
# calculate 1.5x overtime as hours * rate (min 0 hours past 50)
pay += pay_rate * 2.0 * max(hours-50, 0)

print("Pay: $", pay, sep='')

# are the other parts also part of the HW? ↓

"""
Complete the code on lines 4 and 6 so that it prints the number 6.
"""

x = 3
i = 0
while i < 3:
    x = x + 1  # technically x = 6 would be correct because x is now 6
    i = i + 1
print(x)  # technically you could just print 6 and it would be correct


"""
The following program segment should result in an infinite loop. But the lines have been mixed up and include extra lines of code that aren't needed in the solution.
"""

first = 7
second = 5
third = 9
while (first > second):
    print ("This is an infinite loop")  # indent this line and remove below to make an infinite loop
# while (first > third):
#     print ("I wonder which while loop I am in?")

