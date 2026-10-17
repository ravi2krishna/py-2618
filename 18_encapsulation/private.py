# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e __ Special Naming Convention or Prefix 
        
obj = A(10)

print(obj.a) # AttributeError: 'A' object has no attribute 'a'

