# Tuples Methods / Operations 

data = (10,20,30,40,50)
# index(): Used To get Index Position Of Value
data.index(30)
print(data)
print(data.index(30)) # Position Of 30

data = (10,20,30,40,50)
data = (10,20,10,30,10,40,50,10)
print(data)
# count(): Count Of The Number Of Occurrences 
print(data.count(10))

# Requirement, Store Multiple Employee PAN ID's    
pan_ids = ["ABCDE1234A","ABCDE1234B","ABCDE1234C","ABCDE1234D","ABCDE1234E","ABCDE1234A","ABCDE1234D"]
print(pan_ids) # Before
print(pan_ids[0])
# Trying To Modify 1st PAN ID 
pan_ids[0] = "LMNOP5678Z"
print(pan_ids[0])
print(pan_ids) # After

print("=" * 50)

# Requirement, Store Multiple Employee PAN ID's    
pan_ids = ("ABCDE1234A","ABCDE1234B","ABCDE1234C","ABCDE1234D","ABCDE1234E","ABCDE1234A","ABCDE1234D")
print(pan_ids) # Before
print(pan_ids[0])
# Trying To Modify 1st PAN ID 
pan_ids[0] = "LMNOP5678Z" # TypeError: 'tuple' object does not support item assignment
print(pan_ids[0])
print(pan_ids) # After