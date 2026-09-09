# Nested Conditionals 
# inner condition is only checked if the outer condition is true. 

if True:
    print("1")
if True:
    print("This is NOT Nested Condition")
    
# Nested 
if True:
    print("1")
    if True:
        print("This is Nested Condition")
        if True:
            print("This is Nested Condition")
            
if False:
    print("1") # Code is not analyzed because condition is statically evaluated as false
    if True:
        print("This is Nested Condition")
        
# Real World Nested Condition Use Case
age = int(input("Enter Your Age: "))
if age >= 18:
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID Proof")
else:
    print("You Cannot Vote With Under Age")
    
# Real World Use case 
# Net Banking Login - 1st Authentication(Username & Password) - 2nd (OTP Authorization)
# Multi Factor Authentication (Google Authenticator)

