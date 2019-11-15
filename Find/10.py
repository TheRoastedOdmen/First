flag = False
N = int(input('N: '))
for i in range(N):
    x = int(input('x: '))
    flag  = (x % 10 == 0) or flag
print(flag)
#atleast 1 number must be %10 for True