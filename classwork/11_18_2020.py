# substring
print("substring"[0:3])      # same as Java, last index is not included
print("substring"[-6:])      # substring start relative to end, unset is len
print("substring"[:-6])      # substring end relative to end, unset is first (0)
print("substring"[0])        # string index
print("0123456789"[0:10:2])  # third value is step value

# contains (in)
text ="What is CFA, CPA, and ACCA?"
print("Not found" if "what" in text else "It is not found")  # contains = in
print("Not found" if "CPC" not in text else ("It is not found"))

# logical
print(text.isalnum())  # is alphanumeric (no whitespace)
print(text.isalpha())  # is all alphabetic (no whitespace)
print(text.isdigit())  # is all number (no whitespace)
print(text.islower())  # is all lowercase
print(text.isupper())  # is all uppercase
print(text.isspace())  # is all whitespace \n, \t)

# char loop
text = "\tabcdefghijklmnopqrstuvwxyz\n"
for c in text:  # char loop
    char = c  # if any can be achieved by checking each char
    
# string modification
# (similar to Java, strings are immutable, method creates new string)
print(text.lower())             # to lower
print(text.upper())             # to upper
print(text.strip().capitalize())# capitalize first char only

# strip to remove leading/trailing, this does not remove all
# the string is essentially an array of characters to be considered for removal
print(text.lstrip())            # strip leading whitespace
print(text.lstrip("abc\t"))     # strip leading chars
print(text.rstrip())            # strip trailing whitespace
print(text.rstrip("\nxyz"))     # strip trailing chars
print(text.strip())             # strip leading and trailing whitespace
print(text.strip("\n\tabcxyz")) # strip leading and trailing chars

# full string modification
print(text.endswith("abc"))     # ends with
print(text.startswith("abc"))   # starts with
print(text.find("abc"))         # index of (first), -1 means not found
print(text.count("a"))          # count
print(text.replace("\t", ""))   # replace

# string repetition
print("c" * 10)

for c in range(1, 10):
    print("*" * c)

# string split
print("11/18/2020".split('/'))