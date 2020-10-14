# factorial
num = int(input("Number: "))

factorial = 1
for n in range(1, num + 1):
    factorial *= n
    print(factorial)

# ocean
mm = 0;
rate = 1.6
for y in range(1,26): # (1-25)
    mm += rate
    print("Year", y, ':', format(mm, ".1f"), "mm")


# wl
weight = float(input("Current Weight: "))

for i in range(1, 7): # (1-6)
    weight -= 4
    print("Month", i, ':', weight,"lbs")


# 10x
for n in range(0, 1001, 10): # (0-1000, +=10)
    print(n)

# 10

sum = 0
for n in range (1, 11): # (1-10)
    num = float(input("Number: "))
    sum += num
    print("Sum", sum)

# row col
for row in range(3):
    for col in range(6):
        print(col, end=' ')
    print()
    
for row in range(3):
    for col in range(6):
        print(row, end=' ')
    print()