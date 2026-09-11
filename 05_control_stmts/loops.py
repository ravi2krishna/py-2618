# Looping Structures (Iteration Statements) - Repetition

# while Loop 
# while True: # Always True -> This Forms Infinite Loop 
#     print("Repeat....")
#     print("Code............")
    # To Terminate Above Loop Use Control + c 

while False: # Always False -> Never Executes This Block Of Code
    print("Repeat....")
    print("Code............")
    
# Counters 
count = 1
while count <= 5:
    print("Count Is: ",count)
    count += 1

print("=================")

# Generate Employee ID's 
emp_id = 10001
while emp_id <= 15001:
    print("Employee ID Generated: ",emp_id)
    emp_id += 1

print("=================")

# Use while loop when we don't know number of Iterations/Repetitions in advance

# You Found A Lost Phone, Trying To Break The Password / PIN 
# Tell Me At Which Attempt, The Phone Will Be Unlocked ?? 

actual_pin = "2345"
user_given_pin = ""

while user_given_pin != actual_pin:
    user_given_pin = input("Enter PIN To Unlock: ")
print("Phone Unlocked")

print("=================")

# For Loop 
prices_products = [1000,1500,2000,2500,100000] # List Type 

# Requirement: Some Offer Is Running -> Provide Discount Of 100 On Each Product 
# In List We Have Index Concept, Index Starts From Zero and keeps increasing 
print(prices_products)
# print(prices_products[index])
print(prices_products[0])
print(prices_products[1])
print(prices_products[2])
# . 
# . 
# print(prices_products[14999]) 

print("Prices After Applying Discount")
print(prices_products[0] - 100)
print(prices_products[1] - 100)
print(prices_products[2] - 100)

print("=================")

# applying for loop 
prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,100000]
# for variable_name in sequence:
#     block of code 
print("Prices Before Applying Discount")
for price in prices_products:
    print(price)
    
print("=================")    

print("Prices After Applying Discount")
for price in prices_products:
    print(price - 100)
    
print("=================")  

for num in range(5):
    print(num)

print("=================")  

for num in range(10,16,1): # 10 to 15
    print(num)
    
print("=================")  

for num in range(1,10,2): # 1,3,5,7,9
    print(num)
    
print("=================")  

# I Need Multiples Of 5 starting from 5 to 50
for num in range(5,51,5): # 5, 10, 15 ..... 50
    print(num)
    
print("=================")  

for num in range(1,10,1):
    print(num)
    
print("=================")  

for num in range(10,1,-1):
    print(num)
    
print("=================")  

# Greet Good Morning 
print("Good Morning")

# Greet Good Morning For 5 Times 
print("Good Morning")
print("Good Morning")
print("Good Morning")
print("Good Morning")
print("Good Morning")

print("=================") 

# Greet Good Morning For 2500 Times 
for num in range(1,2501,1):
    print("Good Morning: ",num)
