# Strings 

# Single Line Strings
s1 = 'hello' # Recommended
print(s1)
print(type(s1))
print(id(s1))

s2 = "hello" # Recommended
print(s2)
print(type(s2))
print(id(s2))

s3 = '''hello''' # Not Recommended
print(s3)
print(type(s3))
print(id(s3))

s4 = """hello""" # Not Recommended
print(s4)
print(type(s4))
print(id(s4))

# Multi Line Strings
# define_python = 'Python is a high-level, general-purpose programming language. 
#         It emphasizes code readability, simplicity, and ease-of-writing 
#         with the use of significant indentation, "plain English" naming, 
#         an extensive ("batteries-included") standard library, and garbage collection.'

define_python = '''Python is a high-level, general-purpose programming language. 
        It emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, "plain English" naming, 
        an extensive ("batteries-included") standard library, and garbage collection.'''
        
print(define_python)
print(type(define_python))


define_python = """Python is a high-level, general-purpose programming language. 
        It emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, "plain English" naming, 
        an extensive ("batteries-included") standard library, and garbage collection."""
        
print(define_python)
print(type(define_python))

# When you use single quote in a string, enclose them in double quotes 
question = "How are you ?"
# answer = 'i'm fine' # SyntaxError: unterminated string literal (detected at line 49)
answer = "i'm fine"
print(answer)

# When you use double quote in a string, enclose them in single quotes 
question = "How are you ?"
# answer = "i"m fine" # SyntaxError: unterminated string literal (detected at line 55)
answer = 'i"m fine'
print(answer)

# When you use both single quote and double quote in a string, enclose them in triple single / double quotes 
question = "How are you ?"
# answer = "i'm fine i"m fine" # SyntaxError: unterminated string literal (detected at line 61)
answer = '''i'm fine i"m fine'''
print(answer)
answer = """i'm fine i"m fine"""
print(answer)

# Accessing Strings 
text = "python"
print(text)

# Access "individual characters within a string" 
# Positive Indexing
print(text[0])
print(text[1])

# Negative Indexing
print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# print all characters in python
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

print("=========")

text = "python is language"

for character in text:
    print(character)
    
print("=========")

# text = 12345

# for character in text: # TypeError: 'int' object is not iterable
#     print(character)
    
# print("=========")

# Slicing
text = "python"
print(text)

# 0   1 2  3  4  5
# p   y t  h  o  n
# -6 -5 -4 -3 -2 -1 

print(text[0:3:1]) # pyt
# print(text[4:5]) # th -> o
print(text[2:4:1]) # th -> th
print(text[0:5:2]) # pto 

print(text[-4:-1:1]) # tho 
print(text[-4:-1:-1]) # empty 
print(text[-4:-6:1]) # empty 
print(text[-4:-6:-1]) # ty

# String Concatenation 
s1 = "good "
s2 = "morning"
print(s1+s2)

# Formatted String Literals (f-strings)
age = 30 
# print("My Age Is: "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My Age Is {age}")

# String Repetition 
laugh = "HaHa"
print(laugh)

# hard_laugh = "HaHaHaHaHaHaHaHaHaHaHaHaHaHa"
hard_laugh = laugh * 5
print(hard_laugh)

print("=" * 20)
print("      PYTHON")
print("=" * 20)

# String Immutability 
greet = "hi"
print(greet)

greet = "hello" # This is not modifying/changing, this is re-assigning 
print(greet)

greet = "hi"
print(greet)

# Requirement is Print Hi 
print(greet[0])
# greet[0] = 'H' # TypeError: 'str' object does not support item assignment
print(greet[0])

# Example Of An Mutable Data Type i.e List 
greet = ['h','i']
print(greet[0])
greet[0] = 'H'
print(greet[0])
