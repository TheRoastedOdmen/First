from max2min2 import min2

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

def min3(x,y,z):
    return min2(x, min2(y,z))

print()
print(min3(x,y,z))