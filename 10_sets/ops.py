# Sets Methods / Operations 

# add(): Add element to set 
data = {10,20,30,40,50}
print(data)
data.add(10)
print(data)
data.add(60)
print(data)

# update(): Add Multiple element to set 
data = {10,20,30,40,50}
print(data)
data.update({60,70,80})
print(data)

# pop(): Remove Random Element 
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): Remove Element By Value 
data = {10,20,30,40,50}
print(data)
data.remove(30)
# data.remove(300) # KeyError: 300
print(data)

# discard(): Remove Element By Value 
data = {10,20,30,40,50}
print(data)
data.discard(30)
data.discard(300) # KeyError: 300
print(data)

# clear(): Remove All and Empties Set
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): Create Copy
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

# Special Methods Specific To Sets (Math Related Ops)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): Combines Sets 
print(s1.union(s2))
print(s1 | s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
# intersection(): Gets Common Elements From Sets 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
# intersection_update(): Gets Common Elements From Sets, Updates Calling Set 
print(s1.intersection_update(s2))
# print(s2.intersection_update(s1)) # s2 = {40, 50}
print(s1)
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
# difference(): Removes Common Elements From Set and Gives Unique Elements 
print(s1.difference(s2)) 
print(s2.difference(s1)) 
print(s1 - s2)
print(s1)
print(s2)


s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
# difference_update(): Removes Common Elements From Set and Gives Unique Elements, Updates Calling Set  
print(s1.difference_update(s2)) 
print(s1) # {10, 20, 30}
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
# symmetric_difference(): Removes Common Elements From Set and Takes Combined Elements From Both The Sets 
print(s1.symmetric_difference(s2)) 
print(s1 ^ s2) 
print(s1) 
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
# symmetric_difference_update(): Removes Common Elements From Set and Takes Combined Elements From Both The Sets, , Updates Calling Set   
print(s1.symmetric_difference_update(s2)) 
print(s1) 
print(s2)

# issubset(): Checks If Given Set is a Subset Of Another Set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s1.issubset(s2))
print(s3.issubset(s1))

# issuperset(): Checks If Given Set is a Superset Of Another Set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s1.issuperset(s2))
print(s3.issuperset(s1))
print(s1.issuperset(s3))

# isdisjoint(): Checks If Sets Have No Common Elements
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
