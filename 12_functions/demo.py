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

# Arbitrary Positional Arguments
def profile(*info):
    print(info)
    
profile("Ravi","Krishna",34) 

print('=' * 50)    

# Arbitrary Keyword Arguments
def profile(**info):
    print(info)

profile(fname="Ravi")     
print('=' * 50)    
profile(fname="Ravi",lname="Krishna",age=34) 

print('=' * 50)   

def profile(**info):
    for data in info:
        print(data) # Get Key

profile(fname="Ravi",lname="Krishna",age=34) 

print('=' * 50)   

def profile(**info):
    for data in info:
        print(info[data]) # Get Value

profile(fname="Ravi",lname="Krishna",age=34) 

print('=' * 50)   

# Real World Use Case -> https://i.ytimg.com/vi/tfZOZWVb81M/hq720.jpg?sqp=-oaymwEYCJUDENAFSFryq4qpAwoIARUAAIhC0AEB&rs=AOn4CLD61RCES1Oo8OL919n3tkbqnBt2yA

# Real World Use Case -> jan=3000, feb=4500, mar=9000 

# Real World Use Case -> jan=2000, feb=4000, mar=5000, apr=1000, may=2000, jun=4000

# Requirement: Calculate Total Transactions Amount and Number Of Transactions Made 
# Real World Use Case -> jan=3000, feb=4500, mar=9000 (16500 - 3 Transactions)
# Real World Use Case -> jan=2000, feb=4000, mar=5000, apr=1000, may=2000, jun=4000 (18000 - 6 Transactions)

def bank_transactions(**transactions):
    print(transactions)
    
    total_transactions_value = 0 
    total_transactions_count = 0 
    
    for transaction in transactions:
        # total_transactions_value += transaction # transaction = jan, feb, mar # TypeError: unsupported operand type(s) for +=: 'int' and 'str'
        total_transactions_value += transactions[transaction] # transaction = 3000, 4500, 9000
        total_transactions_count += 1
    print(f"Total Transactions Amount Is {total_transactions_value} for {total_transactions_count} Transactions")    
        
bank_transactions(jan=3000, feb=4500, mar=9000)

print('=' * 50)

bank_transactions(jan=2000, feb=4000, mar=5000, apr=1000, may=2000, jun=4000)

print('=' * 50)

# Without return 
def add(a,b):
    a + b 

add(10,5)
print(add(10,5))

# With return 
def add(a,b):
    return a + b 

add(10,5)
print(add(10,5))

print('=' * 50)


# Problem 
# def add(a,b):
#     print(a+b)
    
# # function composition
# def sub(c,d,e): # c + d - e 
#     print(add(c,d) - e) # None - 5 TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
    
# sub(3,4,5) # None - 5 = 2

# Problem Fix With return
def add(a,b):
    return a + b 
    
# function composition
def sub(c,d,e): # c + d - e 
    print(add(c,d) - e) 
    
sub(3,4,5) # 7 - 5 = 2

print('=' * 50)

# If you use return, Make sure it's the last part of statement to be executed 
def add(a,b):
    print("Calculations Started")
    return a + b 
    print("Calculations Completed") # Code is structurally unreachable
    
print(add(1,2))
    
print('=' * 50)

# if you have multiple return statements, first return will be considered 
a = 50
b = 60
a = 70 

print(a) # 50 

print('=' * 50)

def math_ops(a,b):
    return a + b 
    return a - b # Code is structurally unreachable
    return a * b # Code is structurally unreachable 

print(math_ops(2,3)) # 5

print('=' * 50)

# def math_ops(a,b):
#     return a + b return a - b 
#     return a + b, return a - b 

def math_ops(a,b,operator):
    if operator == "+":
        return a + b 
    elif operator == "-":
        return a - b 
    elif operator == "*":
        return a * b 
    else:
        return "Invalid Operator Given"

print(math_ops(2,3,"+"))
print('=' * 50)
print(math_ops(2,3,"*"))
print('=' * 50)
print(math_ops(2,3,"$"))
print('=' * 50)

# Local Scope: lifetime exists only within the function

def add(): 
    la = 10 # local - inside the function
    lb = 20 # local - inside the function
    
    # accessing within the function
    print(la)
    print(lb)
    
add()

# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?
# print(lb) # NameError: name 'lb' is not defined. Did you mean: 'b'?

print('=' * 50)    

def add(la,lb): # la and lb are local scope 
    print(la)
    print(lb)

add(1,2)

# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?
# print(lb) # NameError: name 'lb' is not defined. Did you mean: 'b'?

print('=' * 50) 

# Global Scope 
ga = 100 # Global Scope - outside function

def add(la,lb):
    print(la)
    print(lb)
    print(ga) # inside function - accessing global variable 
    
add(3,4)

print(ga) # outside function - accessing global variable 

print('=' * 50) 

# name conflicts
ga = 500 # Global Scope - outside function

def add(la,lb,ga): # ga is local scope 
    print(la)
    print(lb)
    print(ga) # preference is given to local variable
    print(globals()['ga']) # point to 500 i.e global scope 

add(5,6,7)

print('=' * 50) 

# global variable outside function
count = 0
print(count)
count += 1
print(count)

print('=' * 50) 

# global variable inside function
count = 0
print(count)
def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count 

print(increment())

print('=' * 50) 

# Without Lambda Functions 
def add(a,b):
    return a + b 

print(add(10,20))

print('=' * 50) 

# With Lambda Functions 
# lambda arguments:expression  

lambda a,b:a+b 
print(lambda a,b:a+b)
# print(()())
# print((lambda_function)(arguments)) # IILE
print((lambda a,b:a+b) (4,5)) # IILE 

print('=' * 50) 

# Without Lambda Functions 
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False

print(is_even_num(11))

print('=' * 50) 

print(is_even_num(12))

print('=' * 50) 

# With Lambda Functions 
# lambda arguments:expression 
# print((lambda a,b:a+b) (4,5)) # IILE 
lambda num:num % 2 == 0 
print((lambda num:num % 2 == 0) (4)) # IILE 
print('=' * 50) 
print((lambda num:num % 2 == 0) (5)) # IILE 
print('=' * 50) 

# Without Lambda Functions 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")

print('=' * 50) 

# With Lambda Functions 
# lambda arguments:expression 
# print((lambda a,b:a+b) (4,5)) # IILE 
lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
print((lambda emp_name,emp_email,emp_location:(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")) (emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")) # IILE 

print('=' * 50) 