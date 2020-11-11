# Factorial
# n! = n * (n-1) * (n-2) ...
# 3! = 3 * 2 * 1


def main():
    n = int(input("Positive integer: "))
    print(factorial(n))

def factorial(n):
    product = 1
    # multiply by all nums between n & 1
    # can start at 2 because anything times 1 has no change
    for i in range(2, n+1):  
        product *= i
    return product

def factorial(n):
    return 1 if n == 1 else n * factorial(n-1)

main()

# Sum

def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start+1, end)
    
def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(range_sum(numbers, 3, 7))
    
main()

# Fibonacci
# 0, 1, 1, 2, 3, 5, 8
# next num is sum of two previous
# n = 0 ? 0
# n = 1 ? 1
# n > 1 ? fib(n-1) + fib(n-2)

def fib(n):  # returns num in fib sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def main():
    n = int(input("Positive integer: "))
    for i in range(n):
        print(fib(i))
    
main()