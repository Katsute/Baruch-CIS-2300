# Rainfall Problem:
'''
Rainfall Problem: Let’s imagine that you have a list that contains 
amounts of rainfall for each day, collected by a meteorologist. 
Her rain gathering equipment occasionally makes a mistake and 
reports a negative amount for that day. We have to ignore those. 
We need to write a program to (a) calculate the total rainfall by 
adding up all the positive integers (and only the positive integers), 
(b) count the number of positive integers (we will count with “1.0” so 
that our average can have a decimal point), and (c) print out the 
average rainfall at the end. Only print the average if there was 
some rainfall, otherwise print “No rain”. Construct the following 
code so that it correctly solves the rainfall problem
'''
'''
if day>=0:
sumRain = sumRain + day
count = count + 1.0
if count > 0:
else:
print("No rain")
avg = sumRain/count
sumRain=0
count=0
for day in rain:
print("Average rain is", avg)
rain = [0,5,1,0,-1,6,7,-2,0]
'''
def main1():
    sumRain=0
    count=0
    rain = [0,5,1,0,-1,6,7,-2,0]
    for day in rain:
        if day>=0:
            sumRain = sumRain + day
            count = count + 1.0
    if count > 0:
        avg = sumRain/count
        print("Average rain is", avg)             
    else:
        print("No rain")        
           
    
    return

# ICE12_2    
'''
Write a code to create a list variable called scores that has 
5 columns and 20 rows. Assume current values of all the elements 
in the list is 0. Use only the repetition operator. Once the 
scores variable is created with all 0s, update values in its 
rows and columns  using randint function in the range of 50-100.
'''
import random
def main2():
    # scores = [[0]*5]*20 
    # ^ can not be used because it clones a reference of the 
    # array [0,0,0,0,0] keeping all the row values the same
    
    scores = [None]*20 # create 20 rows
    for row in range(len(scores)):
        scores[row] = [0]*5 # create 5 columns per row
    
    # set random for each row/col
    for row in range(len(scores)):
        for col in range(len(scores[0])):
            scores[row][col] = random.randint(50, 100)
            
    print(scores)
            
    return


################################################################

def main():
    main1()  # run first problem
    main2()  # run second problem

main()