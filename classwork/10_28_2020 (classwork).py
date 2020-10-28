# In-class exercise
# input a number, iterate 5 times, and get running total;
def main():
    total = 0
    for _ in range(5):
        num = float(input("Please enter a number: "))
        total += num
    print("Total:", total)
    
main()