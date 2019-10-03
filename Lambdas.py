def func(f,a):
    return f(a)

func(lambda x: 30/6*x, 1)
#no output here

print((lambda x: 30/6*x) (1))
#5