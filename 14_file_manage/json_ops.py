# Working With JSON Files 

import json

student = {
    "id":"101",
    "name":"Ravi",
    "email":"ravi2krishna@gmail.com",
    "courses":["python","ai","cloud"],
    "gpa":9.5
}

print(type(student))
print(student)

# Write Above Data To JSON File 
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)

print("=" * 50)
    
# Write Above Data To JSON File With Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
print("=" * 50)

# Read Data from JSON File 

with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    print(type(data))
    
print("=" * 50)

# Requirement: Get Student Name & Number Of Courses he joined from student.json file
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)

print("Student Name: ",data['name'])
print("Student Joined Courses: ",data['courses'])
print("Student Enrolled Courses: ",len(data['courses']))    
print("=" * 50)

# File Based - dump() and load()

# Object Based - dumps() and loads()

student = {
    "id":"101",
    "name":"Ravi",
    "email":"ravi2krishna@gmail.com",
    "courses":["python","ai","cloud"],
    "gpa":9.5
}

print(type(student))
print(student)

print("=" * 50)

# dumps(): Convert python dictionary to json string 
json_data = json.dumps(student)
print(json_data)
print(type(json_data))

print("=" * 50)

# loads(): Convert json string  to python dictionary 
string_data = '{"id": "101", "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "ai", "cloud"], "gpa": 9.5}'
print(string_data)
print(type(string_data))

print("=" * 50)

python_data = json.loads(string_data)
print(python_data)
print(type(python_data))

print("=" * 50)

