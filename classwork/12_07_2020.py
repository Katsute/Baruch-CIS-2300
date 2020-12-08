# remove & return
m = dict(key='value', key2='value')
v = m.pop('key', 'value')  # remove dict key and return or default
print(m, v, sep='\n')
v = m.pop('key2')  # remove dict key and return value
print(m, v, sep='\n')

# remove last item
# *note that before Python 3.7 this removes a random item

m = dict(a='v', b='v')
v = m.popitem()  # remove and return last entry
print(m, v, sep='\n')

# clear dict
m.clear()
print(m)

# files

file = open('file.txt', 'w')  # write option
file.write('test')
file.write('ln2')
file.close()
print(open('file.txt', 'r').read())

file = open('file.txt', 'a')  # append option
file.write('test')
file.write('ln2')
file.close()
print(open('file.txt', 'r').read())

print(open('file.txt', 'r').read())  # read

for line in open('file.txt', 'r'):  # print by line
    print(line)