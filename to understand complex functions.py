y = float(input("input argument: "))

def apply_twice(func, arg):
    return func(arg)

def add_five(x):
    return x + 5

print(apply_twice(add_five, y))

def apply_twice2 (func, arg):
    return func(func(arg))

print(apply_twice2(add_five, y))