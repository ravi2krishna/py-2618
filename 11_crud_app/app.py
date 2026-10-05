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
        
        student_id = input("Enter ID: ")
        
        if student_id in  students:
            new_name = input("Enter New Name To Update: ").title()
            students[student_id]['name'] = new_name
            print("=" * 30)
            print(f"Student ID {student_id} Updated")
            print("=" * 30)  
        else:
            print("=" * 30)
            print(f"OOPS!!! Student ID {student_id} Doesn't Exist")
            print("=" * 30)  
        
        print(students) # After Updating i.e For Confirmation

    elif choice == "3":
        # Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)    
        
        student_id = input("Enter ID: ")
        
        if student_id in  students:
            
            students.pop(student_id)
            
            print("=" * 30)
            print(f"Student ID {student_id} Deleted")
            print("=" * 30)  
        else:
            print("=" * 30)
            print(f"OOPS!!! Student ID {student_id} Doesn't Exist")
            print("=" * 30)  
        
        print(students) # After Deleting i.e For Confirmation        
        
    elif choice == "4":
        # Reading Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30) 
        
        student_id = input("Enter ID: ")
        
        if student_id in  students:
            # {'102': {'name': 'John', 'scores': [90,80,70], 'skills': {'cloud'}}}
            data = students[student_id] # assuming student_id is 102 
            # {'102': {'name': 'John', 'scores': [90,80,70], 'skills': {'cloud'}}} 
            # ID is already in student_id
            # data = {'name': 'John', 'scores': [90,80,70], 'skills': {'cloud'}}
            name = data['name']
            scores = data['scores'] # All Scores 
            
            # Average Score 
            total_score = 0 # 90 + 80 + 70
            count_scores = 0 # 1 + 1 + 1
            
            for score in scores:
                total_score += score
                count_scores += 1 
            
            average_score = total_score / count_scores 
            
            # Highest Score [90,80,70] - 90 
            high_score = scores[0] # 90 
            
            for score in scores:
                if score > high_score:
                   high_score = score
                   
            # Lowest Score [90,80,70] - 70 
            low_score = scores[0] # 90 
            
            for score in scores:
                if score < low_score:
                   low_score = score
            
                  
            skills = data['skills'] # All Skills
            
            # Skills Count 
            skill_count = 0
            for skill in skills:
                skill_count += 1 
                
            # Displaying Student Information 
            print("=" * 30)
            print("     Student Information")
            print("=" * 30) 
            
            print(f"Student ID: {student_id}")    
            print(f"Student Name: {name}")    
            print(f"All Scores: {scores}")    
            print(f"Average Score: {average_score}")    
            print(f"Highest Score: {high_score}")    
            print(f"Lowest Score: {low_score}")    
            print(f"All Skills: {skills}")    
            print(f"Skills Count: {skill_count}")    
            
        else:
            print("=" * 30)
            print(f"OOPS!!! Student ID {student_id} Doesn't Exist")
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
        
        