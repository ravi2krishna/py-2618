# Dictionaries 

# Empty Dictionaries 
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# Dict With Numeric Data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# Dict With Text Data 
data = {"c1":"python","c2":"ai","c3":"cloud"}
print(data)

# Dict With Mixed Data 
data = {1:10,2:20,3:30,"c1":"python","c2":"ai","avg":5.5,"passed":True}
print(data)

# Accessing Data In Lists 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# First Element 
# first_element = data[0] # KeyError: 0
first_element = data[1] # here 1 is key, not index
print(first_element)

# Last Element 
last_element = data[5]
print(last_element)

# Unknown Element 
# unknown_element = data[10] # KeyError: 10
# print(unknown_element)

# Not Support For Slicing In Dictionaries
# data = (10,20,30,40,50)
# print(data[1:3:1]) # 20,30 
# print(data[0:5:2]) # 10,30,50

# Access Individual Elements 
data = {1:10,2:20,3:30,4:40,5:50}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

# Access Individual Elements -> 10k elements 
data = {1:10,2:20,3:30,4:40,5:50,100:10000}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# print(data[9999])
print("=" * 50)


# Access Individual Elements -> 10k elements 
data = {1:10,2:20,3:30,4:40,5:50,100:10000}

for num in data:
    print(num) # Only Keys We Got

print("=" * 50)


for key in data:
    print(data[key]) # earlier it was data[index] now data[key]

print("=" * 50)

# Apply Operators -> Requirement: Multiply Each Number With 10     
data = {1:10,2:20,3:30,4:40,5:50}
for key in data:
    print(data[key] * 10)
    
print("=" * 50)

# Apply Operators -> Requirement: Give Courses In Capital Form 
data = {"c1":"python","c2":"ai","c3":"cloud"}
print(data)
for course in data:
    print(data[course].upper())

print("=" * 50)

# Apply Operators -> Requirement: Give Only Even Numbers
data = {1:10,2:20,3:35,4:45,5:50}
for num in data:
    if data[num] % 2 == 0:
        print(data[num])
        
print("=" * 50)

# Duplicates Allowed - Values
data = {1:10,2:20,3:10,4:40,5:10} # Values Can Be Duplicated 
print(data)

print("=" * 50)

# Duplicates Not Allowed - Keys (Overrides)
data = {1:10,2:20,1:100,4:40,5:10} # Values Can Be Duplicated 
print(data)

print("=" * 50)

# Keys Must Be Immutables 
data = {"ten":10,"twenty":20,3:30}
print(data)

print("=" * 50)

# data = {["ten"]:10,["twenty"]:20,3:30} # TypeError: unhashable type: 'list'
# print(data)

data = {("ten"):10,("twenty"):20,3:30} # TypeError: unhashable type: 'list'
print(data)
print("=" * 50)


# Insertion Order Preserved
data = {1:10,2:20,3:10,4:40,5:10}
print(data)

print("=" * 50)


# Dictionary Operations / Methods 
print(dir(data))