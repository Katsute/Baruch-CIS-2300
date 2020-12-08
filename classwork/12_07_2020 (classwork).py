'''
(ICE5_Q1) Create a dictionary that keeps track of the USA's 
Olympic  medal count. Each key of the dictionary should be 
the type of medal (gold, silver, or bronze) and each key's 
value should be the number of that type of medal the USA's 
won. Say the USA has 33 gold metals, 17 silver, and 
12 bronze. Create a dictionary saved in the variable medals 
that reflects this information. 
'''
def ice5q1():
    
    medals = {
        'gold': 33,
        'silver': 17,
        'bronze': 12
    }
    
    print(medals)
    
    return

'''
(ICE5_Q2) Name and Email Addresses: Write a program using 
various functions that keeps names and email addresses in a 
dictionary as key-value pairs. The program should display a 
menu [write a function displayMenu] that lets the user choose 
from the following options:
    
- look up and return a person's email address if it exists
  [write a function lookupEmail]
- add a new name and email address and return the updated
  dictionary [write a function addEmail]
- change an existing email address and return the updated
  dictionary [write a function updateEmail]
- delete an existing name and email address and return the
  updated dictionary [write a function deleteEmail]
'''

email = {'name': 'email@gg.ca'}

def ice5q2():
    option = displayMenu()
    
    options = {
        1: lookupEmail,
        2: addEmail,
        3: updateEmail,
        4: deleteEmail
    }
    
    print(options[option]())
    
    return

def displayMenu():
    print("Please select an option: ")
    print("[1] Look up email address")
    print("[2] Add new name and email")
    print("[3] Change email address")
    print("[4] Delete email address")  
    
    return int(input("> "))
    
def lookupEmail():
    return email.get(input("Please enter name to search: "))

def addEmail():
    k = input("Please enter name to add: ")
    email[k] = input("Please enter email address: ")
    return email

def updateEmail():
    k = input("Please enter name to change: ")
    email[k] = input("Please enter email address: ")
    return email

def deleteEmail():
    email.pop(input("Please enter name to delete: "))
    return email



################################################################

def main():
    ice5q1()
    print('_'*40)
    ice5q2()
    
main()