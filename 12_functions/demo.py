# Functional Programming 

# Without Functions 

# User One Wants To Calculate Mathematical Operations For Below Values
num1 = 10
num2 = 5 

# Mathematical Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print('=' * 50)

# User Two Wants To Calculate Mathematical Operations For Below Values
num1 = 20
num2 = 10 

# Mathematical Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print('=' * 50)

# User Three Wants To Calculate Mathematical Operations For Below Values
num1 = 30
num2 = 10 

# Mathematical Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print('=' * 50)

# With Functions

def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# User One Wants To Calculate Mathematical Operations For Below Values
num1 = 10
num2 = 5 
math_ops()
print('=' * 50)
# User Two Wants To Calculate Mathematical Operations For Below Values
num1 = 20
num2 = 10 
math_ops()
print('=' * 50)
# User Three Wants To Calculate Mathematical Operations For Below Values
num1 = 30
num2 = 10 
math_ops()
print('=' * 50)

# math_ops(1,2) # TypeError: math_ops() takes 0 positional arguments but 2 were given

# Functions With Parameters 
def math_ops(num1, num2): # num1, num2 are Parameters
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'
math_ops(10,5)
print('=' * 50)
math_ops(20,10)
print('=' * 50)
math_ops(30,10)
print('=' * 50)

# Processes data 

def process_email(email_id):
    print(email_id.lower()+"@ai.com")

process_email("RaVI2KrISHna")
process_email("JoHN_kYLE")

print('=' * 50)

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","Ravi","ravi@gmail.com")  # without following order unexpected behavior  
print('=' * 50)
employee_info("Ravi","ravi@gmail.com","Hyderabad") # with order 
print('=' * 50)

# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")

employee_info("Hyderabad","Ravi","ravi@gmail.com")  # without following order unexpected behavior  
print('=' * 50)
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")
print('=' * 50)

# Without Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com",org_name="IBM")
print('=' * 50)
employee_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com",org_name="IBM")
print('=' * 50)
employee_info(emp_location="Bangalore",emp_name="Mike",emp_email="mike@gmail.com",org_name="IBM")
print('=' * 50)

# With Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="IBM"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")
print('=' * 50)
employee_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com")
print('=' * 50)
employee_info(emp_location="Bangalore",emp_name="Mike",emp_email="mike@gmail.com")
print('=' * 50)
employee_info(emp_location="Bangalore",emp_name="Doe",emp_email="doe@gmail.com",org_name="TCS")
print('=' * 50)

# Placement Requirement
# def employee_info(emp_name,emp_email,emp_location,org_name="IBM",emp_mobile):
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

# Non-default argument follows default argumentPylance
# SyntaxError: parameter without a default follows parameter with a default

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="IBM",):
    print(f"Hi {emp_name} your email is {emp_email} with mobile number {emp_mobile} and working for {org_name} at location {emp_location}")

employee_info(emp_location="Bangalore",emp_name="Doe",emp_email="doe@gmail.com",emp_mobile=99999)

print('=' * 50)

# Without Arbitrary Positional Arguments
def add_numbers(n1):
    print(n1)

def add_numbers_two(n1,n2):
    print(n1 + n2)
    
def add_numbers_three(n1,n2,n3):
    print(n1 + n2 + n3)
    
def add_numbers_ten(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    print(n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10)
    
add_numbers(1)
add_numbers_two(1,2)
add_numbers_three(1,2,3)
add_numbers_ten(1,2,3,4,5,6,7,8,9,10)

# Online Google Calculator 

print('=' * 50)

# With Arbitrary Positional Arguments
def add_numbers(*numbers):
    print(numbers)
    
add_numbers(1)
add_numbers(1,2)
add_numbers(1,2,3)
add_numbers(1,2,3,4,5,6,7,8,9,10)

print('=' * 50)

# Add Numbers 
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num 
    print(f"Total Sum Is {total}")

add_numbers(1)
add_numbers(1,2)
add_numbers(1,2,3)
add_numbers(1,2,3,4,5,6,7,8,9,10)

print('=' * 50)

# Profile Information 
def profile(*info):
    print(info)
    
profile("Ravi") 
profile("Ravi","Krishna") 
profile("Ravi","Krishna",34) 
profile("Ravi","Krishna",34,False,9.5,{"key":"hello"})

print('=' * 50)

# Real World Use Case w.r.t Ecommerce Cart Functionality 
def cart_value_total(*products):
    total_cost_cart = 0
    for product_price in products:
        total_cost_cart += product_price
    print(f"Total Cart Value is {total_cost_cart}")
    
cart_value_total(89) # only one product 
cart_value_total(89,595,1800) # only three product 

print('=' * 50)    