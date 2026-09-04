# Operators

# Arithmetic Operators 

num1 = 10
num2 = 5

print("Sum Of Numbers: ", num1 + num2)
print("Difference Of Numbers: ", num1 - num2)
print("Product Of Numbers: ", num1 * num2)
print("Division Of Numbers: ", num1 / num2)
print("Modulus Of Numbers: ", num1 % num2)

print("Normal Division: ", 3/2)
print("Floor Division: ", 3//2)
print("Exponentiation: ", 3**2) # 3 ^ 2

# Compound Assignment Operators 
num = 10
num = num + 5 # long form
print(num)

num = 10
num += 5 # short form
print(num)

# Increment and Decrement Operations 
count = 1
print(count)
# count++ # SyntaxError: invalid syntax
count += 1
print(count)
count += 1
print(count)
count += 1
print(count)

count = 10
print(count)
# count++ # SyntaxError: invalid syntax
count -= 1
print(count)
count -= 1
print(count)
count -= 1
print(count)

# Comparison Operators 
num1 = 3
num2 = 2 

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)

print("=================")

# Logical Operators 
num1 = 4
num2 = 3
num3 = 2
num4 = 1

print(num1 > num2 and num3 > num4) # T and T -> T
print(num1 > num2 and num3 < num4) # T and F -> F

print(num1 > num2 or num3 > num4) # T or T -> T
print(num1 > num2 or num3 < num4) # T or F -> T

print(num1 > num2) # T 
print(not num1 > num2) # T 

print("=================")

# Membership Operators 
data = "python is an programming language"
find_word = "java"
status = find_word in data
print(status)

data = "python is an programming language"
find_word = "python"
status = find_word in data
print(status)

data = "python is an programming language"
find_word = "java"
status = find_word not in data
print(status)

# List Data Type -> Complex Data Types Used To Store Multiple Values, Represented Using []
list_employee_ids = [101,102,103,105,108,112,120]
find_emp_by_id = 120
status = find_emp_by_id in list_employee_ids
print("Employee Found: ",status)
print("Employee Found: ",104 in list_employee_ids)

print("=================")

# Identity Operators 

value_x = 10 # 1234
print(id(value_x))

value_y = 100 # 4567
print(id(value_y))

value_z = 10 # 1234
print(id(value_z))

print(value_x is value_y)
print(value_x is value_z)

print("=================")

# Bitwise Operators 
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000111
       # 0000000000000001

print(n1 & n2) # 1 
print(n1 | n2) # 7