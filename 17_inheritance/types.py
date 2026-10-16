# Types Of Inheritance 

class Father:
    def house(self):
        print("Has House")
        
class Son(Father): # Single Level Inheritance
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.house()
son_object.car()

print("=" * 50)

class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Son(Father): # Multi Level Inheritance
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.house()
son_object.car()
son_object.land()

print("=" * 50)

class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Mother():
    def gold(self):
        print("Has Gold")
        
class Son(Father,Mother): # Multiple Inheritance
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.house()
son_object.car()
son_object.land()
son_object.gold()

print("=" * 50)

class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Mother():
    def gold(self):
        print("Has Gold")
        
class Son(Father,Mother): # Hierarchical
    def car(self):
        print("Has Car")

class Daughter(Father): # Hierarchical
    def business(self):
        print("Has Business")
       
son_object = Son()
son_object.house()
son_object.car()
son_object.land()
son_object.gold()

daughter_object = Daughter()
daughter_object.business()
daughter_object.house()
daughter_object.land()

print("=" * 50)

class A:
    def a(self):
        print("A")
        
class B(A):
    def b(self):
        print("B")
        
class C(A):
    def c(self):
        print("C")
        
class D(B,C):
    def d(self):
        print("D")
        
obj_d = D()

obj_d.a()
obj_d.b()
obj_d.c()
obj_d.d()