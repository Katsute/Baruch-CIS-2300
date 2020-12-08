# TOC

- [General Concepts](#general-concepts)
- [String](#string)
- [Math](#math)
- [Boolean](#boolean)
- [Conditionals](#conditionals)
- [While Loops](#while-loops)
- [For Loops](#for-loops)
- [Lists](#lists)
- [Tuples](#tuples)
- [Dictionaries](#dictionaries)
- [Functions](#functions)
- [Libraries](#libraries)

# General Concepts

## Variables

  - Variables may only use alphanumeric characters and `_`.
  - Variables may not start with a number.
  - Variables can use built-in function names but this will override the value.

Single variable assignment
```python
a = 1
b = 's'
```
Multiple variable assignment
```python
a, b = 1, 's'
```

## Type

Returns the type of the object.

`type(Object)`
```python
type('string')  # string
type(1)  # int
type(1.0)  # float
```

## Casting

Casts the object to a datatype.

`str(Object)`
```python
str(1)  # "1"
str(1.0)  # "1.0"
str(False)  # "False"
```

# String

Things to note:
  - String concatentation only works with string types. You must cast objects using [`str(Object)`](#Casting) to concatenate them.
  - Escape special characters like `\n` or `\t` using an additional back slash `\`.
    ```python
    "\\n"  # "\n"
    ```
  - A full string can be escaped using a literal string.
    ```python
    r'\n'  # "\n"
    ```

## Input

Ask for user input. This value will always be a string.

`input(string)`

```python
value = input("Please enter value: ")
```

## Print

Print a text.

`print(string...)`

```python
print("first", "next")  # first next
```

`print(string..., sep=string)`

```python
print("first", "next", sep='+')  # first+next
```

## String Format (f-strings)

### Number Formats
```python
# '.2f' ; as a two point float
f"{10:.2f}"  # 10.00

# '.2%' ; as a two point percent
f"{.10:.2%}"  # 10.00%

# '.2e' ; as a two point scientific number
f"{10:.}"  # 1.00e+01
```
### Whitespace
```python
# String with set width
f"{'Hello':25}"   # "Hello                    "

# Left aligned string
f"{'Hello':<25}"  # "Hello                    "

# Right aligned string
f"{'Hello':<25}"  # "                    Hello"

# Center aligned string
f"{'Hello':^25}"  # "          Hello          "
```

## String Conditionals

### Equals

```python
# Test if strings are equal
"string" == "String"  # False

# Test if string is shorter
"str" > "string:"  # False

# Test string alphabetical order
"a" > "b"  # False
```

### Contains

```python
"he" in "hello"  # True

"he" not in "hello"  # False
```
```python
# Get first index occurance of string or -1 if not found
"hello".find("e")  # 1

# Get number of string occurances or -1 if not found
"hello".count("l") # 2
```

### Common Methods

```python
# If each in string is alphanumeric
"a1".isalnum()  # True
"a 1".isalnum()  # False

# If each in string is alphabetic
"aa".isalpha()  # True

# If each in string is a digit
"1".isdigit()  # True
"2.0".isdigit()  # False

# If each in string is lowercase
"ab".islower()  # True
"Ab".isLower()  # False

# If each in string is uppercase
"AB".isupper()  # True
"Ab".isupper()  # False

# If each in string is a whitespace
" \n\t".isspace()  # True
```
```python
# If string starts with
"ab".startswith("a")  # True

# If string ends with
"ab".endswith("b")  # True
```

## Character Loop

Strings can be iterated through as a string array.

```python
text = "abcd"
for c in text:
    print(c)
# a
# b
# c
# d
```

## String Manipulation

Things to note:
  - Strings are immutable, modification will create a new string.
  - Strings can be instantiated using double quotes `"` or single quotes `'`.

```python
# String repetition
"s"*5  # "sssss"

# String split
"a, b, c".split(", ")  # ["a", "b", "c"]
```

### Substring

All values for substring are optional.
  - First value is the start index.
  - Second value is the end index (not included).
  - Third value is the step value.

```python
# Return string from start to end (end index is not included)
"substring"[0:3]  # "sub"

# Returns string from start to end (relative from the right side)
"substring"[-6:]  # "string"

# Returns string from start to end (relative from the right side)
"substring"[:-6]  # "sub"

# Returns string at index
"substring"[0]  # "s"

# Returns string by step value
"0123456789"[0:10:2]  # "02468"
```

### Common Methods

```python
# String to lowercase
"AA".lower()  # "aa"

# String to uppercase
"aa".upper()  # "AA"

# Capitalize string
"aa".capitalize()  # "Aa"
```
```python
# Remove whitespace from left
" abc<>123 ".lstrip()  # "abc<>123 "

# Remove any from list from left
" abc<>123 ".lstrip("123 abc")  # "<>123 "

# Remove whitespace from right
" abc<>123 ".rstrip()  # " abc<>123"

# Remove any from list from right
" abc<>123 ".rstrip("123 abc")  # " abc<>"

# Remove whitespace from both sides
" abc<>123 ".strip()  # "abc<>123"

# Remove any from list from both sides
" abc<>123 ".rstrip("123 abc")  # "<>"
```
```python
# Replace string with another string
"hello".replace("h", "m")  # mello
```

# Math

Things to note:
  - Python uses floats as the decimal type. This means you will encounter floating point precision errors.

## Multiplication

```python
10*2  # 20

# power
10**2  # 100
```

## Division

```python
16/5  # 3.2

# casting to int will remove decimal
int(16/5)  # 3

# divide without remainder
16//5 # 3
```

## Common Methods
Works for both `float` and `int`.

|method|description|
|-|-|
|`max(float, float)`|returns the maximum value|
|`min(float, float)`|returns the minimum value|
|`abs(float)`|returns the absolute value|


# Boolean

`True` and `False`

|condition|description|
|-|-|
|`>`|greater than|
|`<`|less than|
|`>=`|greater than or equal to|
|`>=`|less than or equal to|
|`==`|equal to|
|`!=`|not equal to|

# Conditionals

```python
if condition:
    print("Print if True")
elif otherCondition:
    print("Print if first False and this True")
else
    print("Print if none above")
```

# While Loops

```python
while condition:
  print("Execute while condition is true")
```

# For Loops

## Range

Generate an array to be used in a for-index loop.
  - The first optional parameter is the starting index (included). If not included it is presumed to be 0.
  - The second parameter is the ending index (not included).
  - The third optional parameter is the step value (default is 1).  

`range(int, int, int)`

```python
for i in range(0, 10, 2):
    print(i)
# 0, 2, 4, 6, 8
```

# Lists

Things to note:
  - Lists are mutable, the values can be changed.
  - List values are mutable, a list contains the references to the original values.
  - Lists start at index `0`.

Instantiate lists using `[]`. Retrieve values using indexes.

```python
li = ["a"]
li[0]  # "a"
```

## Iterator

Iterate through items in a list using a [for loop](#for-loops).

```python
li = []
for i in li:
    print(i)
```

## List Conditionals

```python
li = ["a", "b"]

# If list contains
"a" in li  # True
"b" not in li  # False
```

## List Manipulation

```python
# Append to end of list
li = ["a"]
li += "b"  # ["a", "b"]

# Repeat in array
li = ["a"]*5  # ["a", "a", "a", "a", "a"]

# Reassign in array (only existing indexes)
li = ["a", "b"]
li[0] = "c"  # ["c", "b"] 

# Append array
li = ["a", "b"]
li += li  # ["a", "b", "a", "b"]
```

### Common Methods

```python
# Append to end of list
li = ["a"]
li.append("b")  # ["a", "b"]

# Insert and shift in list
li = ["a","c"]
li.insert("b", 1)  # ["a", "b", "c"]

# Remove from list (only one value)
li = ["a", "a"]
li.remove("a")  # ["a"]
```
```python
# Sort list
li = [5, 4, 3, 2, 1]
li.sort()  # [1, 2, 3, 4, 5]

# Reverse list
li = [1, 2, 3, 4, 5]
li.reverse()  # [5, 4, 3, 2, 1]
```

## Common Methods

```python
# Retrieve from index
li = ["a"]

li[0]  # "a"
li.index(0)  # "a"

# Get minimum value
li = [2, 1]
min(li)  # 1

# Get maximum value
li = [2, 1]
max(li)  # 2

# Get length
li = ["a", "b"]
len(li)  # 2
```

## List Duplication

Assigning a list to a variable copies the reference not value. Any changes in either list will change all the variables with the same list.

```python
list1 = [1, 2]
list2 = list1
list2 += [3, 4]

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 3, 4]
```

Copying a list will create a new list with a copy of the references.

```python
list1 = [1, 2]
list2 = list1.copy()
list2 += [3, 4]

# list1 = [1, 2]
# list2 = [1, 2, 3, 4]

list1 = [1, 2]
list3 = [list1]
list1[0] = 2  # [2, 2]

# list1 = [2, 2]
# list3 = [[2, 2]]
```

# Tuples

Things to note:
  - Tuples are immutable, the references can not be changed.

```python
tup = 1, 2, 3
tup = (1, 2, 3)
```

# Dictionaries

Things to note:
  - Dictionaries can be assigned with any immutable key.

```python
d = {'k':'v'}
d = dict(key='v')
```

## Dictionary Conditionals

```python
# Check if contains key
d = {'k':'v'}
'k' in d  # True
'v' not in d  # True
```

## Dictionary Modification

```python
# Change key value
d = {'k':1}
d['k'] = 'v'  # {"k":"v"}

# Delete key value
del d['k']  # {}
```
```python
# remove and return
d = {'k':'v'}
d.pop('k')  # "v"

# remove and return or default
d = {}
d.pop('k', 'v')  # "v"
# d = {}

# remove last item*
d = {'a':1, 'b':2}
d.popitem()  # 1
# d = {'b':2}

# clear dictionary
d = {'k':'v'}
d.clear()  # {}
```
*\*before Python 3.7 this removes a random item*

## Common Methods

```python
d = {'k':'v'}

# iterate through keys
for key in d.keys():
    print(key)  # "k"

# iterate through values
for val in d.values():
    print(key)  # "v"

# iterate through items
for item in d.items():
    print(key[0], key[1]) # "k v"

# get without error
d = {}
d.get('k')  # None

# get or default
d = {}
d.get('k', 'v')  # "v"
```

# Functions

Things to note:
  - Functions follow the same naming conventions as [variables](#variables).
  - Variables created in the function are only visible in the function.
  - Variables modified in the function are only visible in the function, they will not change global variable values.
    ```python
    v = 1
  
    def main():
        v = 2  # outer variable is still 1
  
    main()
    ```
  - Global variables can only be modified if the function explicetly states them as global.
    ```python
    v = 1
  
    def main():
        global v
        v = 2  # sets outer v to 2
  
    main()
    ```

Function names are defined as:

`def function_name(parameters)`

```python
def function_name(parameters):
    print(parameters)
    return
```

Functions are called using:

`function_name(parameters)`

```python
function_name("Hello")
```

## Keyword Arguments

Things to note:
  - Any unnamed arguments are required.
  - Keyword arguments can be set in any order.
  - Positional arguments may not come after keyword arguments.

```python
def function_name(required_arg, keyword_arg=1):

    return

function_name("required")
function_name("required", keyword_arg=2)

function_name(keyword_arg=2, "required")  # not allowed
```

## Recursion

Call a method recursively. This is not recommended as it will create a new function in memory each time. A [for loop](#for-loops) is recommended instead.

```python
def main():
    message(5)
    
def message(times):
    if times > 0:
        print("This is a recursive function.")
        message(times - 1)

main()
```

# Libraries

Things to know:
  - Imports can use aliases by importing them using import as.
    ```python
    import random as rand
    rand.randint(1, 10)
    ```

## Random

`random.random()`

```python
import random
random.random()  # random float between 0 and 1 (including 0 but not 1)
```

`random.randint(start, end)`

```python
import random
random.randint(1, 10)  # random int between 1 and 10 (including start and end)
```

## Pandas

```python
import pandas as pd

df = pd.read_csv(r"file.csv", skiprows=1)  # read a csv file skipping header row

pd.set_option("display.max_rows", 10)  # display maximum 10 rows
pd.set_option("display.max_columns", 10)  # display maxmimum 10 columns

df.iloc[0]  # first row
df.iloc[-1]  # last row (first from end)

df.iloc[0:5, 1:2]  # rows 0-5 with columns 1:2

df.fillna(value = 0)  # fill N/A values with default

left = pd.DataFrame({"col": ["value", "value"], "col2": [1, 2]})
right = pd.DataFrame({"col": ["value", "value"], "col3": ["another", "value"]})
merge = pd.merge(left, right)  # merge on matching columns
```
