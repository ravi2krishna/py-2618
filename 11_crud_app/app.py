# Student Management System

# Menu Based System -> In Future, if you learn Full Stack, Replace Menus With UI Elements Like Buttons 

# System Setup -> READ ONLY(Tuple)
# system_info = ("Digital Tech","Student Management System","v1")
SYSTEM_INFO = ("Digital Tech","Student Management System","v1")

# Admin Info -> READ ONLY(Tuple)
ADMIN_INFO = ("9999999999","admin@digital.com")

# Display System Info 
print("=" * 50)
print(f"       Welcome To {SYSTEM_INFO[0]}")
print(f"       {SYSTEM_INFO[1]}")
print(f"       Application Version: {SYSTEM_INFO[-1]}")
print("=" * 50)

# Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores, Skills 
# Represent Student Data In Dictionary 

students = {}

# students = {
#     "101":{
#         "name": "Ravi",
#         "scores": [90,80,70],
#         "skills": {"python","ai"}
#     },
#     "102":{
#             "name": "John",
#             "scores": [90,90,70],
#             "skills": {"java","sql"}
#     }
# }

# Build Menu Based System For Different CRUD Operations 

while True:
    print("Choose An Option: ")
    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        # Create Student 
        print("=" * 30)
        print("     Adding Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        
        if student_id in  students:
            print(f"OOPS!!! Student ID {student_id} Already Exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score Should Be (0-100) Only")
                else:
                    print("Invalid Score, Only Digits Allowed")
            
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input)
                    
            print(students) # Before Adding 
            
            print("========== Student Added ==========")
            
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print(students) # After Adding i.e For Confirmation
                        

    elif choice == "2":
        # Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)  

    elif choice == "3":
        # Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)    
        
    elif choice == "4":
        # Reading Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30) 
    
    elif choice == "5":
        # Exit Application
        print("=" * 30)
        print("     Exiting Application")
        print("=" * 30) 
        # Display System Info 
        print("=" * 50)
        print(f"    Admin Contact Number - {ADMIN_INFO[0]}")
        print(f"    Admin Email ID - {ADMIN_INFO[-1]}")
        print("=" * 50)
        break
        
    else:
        # Invalid Choice
        print("=" * 30)
        print("     Invalid Option Selected, Use Only (1-5)")
        print("=" * 30) 
        
        