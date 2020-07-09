def square(a):
	return a ** 2


print(map(square, range(5)))
print(set(map(square, range(5))))  # map нужно заключить во множество

"""Что происходит:
list = []
for num in range(5):
	list.append(square(num))"""

"""С помощью lambda:
set(map(lambda x: x ** 2, range(5)))"""


def is_pos(a):
	return a > 0


print(list(filter(is_pos, range(-10, 11))))  # если is_pos == True, возвращает число и идет дальше
