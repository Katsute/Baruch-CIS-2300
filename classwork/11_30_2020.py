# list slicing [start:end:step]

numbers = [1, 2, 3, 4, 5]

my_list = numbers[2:4]
print(my_list)

my_list = numbers[-3:-1]  # from right side
print(my_list)

# search

print(2 in numbers)
print(0 not in numbers)

# index

print(numbers.index(2))

# sort

numbers = [5, 4, 3, 2, 1]
numbers.sort()
print(numbers)

print(min(numbers))
print(max(numbers))

# reverse

numbers.reverse()

print(numbers)
print(len(numbers))
print(type(numbers))

# list copy

num = numbers.copy()  # only makes new array, references are the same
num = numbers[:]  # also copy using slice

list1 = [3, 4]
list2 = list1  # this makes the REFERENCE equal, this doesn't create a copy
list2 += [5, 6]  # this also changes list1 to match

# enumerate

list3 = [1, 2, 2, 3, 4]
list4 = [i for i, x in enumerate(list3) if x == 2]

# tuple assignment, immutable

tuple1 = 1, 2, 3
tuple2 = (1, 2, 3)
print(tuple1, tuple2)

# dict/map

db = {
      "col": [1, 2, 3],
      "col2": [4, 5, 6]
}

db['col'] = num # overwrite a column/kv (copies REFERENCE)