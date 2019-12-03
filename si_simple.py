x = int(input('x: '))

def is_simple_number(x):
    """Checking if the number is simple. Returning True, else - False"""
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True

print(is_simple_number(x))
print()


def factorize_number(x):
    divisor = 2
    iter = 0
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
            iter += 1
        else:
            divisor += 1
    print(iter)
print(factorize_number(x))