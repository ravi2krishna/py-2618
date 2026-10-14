# Exception Handling 

# When No Errors -> Nothing To Handle 

print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 5

print("Result: ",num1/num2)

print("Program Execution Completed")

print("=" * 50)

# When Errors Come -> 

print("=" * 50)

# print("Program Execution Started")

# num1 = 10
# num2 = "5"

# print("Result: ",num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'

# print("Program Execution Completed")

# print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = "5"

try:
    print("Result: ",num1/num2) 
except:
    print("WARNING! Don't Divide Numerics With Strings, Pass Only Numeric Values")

print("Program Execution Completed")

print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ",num1/num2) 
except:
    print("WARNING! Don't Divide Numerics With Strings, Pass Only Numeric Values")

print("Program Execution Completed")

print("=" * 50)

# print("Program Execution Started")

# num1 = 10
# num2 = 0

# print("Result: ",num1/num2) # ZeroDivisionError: division by zero

# print("Program Execution Completed")

# print("=" * 50)

# 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!!!! Check This - https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!!!! Check This - https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)


# When We Come Across Multiple Errors
print("Program Execution Started")

# data = [1,2,'three',0,4]

# data = [1,2,0,4]

data = [1,2,4]

for num in data:
    print(1/num) # 1/1 - 1/2 - 1/three - 1/0 - 1/4
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    
print("Program Execution Completed")

print("=" * 50)

# When We Come Across Multiple Errors
print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num) # 1/1 - 1/2 - 1/three - 1/0 - 1/4
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
    except:
        print("OOPS!!!!! Something Went Wrong")
    
print("Program Execution Completed")

print("=" * 50)

# When We Come Across Multiple Errors
print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num) # 1/1 - 1/2 - 1/three - 1/0 - 1/4
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
    except TypeError:
        print("OOPS!!!!! Don't Divide Numerics With Strings")
        
    except ZeroDivisionError:
        print("OOPS!!!! Check This - https://en.wikipedia.org/wiki/Division_by_zero")
        
    # except:
    #     print("OOPS!!!!! Some Generic Error Message")
    
print("Program Execution Completed")

print("=" * 50)

# else when no error
print("Program Execution Started")

num1 = 10
num2 = 3

try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!!!! Check This - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Successful")

print("Program Execution Completed")

print("=" * 50)

# else when error came
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ",num1/num2) # Verify Login Credentials 
except:
    print("OOPS!!!! Check This - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Successful") # Then Only Check For OTP

print("Program Execution Completed")

print("=" * 50)


# finally - Run This Code For Sure
print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ",num1/num2) # Verify Login Credentials 
except:
    print("OOPS!!!! Check This - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Successful") # Then Only Check For OTP
finally:
    print("Closing All Opened File Streams & Database Connections")

print("Program Execution Completed")

print("=" * 50)

# Without User Defined Exceptions
age = int(input("Enter Your Age: "))

if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
print("=" * 50)

# Create User Defined Exception 
class UnderAgeError(Exception):
    pass 

age = int(input("Enter Your Age: "))


if age < 18:
    # print("You Cannot Vote")
    # raise TypeError # Unrelated Error
    # raise UnderAgeError # # ZeroDivisionError: division by zero
    raise UnderAgeError("Below 18 Cannot Vote")
else:
    print("You Can Vote")