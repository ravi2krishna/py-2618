# Modules 

# Inbuilt Modules

# 1st Syntax 
# import module (this imports complete module i.e loads all the Functionalities in module)
# print(sqrt(25))
# print(math.sqrt(25))

import math
print(math.sqrt(25))
print(math.pi)

print("=" * 50)

# 2nd Syntax 
# from module import specific_functionality (import only what you need) # Recommended

# Requirement is only pi value 
from math import pi 
print(pi)
# print(sqrt(25))

print("=" * 50)

# Requirement is only pi value and sqrt
from math import pi,sqrt 
print(pi)
print(sqrt(25))

print("=" * 50)