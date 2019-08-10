x = int(input('x: '))

def s(x):
    res = 0
    for i in range(x):
        res += i
        yield res

print(list(s(x)))
