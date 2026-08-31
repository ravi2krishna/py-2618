# This is Comment 
# This is Comment 
print()
print(10)
print(10.5)

# print(five) # NameError: name 'five' is not defined

print('five')
print("ten")

# Identifier Rules 
# 2day = "monday" # SyntaxError: invalid decimal literal
# print(2day)

today = "monday"
print(today)

day2moro = "tuesday"
print(day2moro)

# $2moro = "tuesday" # SyntaxError: invalid decimal literal
# print($2moro)

_2moro = "tuesday" 
print(_2moro)

# Improper Way Of Naming Identifiers 
x = "Ravi"
y = 25
z = 9.5 


# Proper Way Of Naming Identifiers 
# student name = "Ravi"
student_name = "Ravi"
student_age = 25
student_gpa = 9.5 

# Static Data (Fixed Data)
math_pi = 3.14159265359 # Not Recommended
print(math_pi)

MATH_PI = 3.14159265359 # Recommended
print(MATH_PI)

STUDENT_AADHAR_ID = 123456789012 # Recommended
print(STUDENT_AADHAR_ID)