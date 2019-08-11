x = int(input('x: '))

#prints uneven numbers in the range of x
def numbers(x):
  for i in range(x):
    if not i % 2 == 0:
      yield i

print(list(numbers(x)))

#prints the sum of every number in the range of x
def f(x):
  res = 0
  for i in range(x + 1):
    res += i
  return res

print(f(x))

#prints the list of numbers (+i) in the range of x
def f1(x):
  res = 0
  for i in range(x + 1):
    res += i
    yield res

print(list(f1(x)))