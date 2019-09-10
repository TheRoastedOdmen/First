x = int(input('x: '))
print('\nstart\n')

while x > 0:
    print('main iteration')
    y = x
    while y > 0:
        y -= 1
        print(y) 
    x -= 1

print('\nstop')