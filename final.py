'''
You are working as a teaching assistant and have been maintaining 
grades of 100 students enrolled in an CHEM4444 class. Their grades 
in the 10 assignments are recorded in the file  
AllGrades_Chem4444.txt

(Tab separated). Each assignment is scored out of 100 points.  
As the end of the semester has approached, you have been asked 
to perform various calculations using this data.

 

To complete these tasks you will need to read the grades from 
text file appropriately using either lists or dictionaries. Once 
the file's contents are read, here are the calculation tasks that 
you need to complete.
'''
'''
(10 points) Write code that will calculate total final score for 
each student by summing up all the assignment. (hint: read 
text file; split function; list.append)
'''
file = open('AllGrades_Chem4444.txt', 'r')

grades = []
students = {}

for ln in file:
    if not ln.startswith("StudentID"):  # skip header row
        grades.append(ln.split("\t"))
file.close()

for student in grades:
    # create dictionary with student IDs as key and grade as value
    students[student[0]] = {"grades":[]}
    for grade in student[1:]:  # get grades as List<int>
        students[student[0]]["grades"].append(int(grade))
    students[student[0]]["total_final_score"] = sum(students[student[0]]["grades"])

'''
(20 points) Using this final score, write code to calculate 
final % grade (Assume all assignments are weighted equally) and 
the final letter grade based on the following craziest grading 
scheme:  (two dimensional list) 

- above [a] -- A  (90-100)

- above [b] and less than or equal to [a] -- B  (80-90)

- above [c] and less than or equal to [b] -- C  (70-80)

- above [d] and less than or equal to [c] -- D  (60-70)

- Below [d] -- F (below 60)
'''
ASSIGNMENTS = len(grades[0][1:])  # get num of columns (exclude id))
for student, v in students.items():  # <student id, dict>
    # get % grade
    v["percent_grade"] = v["total_final_score"] / ASSIGNMENTS
    # convert % grade to letter
    percent = v["percent_grade"]
    if percent > 90:
        v["letter_grade"] = 'A'
    elif percent <= 90 and percent > 80:
        v["letter_grade"] = 'B'
    elif percent <= 80 and percent > 70:
        v["letter_grade"] = 'C'
    elif percent <= 70 and percent > 60:
        v["letter_grade"] = 'D'
    else:  # given the above conditions this can only mean <= 60
        v["letter_grade"] = 'F'

'''
(10 points) Write code to display how many students got each of 
the above grades. e.g. x number of students got A, y number of 
students got B, and so on. (hint: count )
'''
# student dict contains only numeric keys and values except for letter grade
as_str = str(students)
class_grades = dict(  # count occurance (more efficient than for loop))
    A = as_str.count("A"), 
    B = as_str.count("B"), 
    C = as_str.count("C"), 
    D = as_str.count("D"), 
    F = as_str.count("E")
)
print("Class grades:", class_grades)

'''
(20 points) Along with original grades, write code to save back 
these three new columns (total final score, final % grade, and 
final letter grade) to a new text file. Name this new text file 
with your first and last name as firstnameLastname.txt
'''
OUT = ''
first = True
file = open('AllGrades_Chem4444.txt', 'r')  # must reopen b/c lines were already read
for ln in file:  # read existing lines
    if first:  # handle header row
        # append col to header row
        OUT += ln + "Total Final Score\tFinal % Grade\tFinal Letter Grade"
        first = False
    else:
        OUT += '\n'
        student_id = ln.split('\t')[0]  # retrive row id
        student = students[student_id]  # get dict
        # append new column (values) to student row
        OUT += ln + f"\t{student['total_final_score']}\t{student['percent_grade']}\t{student['letter_grade']}"
file = open("KC.txt", 'w')
file.write(OUT)
file.close()
'''
(10 points) Write code to calculate for each assignment the 
average score and show which students have the highest and 
lowest score for each assignment. 
'''

totals = {
    'HW-1': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-2': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-3': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-4': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-5': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-6': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-7': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-8': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-9': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100),
    'HW-10': dict(total = 0, MAX = [], LOW = [], max_gd=0, min_gd=100)
}
    
for g in grades:
    student = g[0]
    for i in range(len(g[1:])):
        total = totals["HW-" + str(i+1)]  # get hw dict (above)
        grade = int(g[i+1])  # get student grade for hw
        total['total'] += grade # increment toal for hw
        if grade > total['max_gd']:  # get max scr
            totals["HW-" + str(i+1)]['max_gd'] = grade
        if grade < total['min_gd']:  # get min scr
            totals["HW-" + str(i+1)]['min_gd'] = grade

STUD_NUM = len(grades) - 1
for k in totals.keys():
    totals[k]['avg'] = totals[k]['total']/STUD_NUM

# get students who equal min and max grade
for g in grades:
    student = g[0]
    for i in range(len(g[1:])):
        total = totals["HW-" + str(i+1)]  # get hw dict (above)
        grade = int(g[i+1])  # get student grade for hw
        total['total'] += grade  # increment toal for hw
        if grade == total['max_gd']:
            totals["HW-" + str(i+1)]['MAX'].append(student)
        elif grade == total['min_gd']:
            totals["HW-" + str(i+1)]['LOW'].append(student)

for k, v in totals.items():
    print(k, "avg:", v['avg'], "highest:", v['MAX'], "lowest:", v['LOW'])

'''
Rearrange the following statements to figure out how much the 
items in will cost. There are a few syntax errors and erroneous 
lines of code that you also need to fix.
'''
# dictionary of price of items

itemPrice = {'pasta': 1.59, 'ravioli':5.99, 'sauce':3.99, 'spinach':1.99, 'kale':2.99, 'yogurt':3.99, 'milk':2.99, 'cream':1.69, 'cheese':4.99, 'basil':.99, 'dill':1.99, 'bread':1.99}

# Create dictionary with items in shopping cart

shopperCart = {'pasta': 3, 'sauce':3, 'kale':2, 'milk':3, 'cheese':2, 'basil':1, 'dill':1, 'bread':1}

cartTotalPrice=0

for item in shopperCart.keys(): 
    cartItemCost = shopperCart[item]*itemPrice[item]
    cartTotalPrice += cartItemCost

print(f"Total Price is: ${cartTotalPrice:.2f}")