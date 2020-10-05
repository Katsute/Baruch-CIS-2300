#wl review
number = 0
while number < 10:
    if number % 2 == 0:
        print("Even")
        number += 1
    if number %2 != 0:
        print("Odd")
        number += 1
        
# for
for num in [1,2,3,4,5]:
    print(num)
    
for names in ["Aca","Ariana"]:
    print(names)

for weekdays in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print(weekdays)

for num in [1,3,5,7,9]:
    print(num)
    
# range
# ranges include first number (def:0) but not the last number

# for(int i = 0; i < 10; i++)
for num in range(10): # [0-10)
    print(num)
    
# for(int i = 1; i < 10; i+=2)
for num in range(1, 10, 2):  # (start, end, step)
    print(num)


# for(int i = 10; i > 0; i--)
for num in range(10, 0, -1):
    print(num)