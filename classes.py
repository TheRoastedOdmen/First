class Student: 
    def __init__(self, name):
        self.name = name
        
    def sayhi(self):
        print('Hi from ' + self.name)

s1 = Student('Dima')
print()
s1.sayhi()

class Animal:
    def __init__(self,name,color,voice):
        self.name = name
        self.color = color
        self.voice = voice
#class cat(Animal):
    #def purr(self):
       # print("Purr")
#class dog(Animal):
    #def bark(self):
       # print("Woof")

fido = Animal("Fido", "brown", "bark")
Teffi = Animal("Teffi", "white", "purr")
print()
print(fido.name, fido.color, fido.voice)
#fido.bark()
print()
print(Teffi.name, Teffi.color, Teffi.voice)
#Teffi.purr()

class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  #def bark(self):
    #print("Grr...")

class Dog(Wolf):
  def bark(self):
    print("Woof")
      #this will reassign last def bark
      
husky = Dog("Max", "grey")
print('\n', husky.name, husky.color)
husky.bark()