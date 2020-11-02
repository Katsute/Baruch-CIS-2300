def show_interest(principal, rate, periods):
    print(principal, rate, periods)


# (positional arg, keyword arg, keyword arg)
show_interest(10_000.0, rate=0.01, periods=10)

# (positional arg, keyword arg, ? arg)
# show_interest(10_000.0, rate=0.01, 10)  # pos arg not allowed after kw arg

# (positional arg, positional arg, used keyword arg)
# show_interest(10_000.0, 10, rate=0.01)  # kw arg can not override pos arg


# random

import random as rd

# [1-10] (inclusive)
print(rd.randint(1, 10))

# [0-1) (0-1 except exactly 1.0)
print(rd.random())


import random as rd

def rollDice(lowest, highest):
    value1 = rd.randint(lowest, highest)
    value2 = rd.randint(lowest, highest)
    print(value1, value2)
    return value1, value2
    # expressions after return are not processed but also doesnt throw a syntax error

def main():
    n1 = int(input("Lowest number: "))
    n2 = int(input("Highest number: "))
    retVal1, retVal2 = rollDice(n1, n2)
    print(retVal1, retVal2)
    
main()


# math

import math
from math import log

print(log(10))