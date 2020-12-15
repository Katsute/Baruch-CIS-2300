'''
1. Create a dictionary that keeps track of the USA’s Olympic medal count. 
Each key of the dictionary should be the type of medal (gold, silver, or 
bronze) and each key’s value should be the number of that type of medal 
the USA's won. Say, the USA has 33 gold medals, 17 silver, and 12 bronze. 
Create a dictionary saved in the variable medals that reflects this 
information.
'''
def ice5_1():
    
    medals = {
        'gold': 33,
        'silver': 17,
        'bronze': 12
    }
    
    print(medals)
    
    return

'''
(2) Update the value for "Phelps" in the dictionary swimmers to include 
his medals from the Rio Olympics by adding 5 to the current value 
(Phelps will now have 28 total medals). Do not rewrite the dictionary. 
Assume 

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 
            'Dirado':4, 'Phelps':23}
'''
def ice5_2():
    
    swimmers = {
        'Manuel':4, 
        'Lochte':12, 
        'Adrian':7, 
        'Ledecky':5, 
        'Dirado':4, 
        'Phelps':23
    }
    
    swimmers['Phelps'] += 5
    print(swimmers)
    
    assert(swimmers['Phelps'] == 28)  # check result
    return

'''
(3) Concatenate following dictionaries to create a new one. 
Sample Dictionaries:

d1={1:10, 2:20}

d2={3:30, 4:40}

d3={5:50, 6:60}

Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

HINT: You need to use list of dictionaries to loop over the three 
dictionaries using nested FOR loops. Do not use update or any other 
dictionary functions that we have not covered in the class. 
'''
def ice5_3():
    
    d1={1:10, 2:20}

    d2={3:30, 4:40}
    
    d3={5:50, 6:60}
    
    ds = [d1, d2, d3]
    
    d4 = {}
    
    for li in ds:
        for k, v in li.items(): # .items() returns a tuple <Key, Value>
            d4[k] = v
    
    print(d4)
    
    assert(d4 == {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}) # check result 
    return

'''
(4) Concatenate the following dictionaries to creata a new one. If a key 
repeats across the three dictionaries, you have to add the values 
corresponding to the key.

d1={1:10, 2:20}

d2={1:20, 3:30, 4:40}

d3={5:50,6:60,3:60}

Expected result: {1: 30, 2: 20, 3: 90, 4: 40, 5: 50, 6: 60}
'''
def ice5_4():

    d1={1:10, 2:20}

    d2={1:20, 3:30, 4:40}
    
    d3={5:50,6:60,3:60}
    
    ds = [d1, d2, d3]
    d4 = {}

    for li in ds:
        for k, v in li.items():
            if k not in d4:  # add new key if not in dictionary
                d4[k] = v
            else:            # otherwise increment the existing value
                d4[k] += v
                
    print(d4)
    
    assert(d4 == {1: 30, 2: 20, 3: 90, 4: 40, 5: 50, 6: 60}) # check result
    
    return

'''
2. Name and Email Addresses: Write a program using various functions 
that keeps names and email addresses in a dictionary as key-value pairs. 
The program should display a menu [write a function displayMenu] that 
lets the user to choose from following options:    
    - look up and return a person's email address if it exists 
      [write a function lookupEmail],     
    - add a new name and email address and return the updated 
      dictionary [write a function addEmail],     
    - change an existing email address and return the updated 
      dictionary [write a function updateEmail] and     
    - delete an existing name and email address and return the updated 
      dictionary [write a function deleteEmail].
'''

email = {'name': 'email@gg.ca'}

def ice5q2():
    options = {  # dictionary of methods (defined below)
        1: lookupEmail,
        2: addEmail,
        3: updateEmail,
        4: deleteEmail
    }
    
    while True:
        option = displayMenu()
        if not option:  # repeat until user enters no option
            break
        else:
            print("\n[", options[option](), "]\n")  # print result of method
            
    return

def displayMenu():
    print("Please select an option or [ENTER] to exit: ")
    print("[1] Look up email address")
    print("[2] Add new name and email")
    print("[3] Change email address")
    print("[4] Delete email address")  
    
    IN = input("> ")
    return None if IN == '' else int(IN)  # return null if blank
    
def lookupEmail():
    return email.get(input("Please enter name to search: "))

def addEmail():
    k = input("Please enter name to add: ")
    email[k] = input("Please enter email address: ")
    return email

def updateEmail():
    k = input("Please enter name to change email for: ")
    email[k] = input("Please enter new email address: ")
    return email

def deleteEmail():
    email.pop(input("Please enter name to delete: "))
    return email



################################################################

def main():
    q = [
        ice5_1,
        ice5_2,
        ice5_3,
        ice5_4,
        ice5q2
    ]
    for m in q:  # execute all above questions
        m()
        print('_'*50)

    
main()