# sum of first 5 nums
sum = 0
Max = 5

for number in range(Max):
    number = float(input("enter a number: "))
    sum += number
    
print(sum)

# indexed loops
vals = [3, 15, 17, 7]
result = 0
for x in vals:
    result += x
print(result)

# += -= *= .= %=

# getscore
score = float(input("Please enter your score: "))
while score < 0:
    print("There is an error, please enter a positive number")
    score = float(input("Please enter your score: "))
print(score)

# practice

# nums = ''
# for num in range(99, 89, -1):  # 99-90 (inclusive) decrement by 1
#    nums += str(num) + ", "  # append comma to string
# print(nums[:-2])  # remove last comma and space from string

for num in range(99, 89, -1):
    print(num, end=", ")  # by default end is newline