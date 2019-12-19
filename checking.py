base = 7
x = int(input())
while x > 0:
    print()
    dig = x % base
    print(dig)
    #print(dig, end='') #no line break
    print()
    x //= base
    print(x)

print()    
print('end')
