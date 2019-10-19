class Student: 
    def __init__(self, name):
        self.name = name
        
    def sayhi(self):
        print('Hi from ' + self.name)

s1 = Student('Dima')
print()
s1.sayhi()

class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class cat(Animal):
    def purr(self):
        print("Purr")
class dog(Animal):
    def bark(self):
        print("Woof")

fido = dog("Fido", "brown")
Teffi = cat("Teffi", "white")
print()
print(fido.name,fido.color)
fido.bark()
print()
print(Teffi.name,Teffi.color)
Teffi.purr()