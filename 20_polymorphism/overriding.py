# Method Overriding Supported 

class Animal():
    def sound(self):
        print("Some Animal Makes Sound")
        

class Dog(Animal):
    def sound(self):
        print("Dog Animal Makes Sound - Woof")
        
        
class Cat(Animal):
    def sound(self):
        print("Cat Animal Makes Sound - Meow")
            
animal_obj = Animal()
animal_obj.sound()

dog_obj = Dog()
dog_obj.sound()

cat_obj = Cat()
cat_obj.sound()