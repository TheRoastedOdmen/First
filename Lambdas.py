x = int(input('x: '))

def func(f,a):
    return f(a)

func(lambda x: 30/6*x, 1)
#5

print((lambda x: 30/6*x) (x))