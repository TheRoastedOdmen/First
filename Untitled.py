x = int(input('x: '))

#prints uneven numbers in the range of x
def numbers(x):
  for i in range(x):
    if not i % 2 == 0:
      yield i

print()
for i in numbers(x): #prints in column
  print(i)

print()
print(list(numbers(x))) #prints in list

#prints the sum of every number in the range of x
def f(x):
  res = 0
  for i in range(x + 1):
    res += i
  return res

print()
print('sum: ', f(x))

#prints the list of numbers (+i) in the range of x
def f1(x):
  res = 0
  for i in range(x + 1):
    res += i
    yield res

print()
for i in f1(x):
  print(i) #prints in column

print()
print(list(f1(x))) #prints in list