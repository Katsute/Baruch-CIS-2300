def main():
    # get
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    rate = determined_comm_rate(sales)
    # calc
    pay = sales * rate - advanced_pay
    # print
    print("The pay is $", format(pay, ",.2f"), sep='')
    return

def get_sales():
    return float(input("Sales: $"))

def determined_comm_rate(sales): 
    if sales < 10_000 :
        return 0.10
    elif sales >= 10_000 and sales <= 14_999:
        return 0.12
    elif sales >= 15_000 and sales <= 17_999:
        return 0.14
    elif sales >= 18_000 and sales <= 21_999:
        return 0.16
    else:  # 22k+
        return 0.18

def get_advanced_pay():
    print("Input $0 if you do not have advanced pay")
    return float(input("Advanced Pay: $"))

main()