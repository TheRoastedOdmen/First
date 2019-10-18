class Student: 
    def __init__(self, name):
        self.name = name
        
    def sayhi(self):
        print('Hi from ' + self.name)

s1 = Student('Dima')
s1.sayhi()

class Dog:
    def __init__(self, name, color, bark):
        self.name = name
        self.color = color
        self.bark = bark

    #def bark(self):
    #    print("Woof!") #not needed cuz 15 line

fido = Dog("Fido", "brown","Woof!")
print(fido.name,fido.color,fido.bark)