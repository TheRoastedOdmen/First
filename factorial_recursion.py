def factorial(x):
    if x == 1:
        return x
    else:
        return factorial(x-1) * x
#the same as: return x if x == 1 else factorial(x-1) * x
print(factorial(5))


