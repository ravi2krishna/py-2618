# List Methods / Operations 

data = [10,20,30,40,50]
print(data)

# append(): Adds Element To End Of The List 
data.append(60)
print(data)
# data.append(70,80,90)
data.append([70,80,90])
print(data)

data = [10,20,30,40,50]
print(data)

# extend(): Adds Iterable To List 
# data.extend(60,70,80,90)
data.extend([60,70,80,90])
print(data)

data = [10,20,40,50]
print(data)

# insert(): Add Element On Specific Position Based On Index 
# data.append(30)
data.insert(2,30)
print(data)

data = [10,20,30,40,50]
print(data)

# pop(): Removes An Element, By Default Last Element
data.pop()
print(data)
# if index is provided, removes specific element 
data = [10,20,30,40,50]
print(data)
data.pop(2)
# data.pop(20) # IndexError: pop index out of range
print(data)

data = [10,20,30,40,50]
print(data)

# remove(): Remove Element By Value 
# data.remove(100) # ValueError: list.remove(x): x not in list
data.remove(10)
print(data)

data = [10,20,10,30,10,40,50,10]
print(data)
# Remove All 10's 
data.remove(10) # Only One 10 Removed
print(data)


data = [10,20,10,30,10,40,50,10]
print(data)
# Remove All 10's 
for num in data:
    if num == 10:
        data.remove(num)
print(data)

data = [10,20,10,30,10,40,50,10]
print(data)
# Remove All 10's 
while 10 in data:
    data.remove(10)
print(data)    

data = [10,20,30,40,50]
print(data)
# clear(): Removes All Elements and Empties 
data.clear()
print(data)

data = [10,20,30,40,50]
print(data)

# index(): Used To get Index Position Of Value
data.index(30)
print(data)
print(data.index(30)) # Position Of 30

data = [10,20,30,40,50]
data = [10,20,10,30,10,40,50,10]
print(data)
# count(): Count Of The Number Of Occurrences 
print(data.count(10))


data = [10,20,30,40,50]
print(data)
# reverse(): Reverses List 
data.reverse()
print(data)

data = [10,20,40,30,50]
# data = ["a","d","b","c"]
print(data)
# sort(): Sorts Lists, Default is Ascending Order 
data.sort()
print(data)

data = [10,20,40,30,50]
print(data)
data.sort(reverse=True) # Descending Order
print(data)

data = [10,20,30,40,50]
print(data)
backup = data.copy()
print(backup)

# Requirement, Store Multiple Employee PAN ID's    
pan_ids = ["ABCDE1234A","ABCDE1234B","ABCDE1234C","ABCDE1234D","ABCDE1234E","ABCDE1234A","ABCDE1234D"]
print(pan_ids) # Before
print(pan_ids[0])
# Trying To Modify 1st PAN ID 
pan_ids[0] = "LMNOP5678Z"
print(pan_ids[0])
print(pan_ids) # After