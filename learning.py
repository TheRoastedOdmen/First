x = int(input('x: '))

#prints uneven numbers in the range of x
def numbers():
  for i in range(x):
    if not i % 2 == 0:
      yield i

print()
for i in numbers(): #prints in column
  print(i)

print()
print(list(numbers())) #prints in list

print('_','\n_')

#prints the sum of every number in the range of x
def f():
  res = 0
  for i in range(x + 1):
    res += i
  return res

print()
print('sum: ', f())

print('_','\n_')

#prints the list of numbers (+i) in the range of x
def f1():
  res = 0
  for i in range(x + 1):
    res += i
    yield res

print()
for i in f1():
  print(i) #prints in column

print()
print(list(f1())) #prints in list