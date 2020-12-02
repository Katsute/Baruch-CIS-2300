# dictionaries (aka Java Maps)

d = {'k':'v'}
print(d['k'])
d = dict(key = 'v')
print(d['key'])

# check contains key
print('key' in d)
print('v' not in d)

# any immutable type of key (no arrays)

d = {
     (1, 2, 3): "tuple",
     "abc": "string",
     999: "num"
}

# update/new dict value
d['k'] = 'v'

# remove key
del d['k']

# k/v arr
for key in d.keys():
    print(key)
    
for value in d.values():
    print(value)
    
# items as tuple
for tu in d.items():
    print(tu[0], tu[1])
    
# get key or default w/o error

print(d.get('null'))