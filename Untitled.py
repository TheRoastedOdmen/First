x = int(input('x: '))

def numbers(x):
  for i in range(x):
    if not i % 2 == 0:
      yield i

print(list(numbers(x)))


y = int(input("y: "))

def f(y):
  res = 0
  for i in range(y):
    res += i
  return res

print(f(y))