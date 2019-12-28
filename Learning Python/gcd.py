def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    if a < b:
        return (a, b - a)

print(gcd(21, 7))

def gcd2(a,b):
    return (a if b==0 else  gcd2(b, a%b))

print(gcd2(7, 21))