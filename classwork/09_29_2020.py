# intro to while loops
sum = 0
i = 0

while i <= 100:
    sum += i
    i += 1
    
print(sum)

# sale/com

i = 0
while i < 2:
    sales = float(input("Amount of sales: "))
    comm_rate = float(input("Commission rates: "))
    comission = sales * comm_rate
    i+=1

