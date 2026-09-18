# String Methods / Operations 

greet = "hi"
print(greet)
print(type(greet))
print(dir(greet))

print("=" * 50)

# Requirement is Print Hi 
greet = "hi"

# Manipulation
# capitalize() - Return a capitalized version of the string. 
result = greet.capitalize()
print(type(result))
print(greet)
print(result)

# Transformation
# Simulate Gmail Functionality 
#            RaVI2KRisHnA            --> ravi2krishna@gmail.com (Transformation)

email = input("Enter Email ID: ")
print("Original Email Given: "+email)

# lower(): To convert a string to lowercase in Python, use the built-in lower() method.
transformed_email = email.lower()
print("Transformed Email: "+transformed_email)

# strip(): Return a copy of the string with leading and trailing whitespace removed.
# lstrip(): Return a copy of the string with leading whitespace removed.
# rstrip(): Return a copy of the string with trailing whitespace removed.
transformed_email = transformed_email.strip()
print("Transformed Email: "+transformed_email)

# add domain name using concatenation 
domain = "@gmail.com"
transformed_email = transformed_email + domain 
print("Transformed Email: "+transformed_email)

print("=" * 50)

# Validation
# Simulate PAN CARD Functionality - Validations (Checks)
# https://www.pan.utiitsl.com/
pan = input("Enter PAN ID: ")
print("Original PAN Given: "+pan) # @anomp9912w --> anomp9912w --> an12 --> anomp9912w --> an9912womp

# isalnum() - It returns True if the string contains only letters and numbers
valid_pan = pan.isalnum()
print(f"Given PAN {pan} is {valid_pan}")

if pan.isalnum() and len(pan) == 10:
    print("Original PAN: "+pan)
    # upper() - The upper() method returns a string where all characters are in upper case. 
    print("Transformed PAN: "+pan.upper())
else:
    print(f"Given PAN {pan} is INVALID")
    
# Valid PAN Should Have first 5 has Alphabets, next 4 should be numbers and last should be Alphabet

print("=" * 50)

pan = input("Enter PAN ID: ")
print("Original PAN Given: "+pan)
# ABCDE1234F
if len(pan) == 10:
    first_five = pan[0:5] 
    middle_four = pan[5:9]
    last_one = pan[-1]
    
    # isalpha() - If you need to verify whether an existing string consists purely of alphabetic characters, use the built-in .isalpha()
    # isdigit() - To check if a Python string contains only digits, the most common and direct built-in tool is the isdigit() method.
    if first_five.isalpha() and middle_four.isdigit() and last_one.isalpha():
        print("Transformed PAN: "+pan.upper())
    else:
        print(f"Given PAN {pan} is INVALID")
else:
    print("PAN Should Be 10 Characters Exactly")
    
# Work On Following Task To Verify GST Number 

# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
# https://www.businessbloomer.com/wp-content/uploads/2014/11/woocommerce-add-coupon-automatically-to-cart-if-product.png

contact_number = input("Enter Contact Number Starting With ISD CODE: ")

# Simulate Data Operations Work: CSV Data from a file and perform some operations 
# https://www.datablist.com/learn_images/csv/google_sheet_csv.png
# https://www.slashgear.com/img/gallery/csv-files-explained-what-they-are-and-how-to-open-them/what-are-csv-files-1699455969.jpg
# Name,Email,Age,City,Job_Role
# emp_data = "John,john@apple.com,30,Hyderabad,Developer"
# emp_data = "Michael,michael@google.com,35,Bangalore,Administrator"
# emp_data = "Ravi,ravi@google.com,35,Hyderabad,Manager"
# Requirement is Display Employee Name & Employee Role 