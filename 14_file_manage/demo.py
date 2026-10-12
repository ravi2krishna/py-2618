# File Management With Python 

# Syntax - 1 
# file = open("file_path","mode") 
# file = open("file.txt","r") 

# file_data = open("file.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# print(file_data)

file_data = open("14_file_manage/file.txt","r") 
print(file_data)

print(file_data.closed) # False --> Still Open 
file_data.close() # Flush and close the IO object (explicit closing)
print(file_data.closed) # True --> Now File Is Closed

print("=" * 50)

# Syntax - 2 (Recommended)

# with open("file.txt","r") as alias_name:
#     statements 

with open("14_file_manage/file.txt","r") as file_data:
    print(file_data) 
    
print(file_data.closed) # True --> Now File Is Closed (implicit closing)
# file_data.close() # Flush and close the IO object (explicit closing)
# print(file_data.closed) # True --> Now File Is Closed    

print("=" * 50)

# Read Data From File
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data) 
    print(file_data.read()) 
    
print("=" * 50)

# Create File On Disk 
# with open("14_file_manage/write.txt","x") as file_data:
with open("14_file_manage/write.txt","w") as file_data:
    print("Creating File")
    print(file_data) 
print("=" * 50)

# Write/Update Data To File/Disk 
with open("14_file_manage/write.txt","w") as file_data:
    print("Creating File")
    # print(file_data.write("This File Was Created Using Python")) 
    file_data.write("This File Was Created Using Python - On Disk")
print("=" * 50)


# Delete File From Disk 
file_path = "14_file_manage/write.txt"
# os.remove(file_path) # NameError: name 'os' is not defined. Did you forget to import 'os'?
import os 
os.remove(file_path)
print("Deleting File")
print("=" * 50)