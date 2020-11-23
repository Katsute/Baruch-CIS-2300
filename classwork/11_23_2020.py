# lists are mutable (unlike java arrays)

arr = ["a"]
arr += "b"  # append to arrays (lists)

arr = list(range(1, 10, 2))  # range as list

arr = ["a"] * 5  # array repetition

# iterator
myList = ["hello", "hi", "hey", "Morning!", "Today", "is", "Nov", 15, 2019, 11.10]

for e in myList:
    print(e)
    
# indexed loop
for index in range(len(myList)):
    print(myList[index])
    
# while loop
index = 0
length = len(myList)
while index < length:
    print(myList[index])
    index += 1
    
print("―"*50)

# array reassignment

arr[0] = 0  # reassigns only indexes that already exist

# list modification

arr += arr  # append list to list

arr.append('a')  # also append

arr.insert(2, "b")  # insert & shift

arr.remove("a")  # remove first matching

# remove all
remList = [1, 2, 3, 4, 5, 6, 4, 4, 2, 4]
item2Remove = 4
while item2Remove in remList:
    remList.remove(item2Remove)