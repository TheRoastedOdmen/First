print('Full adder logic gates')
print('Enter 4 source states. Values >1 will return 1; values <0 will return 0\n')

#input module
a = int(input('Enter the first source: ' ))
b = int(input('Enter the second source: '))
c = int(input('Enter the third source: ' ))
d = int(input('Enter the fourth source: '))

#convertation module
if a > 1:
    a = 1
if a < 0:
    a = 0

if b > 1:
    b = 1
if b < 0:
    b = 0

if c > 1:
    c = 1
if c < 0:
    c = 0

if d > 1:
    d = 1
if d < 0:
    d = 0

print('First source:  ',a)
print('Second source: ',b)
print('Third source:  ',c)
print('Fourth source: ',d)

print('\nBin: ', a,b, '+' ,c,d)

bool(a) == 1
bool(b) == 1
bool(c) == 1
bool(d) == 1
#logic module (first adder)
if a == 1 and b == 1 and :
    a = 1
    b = 0
    print ('\nSum: ',a,b,c,d)
if a == 0 and b == 0:
    a == 0
    b == 0
    print ('\nSum: ',a,b,c,d)
if a    !=    b     : #XOR
    a == 0
    b == 1
    print ('\nSum: ',a,b,c,d)


