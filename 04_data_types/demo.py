# Data Types

# Numeric Types 

data = 10 
print(type(data))

data = -10 
print(type(data))

data = 10.5 
print(type(data))

data = -10.5 
print(type(data))

# complex number -> a + ib 
# data = 3 + i5 # Error
# print(type(data))

data = 3 + 5j # No Error
print(type(data))

data = True
print(type(data))

data = False
print(type(data))

data = None
print(type(data))

data = "hello there"
print(type(data))

# Complex Data Types 

# Lists
data = [10,20,30,40,50]
print(type(data))

# Tuples
data = (10,20,30,40,50)
print(type(data))

# Sets
data = {10,20,30,40,50}
print(type(data))

# Dictionaries
data = {"course":"python","timing":10,"location":"hyderabad"}
print(type(data))

# Custom Datatype For Student
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_gpa = 9.2
    student_enrolled_courses = ["python","ai","cloud"]
    
data = Student() # object creation 
print(type(data))
print(data.student_name)

# Type Conversion / Implicit Conversion [Automatic]
n1 = 10 # int 
n2 = 5.5 # float
sum = n1 + n2 
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion [Manual]
price = 1128.23 # float 
print(price)
print(type(price))
# Round Off Price 
round_off_price = int(price) 
print(round_off_price)
print(type(round_off_price))

# How casting is needed in Real World Applications 
# Some User In Web Site Was Filling Form (text boxes) -> Behind the scenes these are Strings 
rating = "2" # string, as it's a input in website 
print(type(rating))
# if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
rating = int(rating) # casting 
print(type(rating))

if rating >= 4:    
    print("Positive Feedback")
else:
    print("Negative Feedback")