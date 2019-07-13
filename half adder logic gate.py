print('Half adder logic gate')
print('Enter 2 source states. Values >1 will return 1; values <0 will return 0\n')

#input module
a = int(input('Enter the first state: '))
b = int(input('Enter the second state: '))

#converting module
if a > 1:
    a = 1
if a < 0:
    a = 0

if b > 1:
    b = 1
if b < 0:
    b = 0

print('First source: ', a)
print('Second source: ',b)

#logic module
if a == 1 and b == 1:
    print ('1 0')
if a == 0 and b == 0:
    print ('0 0')
if a    !=    b     :
    print ('0 1')
