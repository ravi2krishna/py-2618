# Indentation Rules 

# -> When to use Space 
# -> When Not to use Space: Single Statement
# -> How many spaces to use

print("Good Morning") # When Not to use Space ? -> Single Statement

# print("Good Morning") # IndentationError: unexpected indent

# Taking Class Use Case For Indentation 
# class Student:
# student_name = "Ravi" # IndentationError: expected an indented block after class definition on line 12

# When to use Space  ? -> When We Write Block Of Code 

# How many spaces to use ? -> At least One Space is Must, But Recommended is 4 Space(tab)

# At least One Space is Must
class Student:
 student_name = "Ravi"

# two spaces 
class Student:
  student_name = "Ravi"
  
# ten spaces 
class Student:
          student_name = "Ravi"

# Python Allows for any "Consistent Number Of Spaces" 

# widely accepted and Recommended standard is 4 Spaces (tab)
class Student:
    student_name = "Ravi"

# No "Consistent Number Of Spaces" - Error
class Student:
    student_name = "Ravi"
#   student_email = "ravi2krishna@gmail.com" # IndentationError: unindent does not match any outer indentation level


# "Consistent Number Of Spaces" - No Error
class Student:
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
class Trainer:
 trainer_name = "Krishna"
 institute = "Digital Institute"