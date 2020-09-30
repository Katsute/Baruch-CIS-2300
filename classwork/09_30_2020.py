# l1

keep_going = 'y'
while keep_going == 'y':
    sales = float(input("Amount of sales: "))
    comm_rate = float(input("Commission rates: "))
    
    commission = sales * comm_rate
    print("The commission is $", format(commission, ",.2f"), sep='')
    keep_going = input("Do you want to calculate another commission? (y/n): ").lower()
    

# l2

n=1
while n<=10:
    print(n)
    n+=1
print("done")

# l3
status = input("Are you a full time student? (y/n): ").lower()
if status == 'y':
    credits = int(input("How many credits?: "))
    while credits < 12:
        print("You need to register for more courses")
        creditReq = int(input("How many credits you wish to register for?"))
        credits = credits + creditReq
    print("Great, you have reached minimum credit requirement")