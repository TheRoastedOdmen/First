from max2min2 import max2

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

def max3(x,y,z):
    return max2(x, max2(y,z))

print()
print(max3(x,y,z))