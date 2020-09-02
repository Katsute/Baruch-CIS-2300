# typeof(String)
userName = "KC"
print(type(userName))                   # str

# typeof(num)
print(type(1))                          # int
print(type(1.0))                        # float (double)
print(type('1'))                        # str

# Stringformat
# money with comma and two float decimals
print("${:,.2f}".format(10000))         # $10,000.00

# Calculations
print(16/8)                             # inherently a float; no int overflow <3
print(int(16/8))                        # cast to int
print(17//3)                            # div w/o decimal (how java div normally works)
print(17%3)                             # remainder

# Print string join
print("first", "next", ' ')             # separator
print("first", "next", sep=", ")        # python supports specific parameters rather than strict java param order
print("escaped" '\n' '\t' "chars")      # \n \t ' "

# Variable assignment
# same naming conventions as java variables
# python keywords prohibited
Phone = 1234567

# Multiple variable assignment
# more ambiguity compared to java
a, b = 5, "hello"
print(a, b)

# Functions to know:
print(
    # input("input: "), '\n',
    max(1, 2), '\n',
    min(1, 2), '\n',
    int(2.5), '\n',
    abs(-5), '\n',
    type("str"), '\n',
    format("%s" % b)
)

print(open("09_01_2020.py", 'r').name)   # Same as new File("09_01_2020.py")
