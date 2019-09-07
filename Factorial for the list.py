y = []

while True:
    try:
        x = int(input('x: '))
        y.append(x)
    except:
        break

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

print()
for x in y:
    print('Results: ', fact(x))