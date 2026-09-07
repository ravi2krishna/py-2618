# Conditional Structures (Decision Making Statements) 

# if 

if True: # bool -> True / False 
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")
    
print("================")

if False: # bool -> True / False - Code is not analyzed because condition is statically evaluated as false
    print("This") 
    print("Is")
    print("Block")
    print("Of")
    print("Code")

# with dynamic conditions
if 5 > 2:
    print("Yes 5 > 2 Is Correct")
    
if 5 < 2:
    print("Yes 5 < 2 Is Correct")