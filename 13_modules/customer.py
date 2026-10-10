# Now Customer Wants To Use Arithmetic Operations and Profile Related Information

# print(maintainer) # NameError: name 'maintainer' is not defined

from mathprofile import maintainer 
print(maintainer)
print(f"Maintainer is {maintainer}")
# print(f"Institute is {institute}") # NameError: name 'institute' is not defined

print("=" * 50)

from mathprofile import maintainer,institute,mul 
print(f"Maintainer is {maintainer}")
print(f"Institute is {institute}")
print(f"Product Of Numbers is ",mul(5,4))
