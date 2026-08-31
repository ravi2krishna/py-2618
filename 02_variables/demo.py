# Variables

# Assign Data (Store Data)
student_name = "Ravi" 
student_age = 25
student_gpa = 9.5 
student_passed = True # Correct (Student has passed)
student_present = False # InCorrect (Student not present today)
STUDENT_AADHAR = None # Absence Of Value 

# Retrieve Data (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(student_present)
print(STUDENT_AADHAR)

# Concatenation: Joining Strings Using + Operator 
print("========== Student info ==========")
print("Student Name: " + student_name)
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ", student_age) # Using , Operator 
print("Student GPA: ", student_gpa)
print("Did Student Pass: ", student_passed)
print("Did Student Present Today: ", student_present)
print("Student AADHAR ID: ", STUDENT_AADHAR)
print("========== Student info ==========")