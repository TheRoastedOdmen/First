from functools import reduce


def multi(a, b):
	return a * b


print(reduce(multi, [1, 2, 3, 4, 5]))
