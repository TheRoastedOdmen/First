x = int(input('x: '))
z = x
print()
while x > 0:
    y = x
    while y > 0:
        y -= 1
        print(y)
    print('-')
    x -= 1
print('stop')

print()

while z > 0:
    y = z
    while y > 0:
        print(y)
        y -= 1
    z -= 1
    print('-')
print('stop')