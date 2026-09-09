# Conditional Structures (Decision Making Statements) 

# if 

if True: # bool -> True / False 
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")
    
print("================")

if False: # bool -> True / False - Code is not analyzed because condition is statically evaluated as false
    print("This") 
    print("Is")
    print("Block")
    print("Of")
    print("Code")

# with dynamic conditions
if 5 > 2:
    print("Yes 5 > 2 Is Correct")
    
if 5 < 2:
    print("Yes 5 < 2 Is Correct")
    
name = "Ravi" # Hard Coding 
print("Your Name: ",name)
# name = _______ # Dynamic

# input() - Reads The Input Fro User 
name = input("Enter Name: ")
print("Your Name: ",name)

num = input("Enter Number: ")
num = int(num)
if num > 0:
# if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print("Given Number Is Positive")
if num < 0:
    print("Given Number Is Negative")

print("====================") 
    
# if-else 
num = int(input("Enter Number: "))
if num > 0:
    print("Given Number Is Positive")
else:
    print("Given Number Is Negative")

print("====================") 
    
# Interpolation 
username = input("Enter Your Username: ")
print("Welcome: "+username)
print("Welcome: ",username) 
print("Welcome: {username} ") 
print(f"Welcome: {username} ") 

print("====================") 

num = int(input("Enter Number: "))
if num > 0:
    print(f"Given Number {num} Is Positive")
else:
    print(f"Given Number {num} Is Negative")

print("====================") 

# Simple Real World Application Use Case 
# Voting Application
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You Can Vote")
else:
    print(f"You Cannot Vote As You Are {age} Only")

print("====================") 
    
# Conditional Expression - Voting App Scenario
# value_if_true if condition else value_if_false 
age = int(input("Enter Your Age: "))
print(f"You Can Vote" if age >= 18 else "You Cannot Vote As You Are {age} Only" )

print("====================")

# Say I Want To Check If Student Passed Or Failed 
marks = int(input("Enter Your Marks: "))
if marks >= 35:
    print("Passed")
else:
    print("Failed")

print("====================")
    
# Say I Want To Check Student Grade 
# 90 and above - A Grade
# 75 and above but below 90 - B Grade
# 60 and above but below 75 - C Grade
# 60 and above but below 50 - D Grade
# 35 and above but below 50 - E Grade
# Below 35 Failed 
# elif ladder 

marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 50:
    print("D Grade")
elif marks >= 35:
    print("E Grade")
else:
    print("Failed")

print("====================")

# match case 
error_code = int(input(("Enter Error Code You See: ")))

match error_code:
    case 200:
        print("Success - OK")
    case 404:
        print("Not Found")    
    case 500:
        print("Internal Server Error")  
    case _:
        print("Unknown Error")
    


# match case 
user_role = input("Enter Your Role: ")
match user_role:
    case "admin":
        print("Full Access")
    case "student":
        print("Read Only Access - Only Watch Videos")    
    case "mentor":
        print("Read & Write Access - Can Watch Videos & Add Videos")    
    case _:
        print("Access Denied")
