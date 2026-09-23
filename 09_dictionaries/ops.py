# Dict Methods / Operations 

data = {"a":"apple","b":"banana"}
print(data)

# update(): Add / Update Items In Dictionary 
data.update({"a":"apricot"}) # If key is already present, then updates it 
print(data)

data.update({"c":"cheery"}) # If key is not present, then adds it 
print(data)

# pop(): Remove Item By Key 
data = {"a":"apple","b":"banana"}
print(data)
# data.pop("b")
print(data.pop("b"))
print(data)

data = {"a":"apple","b":"banana"}
print(data)
# popitem(): Remove Last Item 
data.popitem()
print(data)

# clear(): Removes Everything and Empties Dictionary 
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

data = {"a":"apple","b":"banana"}
print(data)
# get(): used to get the value for key 
data.get("a")
print(data.get("a"))
print(data.get("z"))

# keys(): Used To get Keys 
data = {"a":"apple","b":"banana"}
print(data)
data.keys()
print(data.keys())

for key in data.keys():
    print(key) 

data = {"a":"apple","b":"banana"}
print(data)    
# values(): Used To get Values
data.values()
print(data.values())

for value in data.values():
    print(value) 
    

data = {"a":"apple","b":"banana"}
print(data)    
# items(): Used To get Keys & Values
data.items()
print(data.items())
for item in data.items():
    print(item)

data = {"a":"apple","b":"banana"}
print(data)    
# setdefault(): returns a value of key, if the key is already present
# if key doesn't exist, then adds the item and returns the value
data.setdefault("b","blueberry")
print(data.setdefault("b","blueberry"))

print(data.setdefault("c","cherry"))
print(data)  

data = {"a":"apple","b":"banana"}
print(data) 
# copy(): Makes Dictionary Copy 
backup = data.copy()
print(backup)