from max2min2 import max2
from max2min2 import min2

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

def max3(x,y,z):
    return max2(x, max2(y,z))

print()
print('Maximum: ', max3(x,y,z))

def min3(x,y,z):
    return min2(x, min2(y,z))

print()
print('Minimum: ', min3(x,y,z))