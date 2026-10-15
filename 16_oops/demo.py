# OOP - Object Oriented Programming 

# Class - Blue Print
class Student:
    
    # Student Has Something (Variables)
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Student Does Something (Methods)
    def student_studies():
        print("Student Is Studying Python")

# This is function as it's outside the class        
# def student_studies():
#     print("Student Is Studying Python")

# To Use This Class, We Need Object 
student_object = Student()

# print("Student Name: ",student_name) # NameError: name 'student_name' is not defined
# print("Student Email: ",student_email) # NameError: name 'student_email' is not defined

print("Student Name: ",student_object.student_name) 
print("Student Email: ",student_object.student_email)

# student_studies() # NameError: name 'student_studies' is not defined

# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

print("=" * 50)

# Class - Blue Print
class Student:
    
    # Student Has Something (Variables)
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Student Does Something (Methods)
    # self is object reference 
    def student_studies(self):
        print("Student Is Studying Python")

# To Use This Class, We Need Object 
student_object = Student()

print("Student Name: ",student_object.student_name) 
print("Student Email: ",student_object.student_email)

student_object.student_studies()

print("=" * 50)

# Class - Blue Print
class Student:
    
    # Student Has Something (Variables)
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Student Does Something (Methods)
    # self is object reference 
    def student_studies(self):
        print("Student Is Studying Python")
        print("Student Name: ",student_object.student_name) # object
        print("Student Email: ",self.student_email) # self is also object # Recommended

# To Use This Class, We Need Object 
student_object = Student()

student_object.student_studies()

print("=" * 50)

# Class - Blue Print
class Student:
    
    # Student Has Something (Variables)
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Student Does Something (Methods)
    # self is object reference 
    def student_studies(self):
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Recommended

# To Use This Class, We Need Object 
student_object = Student()

student_object.student_studies()

print("=" * 50)

# Working With Multiple Objects
# Class - Blue Print
class Student:
    
    # Student Has Something (Variables)
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Student Does Something (Methods)
    # self is object reference 
    def student_studies(self):
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Recommended

# To Use This Class, We Need Object 
student_ravi = Student()
student_ravi.student_studies()

student_john = Student()
student_john.student_studies()

student_mike = Student()
student_mike.student_studies()

print("=" * 50)

# Working With Multiple Objects Using Constructor
# Class - Blue Print
class Student:
    
    # Student Has Something (Variables)
    # student_name = "Ravi"
    # student_email = "ravi@gmail.com"
    
    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something (Methods)
    # self is object reference 
    def student_studies(self):
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Recommended

# To Use This Class, We Need Object 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("Ravi","ravi@gmail.com") 
student_ravi.student_studies()

print("=" * 50)

student_john = Student("John","john@gmail.com")
student_john.student_studies()

print("=" * 50)

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()

print("=" * 50)


# Instance Members (Associated With Objects)
# Working With Multiple Objects Using Constructor
# Class - Blue Print
class Student:
    
    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        # Instance Variables are self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something (Methods)
    # self is object reference 
    # Instance Method student_studies
    def student_studies(self):
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Recommended

# To Use This Class, We Need Object 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("Ravi","ravi@gmail.com") 
student_ravi.student_studies()

print("=" * 50)

student_john = Student("John","john@gmail.com")
student_john.student_studies()

print("=" * 50)

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()

print("=" * 50)

# Class Members (Associated With Class)
# Instance Members (Associated With Objects)
# Working With Multiple Objects Using Constructor
# Class - Blue Print
class Student:
    
    # Class Variable - Shared By All Objects
    institute_name = "Digital Institute"
    
    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        # Instance Variables are self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something (Methods)
    # self is object reference 
    # Instance Method student_studies
    def student_studies(self):
        print("Student Is Studying Python")
        # print("Institute Is: ",self.institute_name) # Not Recommended
        print("Institute Is: ",Student.institute_name) # Recommended
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Recommended
        
    # Class methods, acts on Class Variables
    @classmethod
    def change_institute_name(cls,new_institute_name):
        cls.institute_name = new_institute_name
    
# To Use This Class, We Need Object 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("Ravi","ravi@gmail.com") 
student_ravi.student_studies()

print("=" * 50)

student_john = Student("John","john@gmail.com")
student_john.student_studies()

print("=" * 50)

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()

print("=" * 50)

Student.change_institute_name("New Digital Institute")

student_ravi = Student("Ravi","ravi@gmail.com") 
student_ravi.student_studies()

print("=" * 50)

student_john = Student("John","john@gmail.com")
student_john.student_studies()

print("=" * 50)

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()

print("=" * 50)

# Static Members (Not Associated With Classes & Objects)
# Class Members (Associated With Class)
# Instance Members (Associated With Objects)
# Working With Multiple Objects Using Constructor
# Class - Blue Print
class Student:
    
    # Class Variable - Shared By All Objects
    institute_name = "Digital Institute"
    
    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        # Instance Variables are self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something (Methods)
    # self is object reference 
    # Instance Method student_studies
    def student_studies(self):
        print("Student Is Studying Python")
        # print("Institute Is: ",self.institute_name) # Not Recommended
        print("Institute Is: ",Student.institute_name) # Recommended
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Recommended
        
    # Class methods, acts on Class Variables
    @classmethod
    def change_institute_name(cls,new_institute_name):
        cls.institute_name = new_institute_name
        
    # Static Method 
    @staticmethod
    def something():
        print("I Do Something That Is Not Associated With Class nor Object")
    
    
# To Use This Class, We Need Object 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("Ravi","ravi@gmail.com") 
student_ravi.student_studies()

print("=" * 50)

student_john = Student("John","john@gmail.com")
student_john.student_studies()

print("=" * 50)

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()

print("=" * 50)

Student.something()

print("=" * 50)
