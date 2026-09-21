# Lists 

# Empty Lists 
empty_list = []
print(empty_list)
print(type(empty_list))

empty_list = list()
print(empty_list)
print(type(empty_list))

# List With Numeric Data 
data = [10,20,30,40,50]
print(data)

# List With Text Data 
data = ["python","ai","cloud"]
print(data)

# List With Mixed Data 
data = [10,20,30,"python","ai",5.5,True]
print(data)

# Accessing Data In Lists 
data = [10,20,30,40,50]
print(data)

# First Element 
first_element = data[0]
print(first_element)

# Last Element 
last_element = data[-1]
print(last_element)

# Unknown Element 
# unknown_element = data[10] # IndexError: list index out of range
# print(unknown_element)

# Slicing In Lists is Same As Strings 
data = [10,20,30,40,50]
print(data[1:3:1]) # 20,30 
print(data[0:5:2]) # 10,30,50 

# Access Individual Elements 
data = [10,20,30,40,50]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# Access Individual Elements -> 10k elements 
data = [10,20,30,40,50,100000]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# print(data[9999])

print("=" * 50)

# Access Individual Elements -> 10k elements 
data = [10,20,30,40,50,100000]

for num in data:
    print(num)

print("=" * 50)

# Apply Operators -> Requirement: Multiply Each Number With 10     
data = [10,20,30,40,50]
for num in data:
    print(num * 10)
    
print("=" * 50)

# Apply Operators -> Requirement: Give Courses In Capital Form 
data = ["python","ai","cloud"]
print(data)
for course in data:
    print(course.upper())

print("=" * 50)

# Apply Operators -> Requirement: Give Only Even Numbers
data = [10,20,35,45,50]
for num in data:
    if num % 2 == 0:
        print(num)
        
print("=" * 50)

# Duplicates Allowed
data = [10,20,10,30,10,40,50,10]
print(data)

print("=" * 50)

# Insertion Order Preserved
data = [10,20,10,30,10,40,50,10]
print(data)

print("=" * 50)

# List Operations / Methods 
print(dir(data))