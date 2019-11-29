def hello(name):
    print('Hello, ', name)
#hello() #requires parametr (argument)
hello("John")

print()

def hello2(name = "World"):
    print('Hello, ', name)
hello2()
hello2('Alice')