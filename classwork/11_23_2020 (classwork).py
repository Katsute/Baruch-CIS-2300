# Write a program that gets sales amounts 
# from the user and assigns them to a list.

def ice1():

    sales = [None] * 5
    
    for i in range(len(sales)):
        print("Day:", i + 1)
        sales[i] = float(input("Sales: $"))
    
    for sale in sales:
        print("Sale: $" + str(sale))
    
    
# use a function to remove all occurances

def main():
    ice1()
    
    remList = [1, 2, 3, 4, 5, 6, 4, 4, 2, 4]
    item2Remove = 4
    remove_all(remList, item2Remove)
    print(remList)
    
    return


def remove_all(arr, item):
    while item in arr:
        arr.remove(item)
        
main()