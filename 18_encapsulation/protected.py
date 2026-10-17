# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e __ Special Naming Convention or Prefix 
        
class B(A):
    def showA(self):
        a = A(10)
        print(a.__a) # Accessing Private Data in Sub Class 
        # AttributeError: 'A' object has no attribute '_B__a'. Did you mean: '_A__a'?

obj = B(100)
# obj.showA()


# Protected Access 

class A:
    def __init__(self,a):
        self._a = a # Protected i.e _ Special Naming Convention or Prefix 
        
class B(A):
    def showA(self):
        a = A(10)
        print(a._a) # Accessing Protected Data in Sub Class 

obj = B(100)
obj.showA()