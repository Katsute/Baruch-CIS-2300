# 51177 ################################################################################################
"""
Given a variable n that contains a positive integer value, use two additional variables
k and total to write a for loop to compute the sum of the cubes of the first n counting numbers,
and store this value in total. Thus your code should put 1*1*1 + 2*2*2 + 3*3*3 + ... + n*n*n into total.
Use no other variables other than n, k, and total.
"""

n = int(input("Positive Integer: "))
total = 0
for k in range(1, n+1):
    total += k*k*k
print(total)

# 51259 ################################################################################################
"""
Compute the average of the numbers from 1 to n (where n is a positive integer value) 
and assign it to the variable avg.
"""

n = int(input("Positive Integer: "))
total = 0
for k in range(1, n+1):
    total += k
avg = total / n
print(avg)

# 51929 ################################################################################################
"""
Write a for loop that prints the integers 0 through 39, each value on a separate line.
"""

for n in range(0, 40):
    print(n)

# 51931 ################################################################################################
"""
Write a for loop that prints in ascending order all the positive multiples of 5 that are less than 175, 
each value on a separate line.

Additional Notes:
Regarding your code's standard output, CodeLab will check for case errors and will check whitespaces
(tabs, spaces, newlines) exactly.
"""

for n in range(5, 175, 5):
    print(n)

# 51180 ################################################################################################
"""
Use the variables k and total to write a white loop that computes the sum of the squares of the first
50 counting numbers, and assigns that value to total. Thus your code should assign 1*1 + 2*2 + 3*3 + ...
+ 49*49 + 50*50 to total. Use no variables other than k and total.
"""

total = 0
k = 0
while k <= 50:
    total += k*k
    k += 1

print(total)
