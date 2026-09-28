# Sets 

# Empty Set 
empty_set = {} # This is not Set, This is Dictionary, Empty Set Cannot Be Created With {}
print(empty_set)
print(type(empty_set))

# Empty Set 
empty_set = set()
print(empty_set)
print(type(empty_set))

# Set With Numeric Data 
data = {10,20,30,40,50} # Set is Unordered
print(data)
print(type(data))

data = [10,20,30,40,50] # List is Ordered
print(data)
print(type(data))

# Set With Text Data 
data = {"python","ai","cloud"}
print(data)

# Set With Mixed Data 
data = {10,20,30,"python","ai",5.5,True}
print(data)

# Accessing Data In Sets 
data = {10,20,30,40,50}
print(data)

# First Element 
# first_element = data[0] # TypeError: 'set' object is not subscriptable
# print(first_element)

# # Last Element 
# last_element = data[-1]
# print(last_element)

# Access Individual Elements 
# data = {10,20,30,40,50}
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])

print("=" * 50)

# Access Individual Elements -> 10k elements 
data = {10,20,30,40,50,100000}

for num in data:
    print(num)

print("=" * 50)

# Apply Operators -> Requirement: Multiply Each Number With 10     
data = {10,20,30,40,50}
for num in data:
    print(num * 10)
    
print("=" * 50)

# Apply Operators -> Requirement: Give Courses In Capital Form 
data = {"python","ai","cloud"}
print(data)
for course in data:
    print(course.upper())

print("=" * 50)

# Apply Operators -> Requirement: Give Only Even Numbers
data = {10,20,35,45,50}
for num in data:
    if num % 2 == 0:
        print(num)
        
print("=" * 50)

# Duplicates Allowed
data = {10,20,10,30,10,40,50,10}
print(data)

print("=" * 50)

# Insertion Order Preserved
data = {10,20,10,30,10,40,50,10}
print(data)

print("=" * 50)

# Set Operations / Methods 
print(dir(data))

print("=" * 50)

data = {10,20,30,40,50}
print(data)
print(type(data))

data = frozenset({10,20,30,40,50})
print(data)
print(type(data))

print("=" * 50)

print(dir(data))