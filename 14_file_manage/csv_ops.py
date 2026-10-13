# Working With CSV Files 

# Read Data 
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read()) 

print("=" * 50)

# Customers Requirement: Fetch Me All Students From Hyderabad
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read().find("Hyderabad")) 

print("=" * 50)

# Using CSV Module 
# Customers Requirement: Fetch Me All Students From Hyderabad
import csv
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[-1] == 'Hyderabad':
            print(row)

print("=" * 50)

# Customers Requirement: Fetch Me All Students From Hyderabad, Who Are Doing Internship With tcs 
import csv
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[-1] == 'Hyderabad':
            print(row)

print("=" * 50)

# Now Because Of Business Requirements, Companies Data Sets are Changed / Updated ---> sample.csv 
# Customers Requirement: Fetch Me All Students From Hyderabad
import csv
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)
        # print(row[-1])
        if row[2] == 'Hyderabad':
            print(row)

print("=" * 50)

# Using DictReader
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        print(row)

print("=" * 50)

# Customers Requirement: Fetch Me All Students From Hyderabad
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row['address'] == 'Hyderabad':
            print(row)

print("=" * 50)

# Now Because Of Business Requirements, Companies Data Sets are Changed / Updated ---> sample.csv 
# Customers Requirement: Fetch Me All Students From Hyderabad
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row['address'] == 'Hyderabad':
            print(row)

print("=" * 50)

# Write Data To CSV File 
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'mobile', 'address', 'email'])
    csv_writer.writerow(['Hari', '9889032187', 'Jaipur', 'hari193@outlook.com'])
    
