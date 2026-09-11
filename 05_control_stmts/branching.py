# Branching Structures (Jump Statements)

for num in range(1,11,1):
    print(num)
    
print("==============")

# break: Helps exit a loop early (break)  
for num in range(1,11,1):
    # stop the loop when num becomes 5
    if num == 5:
        break
    print(num)
    
print("==============")

# continue: Helps Skip The Current Iteration
for num in range(1,11,1):
    # skip the 5th Iteration
    if num == 5:
        continue
    print(num)

print("==============")

# pass - acts as a placeholder, does nothing 
# Requirement - To Perform Some Operations in the Future 
# When Salary is above 25000, we want to do something in the Future 
# emp_salary = 15000

# emp_salary = 15000
# if emp_salary > 25000: # IndentationError: expected an indented block after 'if' statement on line 32
    
emp_salary = 15000
if emp_salary > 25000:
    pass # ___________ # park 

# Other Operations You Can Work On 
print("Working With Other Functionalities")

# After 6 Months 
# When Salary is above 25000, we want to Promote Employee as Permanent Employee 
emp_salary = 35000
if emp_salary > 25000:
    print("Promoted as Permanent Employee ")
    
# Working With OOP 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_gpa = 9.2
    student_enrolled_courses = ["python","ai","cloud"]
    
# Trainer 
class Trainer:
    pass 

# Mentor 
class Mentor:
    pass 

# Institute 
class Institute:
    pass 