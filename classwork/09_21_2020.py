# ex1
name1, name2 = "Mary", "Mark"
if name1 == name2:
    print("The names are the same.")
else:
    print("The names are NOT the same.")
    
# ex2
month = None
if month != "October":
    print("This is the wrong time for Octoberfest!")

# ex3
password = input("Enter the password: ")
if password == "prospero":
    print("Password accepted.")
else:
    print("Sorry, that is the wrong password.")
    
# strings can be sorted alphabetically
# and by length (shorter words first)
name1 = input("Name 1: ")
name2 = input("Name 2: ")
print("Names listed alphabetically")
if name1 < name2:  # if name1 is alphabetically higher than name2
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
    
# if; else if; else
cond = False
if cond:
    "statement"
elif cond:
    "statement"
else:
    "statement"

# ex4
MIN_SALARY, MIN_YEARS = 40000.0, 2

salary = float(input("Enter your annual salary: "))
years_on_job = int(input("Enter the number of" + " years employed: "))

if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print("You qualify for the loan.")
    else:
        print("You must have been employed", "for at least", MIN_YEARS,"years to qualify.")
else:
    print("You must earn at least $",format(MIN_SALARY, ",.2f")," per year to qualify.", sep='')