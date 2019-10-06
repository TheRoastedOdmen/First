x = int(input('x: '))

def func(f,a):
    return f(a)

func(lambda x: 30/6*x, 1)
#5

print('y =',(lambda x: 30/(6*x)) (x))

z = (lambda x: x + 2) (x)
print('z =',z)