# 1
x = float(input("First number: "))
y = float(input("Second number: "))

if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} is equal to {y}")
# bb
quiz = float(input("quiz: "))
mid_term = float(input("midterm: "))
final = float(input("final: "))

avg = (quiz + mid_term + final) / 3

if avg > 90:
    print("Congrats! You got an A")
# if else
x = 6
if x >=3:
    y = x-3
else:
    y = x+3
print("y is",y)

# max
x = float(input("First number: "))
y = float(input("Second number: "))
print("The larger number is:", x if x > y else y)  # max(x, y) can also be used

